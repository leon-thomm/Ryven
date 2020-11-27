import json
import os
import sys

from class_inspection import find_type_in_object
from custom_src.Node import Node, NodePort
from custom_src.Script import Script


class Loader:
    def __init__(self, project_path):

        project_config = self.load_project_config(project_path)

        # select script
        script_config = None
        script_name = None
        script_names = [s['name'] for s in project_config['scripts']]
        while script_name not in script_names:
            print('scripts...')
            for sn in script_names:
                print('    '+sn)
            script_name = input('select script: ')
        for s in project_config['scripts']:
            if s['name'] == script_name:
                script_config = s
                break

        self.nodes = []
        self.node_instance_classes = {}

        #   dynamically import all builtin nodes from Ryven
        builtin_path = '../Ryven/custom_src/builtin_nodes'
        sys.path.append(builtin_path)
        files = [f for f in os.listdir(builtin_path) if
                 os.path.isfile(os.path.join(builtin_path, f)) and f.endswith('.py')]
        for fn in [f for f in files if not f.endswith('_NodeInstance.py')]:
            modname = os.path.splitext(os.path.basename(fn))[0]
            mod = __import__(modname, fromlist=[modname])
            # print(inspect.getsource(mod))
            node_class = getattr(mod, modname)
            node_class_inst = node_class()
            self.nodes.append(node_class_inst)
            for fn2 in [f for f in files if f.endswith('_NodeInstance.py')]:
                modname2 = os.path.splitext(os.path.basename(fn2))[0]
                if modname2.__contains__(modname):
                    mod2 = __import__(modname2, fromlist=[modname2])
                    self.node_instance_classes[node_class_inst] = getattr(mod2, modname2)
                    break
        print(self.nodes)
        print(self.node_instance_classes)

        self.buttonNIClass = None
        required_package_names = list(set([n['parent node package'] for n in script_config['flow']['nodes']
                                           if n['parent node package'] != 'built in']))
        self.imported_package_names = []
        print('required packages:')
        for p_n in required_package_names:
            print('    '+p_n)
        while any([n not in self.imported_package_names for n in required_package_names]):
            package_path = input('input package path or \'auto\': ')
            if package_path == 'auto':
                self.auto_import_packages(required_package_names)
            else:
                self.import_package(package_path)


        # create script
        script = Script(script_config, self.nodes, self.node_instance_classes)

        obj = None  # for referencing a node instance

        print('The flow has been successfully created. What to do next?')

        # MAIN LOOP
        while True:
            command = input(
                                '''
Commands:
    instances       - prints a list of all node instances for direct access
    nodes           - prints a list of all nodes
    button          - gives a list of button nodes you can manually execute
    vars            - prints all script variables
    set var         - sets the value of a variable
    exit            - closes the session
'''
            )

            if command == 'nodes':
                packages = []
                for n in self.nodes:
                    if n.package not in packages:
                        packages.append(n.package)
                packages.sort()
                print(len(self.nodes), 'nodes:')
                for p in packages:
                    for n in self.nodes:  # [node for node in self.nodes if node.package == p]:
                        if n.package == p:
                            print('['+p+']', n.title)

            elif command.startswith('obj'):
                print(eval(command))
            elif command == 'instances':
                index_counter = 0
                for ni in script.flow.all_node_instances:
                    print(index_counter, ni)
                    index_counter += 1
                selected_node_instance = None
                try:
                    selection_index = int(input('ref by index: '))
                    selected_node_instance = script.flow.all_node_instances[selection_index]
                except Exception as e:
                    print('Error:', e)
                    continue
                obj = selected_node_instance
                print('--> obj:',obj)


            elif command == 'button':
                button_node_instances = [ni for ni in script.flow.all_node_instances if find_type_in_object(ni, self.buttonNIClass)]
                if len(button_node_instances) == 0:
                    print('no existing button nodes found')
                    continue
                print('button nodes:')
                for i in range(len(button_node_instances)):
                    print(str(i)+':', button_node_instances[i])
                try:
                    index = int(input('index: '))
                    button_node_instances[index].update()
                except Exception as e:
                    print('Error:', e)
                    continue
            elif command == 'vars':
                print([(v.name, v.val) for v in script.variables_handler.variables])
            elif command == 'set var':  # re.match('setvar [.]+', command):
                var_name = input('name: ')
                var_val = eval(input('val: '))
                script.variables_handler.set_var(var_name, var_val)
            elif command == 'exit':
                sys.exit()
            else:
                pass


    def load_project_config(self, path):
        j_str = ''
        # try:
        f = open('../saves/'+path)
        j_str = f.read()
        f.close()
        # except FileNotFoundError:
        #     raise FileNotFoundError('Project file not found')

        return json.loads(j_str, strict=False)


    def auto_import_packages(self, required_package_names):
        packages_dir = '../packages'
        folders_list = [x[0] for x in os.walk(packages_dir) if
                        os.path.basename(os.path.normpath(x[0])) in required_package_names]

        required_files = required_package_names.copy()

        for folder in folders_list:
            for r_f in required_files:
                if r_f + '.rpc' in os.listdir(packages_dir + '/' + folder):
                    self.import_package(os.path.normpath(packages_dir + '/' + folder + '/' + r_f + '.rpc'))


    def import_package(self, package_path):
        package_name = os.path.splitext(os.path.basename(package_path))[0]
        if package_name in self.imported_package_names:
            return

        j_str = ''
        try:
            f = open(package_path)
            j_str = f.read()
            f.close()
        except FileExistsError and FileNotFoundError:
            print('Error: couldn\'t find an open file')
            return

        # Important: translate the package first (metacore files -> src code files)
        PackageTranslator = self.get_class_from_file(file_path='../Ryven_PackageTranslator',
                                                     file_name='Ryven_PackageTranslator',
                                                     class_name='PackageTranslator')
        package_translator = PackageTranslator(os.path.dirname(os.path.abspath(package_path)))  # translate

        j_obj = json.loads(j_str, strict=False)
        if j_obj['type'] != 'Ryven nodes package' and j_obj['type'] != 'vyScriptFP nodes package':  # old syntax
            return

        nodes_config = j_obj['nodes']
        for n in nodes_config:
            new_node = self.parse_node(n, os.path.dirname(package_path), package_name)
            self.nodes.append(new_node)

        self.imported_package_names.append(package_name)


    def parse_node(self, node_config, package_path, package_name):
        new_node = Node()

        # setting the Node's attributes
        new_node.title = node_config['title']
        new_node.description = node_config['description']
        new_node.type_ = node_config['type']
        new_node.package = package_name
        new_node.has_main_widget = node_config['has main widget']

        inputs_config = node_config['inputs']
        inputs = []
        num_inputs = len(inputs_config)
        for ii in range(num_inputs):
            input_config = inputs_config[ii]
            new_input = NodePort()
            new_input.type_ = input_config['type']
            new_input.label = input_config['label']
            inputs.append(new_input)

        outputs_config = node_config['outputs']
        outputs = []
        num_outputs = len(outputs_config)
        for oi in range(num_outputs):
            j_output = outputs_config[oi]
            new_output = NodePort()
            new_output.type_ = j_output['type']
            new_output.label = j_output['label']
            outputs.append(new_output)

        new_node.inputs = inputs
        new_node.outputs = outputs


        node_module_name = node_config['module name']
        node_class_name = node_config['class name']
        module_name_separator = '___'

        # CUSTOM CLASS IMPORTS ----------------------------------------------------------------------------
        # creating all the necessary path variables here for all potentially imported classes

        #       IMPORT NODE INSTANCE SUBCLASS
        node_instance_class_file_path = package_path + '/nodes/' + node_module_name + '/'
        node_instance_filename = node_module_name  # the NI file's name is just the 'module name'
        new_node_instance_class = self.get_class_from_file(file_path=node_instance_class_file_path,
                                                           file_name=node_instance_filename,
                                                           class_name=node_class_name + '_NodeInstance')
        self.node_instance_classes[new_node] = new_node_instance_class

        if new_node.title.lower() == 'button' and new_node.package == 'std':  # convenience feature for exec. buttons
            self.buttonNIClass = new_node_instance_class


        # ---------------------------------------------------------------------------------------------------

        return new_node


    def get_class_from_file(self, file_path, file_name, class_name):
        sys.path.append(file_path)
        try:
            new_module = __import__(file_name, fromlist=[class_name])
        except ModuleNotFoundError as e:
            print(e, file_path, file_name, class_name)
            sys.exit()
        new_class = getattr(new_module, class_name)
        return new_class


def clean_path_string(param):
    if param.startswith('"') and param.endswith('"') or \
            param.startswith('\'') and param.endswith('\''):
        param = param[1:-1]
    return param


if __name__ == '__main__':
    path = ''

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = clean_path_string(input('project name (or path from saves folder): '))

    while True:
        try:
            f = open('../saves/'+path)
            f.close()
            Loader(path)
        except FileNotFoundError:
            print('couldn\'t open file')
            path = clean_path_string(input('project name (or path from saves folder): '))
