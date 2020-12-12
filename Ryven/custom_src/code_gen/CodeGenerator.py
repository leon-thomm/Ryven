import inspect
import ast
import autopep8

from custom_src.code_gen.CodeGenDialog import CodeGenDialog


class CodeGenerator:
    """In production and *very* experimental."""

    IGNORED_COMMANDS = [
        'from NIENV import *',
        'from NIWENV import *'
    ]

    def __init__(self, main_window, node_instances, vars_manager_config, flow_algorithm_mode):
        self.main_window = main_window
        self.node_instances = node_instances
        self.vars_manager_config = vars_manager_config
        self.flow_algorithm_mode = flow_algorithm_mode

    def generate(self):

        code = ''

        ni_class_ast_dict = {}      # {NodeInstance : [name, ast.AST, ast.ClassDef]}
        ni_class_names = []
        for ni in self.node_instances:
            classname = type(ni).__name__
            if type(ni).__name__ in ni_class_names:
                continue
            ni_class_ast_dict[ni] = [classname,
                                     ast.parse(inspect.getsource(inspect.getmodule(ni))),
                                     ast.parse(inspect.getsource(ni.__class__))]
            ni_class_names.append(classname)

        modules_dict: dict = self.get_modules(ni_class_ast_dict)  # {str: [Import/ImportFrom, bool]}


        # IMPORT DIALOG
        code_gen_dialog = CodeGenDialog(modules_dict, self.main_window)
        accepted = code_gen_dialog.exec_()
        if not accepted:
            return None


        modules_dict = code_gen_dialog.get_import_selection()
        import_module_names = [name for name in modules_dict['imports'].keys()]
        fromimport_module_names = [name for name in modules_dict['fromimports'].keys()]


        # IMPORTS
        imports: [str] = []

        # add import statements
        for m in modules_dict['imports']:
            import_statement_obj = modules_dict['imports'][m][0]
            if modules_dict['imports'][m][1]:
                imports.append(ast.unparse(import_statement_obj))

        for m in modules_dict['fromimports']:
            import_statement_obj = modules_dict['fromimports'][m][0]
            if modules_dict['fromimports'][m][1]:
                import_statement_obj: ast.ImportFrom = modules_dict['fromimports'][m][0]
                import_statement_obj.names = []
                for name in modules_dict['fromimports'][m][2]:
                    import_statement_obj.names.append(ast.alias(name=name))
                imports.append(ast.unparse(import_statement_obj))


        code += '\n'.join(imports)+'\n\n\n'
        imports.clear()

        code += self.get_base_classes_code()

        # replace excluded import statements with source
        for m in modules_dict['imports']:
            if not modules_dict['imports'][m][1]:
                import_statement_obj = modules_dict['imports'][m][0]
                mod = __import__(import_statement_obj.names[0].name)
                source = inspect.getsource(mod)
                imports.append(source)
        for m in modules_dict['fromimports']:
            if not modules_dict['fromimports'][m][1]:
                import_statement_obj: ast.ImportFrom = modules_dict['fromimports'][m][0]
                mod = __import__(import_statement_obj.module,
                                 fromlist=[alias.name for alias in import_statement_obj.names])  # doesn't seem to make a difference
                source = inspect.getsource(mod)
                imports.append(source)


        # ------------------------------------------


        code += '\n\n'.join(imports)


        # CLASSES AND EVERYTHING ELSE
        for ni in ni_class_ast_dict.keys():
            a: ast.AST = ni_class_ast_dict[ni][1]
            for component in a.body:
                comp_src = ast.unparse(component)

                if isinstance(component, ast.Import) and component.names[0].name in import_module_names:
                    # Import (already added)
                    continue
                if isinstance(component, ast.ImportFrom) and component.module in fromimport_module_names:
                    # ImportFrom (already added)
                    continue
                if comp_src in self.IGNORED_COMMANDS:
                    # Ignored Import (like 'from NIENV import *')
                    continue

                code += '\n\n'+ast.unparse(component)

            code += '\n\n\n'

        code += self.create_script_code()

        code = autopep8.fix_code(code)

        return code


    def get_base_classes_code(self):
        f = open('custom_src/code_gen/DefaultCode.py')
        code = f.read()
        f.close()
        return code


    def create_script_code(self):

        nodes = []
        for ni in self.node_instances:
            if ni.parent_node not in nodes:
                nodes.append(ni.parent_node)

        nodes_decl_list = []
        for n in nodes:
            input_decls = ', '.join([f'NodePort(type_=\'{i.type_}\', label=\'{i.label}\')' for i in n.inputs])
            output_decls = ', '.join([f'NodePort(type_=\'{o.type_}\', label=\'{o.label}\')' for o in n.outputs])
            nodes_decl_list.append(f'Node(title=\'{n.title}\', inputs=[{input_decls}], outputs=[{output_decls}])')
        nodes_decl = ', '.join(nodes_decl_list)

        node_inst_decl_list = []
        for ni in self.node_instances:
            params = f'(nodes[{str(nodes.index(ni.parent_node))}], None, {str(ni.config_data())})'
            node_inst_decl_list.append(f'{ni.__class__.__name__}({params})')
        node_inst_decl = ', '.join(node_inst_decl_list)

        connections = []
        for k in range(len(self.node_instances)):
            ni = self.node_instances[k]
            for o in range(len(ni.outputs)):
                out = ni.outputs[o]
                outgoing_connections = []
                for j in range(len(out.connected_port_instances)):
                    cpi = out.connected_port_instances[j]
                    outgoing_connections.append(f'node_instances[{self.node_instances.index(cpi.parent_node_instance)}]'
                                                f'.inputs[{cpi.parent_node_instance.inputs.index(cpi)}]')
                outgoing_connections_str = ', '.join(outgoing_connections)
                connections.append(f'node_instances[{k}].outputs[{o}].connected_port_instances=[{outgoing_connections_str}]')
            for i in range(len(ni.inputs)):
                inp = ni.inputs[i]
                incoming_connections = []
                for j in range(len(inp.connected_port_instances)):
                    cpi = inp.connected_port_instances[j]
                    incoming_connections.append(f'node_instances[{self.node_instances.index(cpi.parent_node_instance)}]'
                                                f'.outputs[{cpi.parent_node_instance.outputs.index(cpi)}]')
                incoming_connections_str = ', '.join(incoming_connections)
                connections.append(f'node_instances[{k}].inputs[{i}].connected_port_instances=[{incoming_connections_str}]')

        connections_decl = '\n    '.join(connections)

        code = \
f'''
def create_nodes():
    nodes = [
        {nodes_decl}
    ]
    return nodes

def create_node_instances():
    node_instances = [
        {autopep8.fix_code(node_inst_decl)}
    ]
    for ni in node_instances:
        ni.initialized()
    return node_instances

def connect_node_instances():
    {connections_decl}

def init_vars():
    manager = VarsManager(config={self.vars_manager_config})
    return manager

if __name__ == '__main__':
    vars_manager = init_vars()
    nodes = create_nodes()
    node_instances = create_node_instances()
    connect_node_instances()
    for ni in node_instances:
        ni.update()

    # ...
'''

        return code


    def get_modules(self, ni_ast_dict: dict) -> dict:
        modules = {'imports': {}, 'fromimports': {}}

        for ni in ni_ast_dict.keys():
            a: ast.AST = ni_ast_dict[ni][1]
            for b in a.body:
                command = ast.unparse(b)
                if command in self.IGNORED_COMMANDS:
                    continue
                if type(b) == ast.Import:
                    c: ast.Import = b
                    for alias in c.names:
                        modules['imports'][c.names[0].name] = [c, True]
                elif type(b) == ast.ImportFrom:
                    c: ast.ImportFrom = b
                    mod_name = c.module
                    names = [a.name for a in c.names]
                    if mod_name in modules['fromimports']:
                        fromnames = modules['fromimports'][mod_name][2]
                        for n in names:
                            if n not in fromnames:
                                fromnames.append(n)
                        modules['fromimports'][mod_name][2] = fromnames
                    else:
                        modules['fromimports'][mod_name] = [c, True, names]

        return modules


# SOME AST REFERENCE
#
# ast.dump(ast.parse('''
# ... import numpy as np
# ... import pyside2
# ... from scipy import linalg
# ... from opencv import *
# ... '''))
# Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pyside2')]),
#              ImportFrom(module='scipy', names=[alias(name='linalg')], level=0),
#              ImportFrom(module='opencv', names=[alias(name='*')], level=0)], type_ignores=[])
