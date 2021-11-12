import inspect
import sys
import json
import os
import importlib
import distutils.sysconfig as sysconfig


def find_builtin_modules():
    # TODO: improve this

    mods = []

    std_lib = sysconfig.get_python_lib(standard_lib=True)
    for top, dirs, files in os.walk(std_lib):
        for nm in files:
            # if nm == '__init__.py':
            #     mods.append(os.path.basename(os.path.normpath(top)))
            if nm != '__init__.py' and nm[-3:] == '.py':
                mods.append(os.path.join(top, nm)[len(std_lib) + 1:-3].replace(os.sep, '.'))

    return mods

def get_nodes(package_file: str) -> list:
    nodes = []

    with open(package_file, 'r') as f:
        package = json.loads(f.read())

        sys.path.append(os.path.dirname(package_file))
        if 'nodes' in sys.modules.keys():
            del sys.modules['nodes']
        mod = __import__('nodes')
        sys.path.remove(os.path.dirname(package_file))

        for node_name in package['nodes']:
            nodes.append(mod.__dict__[node_name])
    
    return nodes


def parse_module(mod_name: str, color: str, target_path: str):

    try:
        module = __import__(mod_name)
    except ImportError:
        return

    routines = []

    for name, obj in inspect.getmembers(module):
        if inspect.isroutine(obj):
            routines.append((name, obj))
    # print(routines)
    node_defs = []

    node_names = []

    for name, obj in routines:
        try:
            sig = inspect.getfullargspec(obj)
        except Exception as e:
            # print(e)
            continue

        # print(f'routine {name} of {mod_name}: {sig}')

        input_signatures = []
        for i in range(len(sig.args)):
            arg = sig.args[i]
            if arg != 'self' and not arg.startswith('_'):

                # default values
                defaults = sig.defaults

                # only the last n parameters have default values
                if defaults is None or i < (len(sig.args)-len(defaults)):
                    input_signatures.append(
                        f'NodeInputBP(label=\'{arg}\'),'
                    )
                else:
                    j = i - (len(sig.args)-len(defaults))
                    v = sig.defaults[j]

                    # make sure the type is correctly converted to a valid code string
                    if type(v) == type:
                        default_val = v.__name__

                    elif type(v) == str:
                        default_val = f'\'{v}\''

                    elif type(v) == object or inspect.isfunction(v):  # seems to be a bug
                        default_val = None

                    else:
                        default_val = v

                    input_signatures.append(
                        f'NodeInputBP(label=\'{arg}\', dtype=dtypes.Data(default={default_val}, size=\'s\')),'
                    )

        inputs = '\n        '.join(input_signatures)

        node_name = f'{name.title()}_Node'
        node_names.append(node_name)
        doc = obj.__doc__.replace('\0', '<NULL>') if obj.__doc__ else ''

        input_calls = ', '.join([f'self.input({i})' for i in range(len(input_signatures))])
        update_content = f'self.set_output_val(0, {mod_name}.{name}({ input_calls }))'

        node_def = f'''
class {node_name}(NodeBase):
    """
    {doc}"""
    
    title = \'{name}\'
    type_ = \'{mod_name}\'
    init_inputs = [
        {inputs}
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = \'{color}\'

    def update_event(self, inp=-1):
        {update_content}
        '''

        node_defs.append(node_def)

    node_names_tuple_str = '\n    '.join([f'{name},' for name in node_names])

    if not os.path.exists(target_path):
        os.mkdir(target_path)

    with open(target_path+'/nodes.py', 'w') as f:
        f.write('''
from ryven.NENV import *

import '''+mod_name+'''


class NodeBase(Node):
    pass

'''+'\n'.join(node_defs)+f'''


export_nodes(
    {node_names_tuple_str}
)
''')

    package = {
        'type': 'Ryven auto generated nodes package',
        'nodes': node_names
    }

    try:
        print(target_path+'/'+mod_name+'.rpc')
        os.remove(target_path+'/'+mod_name+'.rpc')
    except OSError:
        pass


if __name__ == '__main__':

    if len(sys.argv) > 1:
        mod_name = sys.argv[1]
        color = sys.argv[2]
        target_path = sys.argv[3] if len(sys.argv) > 3 else mod_name
        parse_module(mod_name, color, target_path)
    else:
        builtin_modules = find_builtin_modules()
        # sys.builtin_module_names is missing many like "random"
        for m in builtin_modules:
            parse_module(m, '#32DA22', m)

