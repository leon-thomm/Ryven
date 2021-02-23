import inspect
import ast
import autopep8
import pkg_resources
import stdlib_list

from ..code_gen.CodeGenDialog import CodeGenDialog


class CodeGenerator:
    """In production and *very* experimental."""


    def __init__(self, script):
        self.nodes = script.flow.nodes
        self.vars_manager_config = script.vars_manager.config_data()
        self.flow_algorithm_mode = script.flow.algorithm_mode()


    @staticmethod
    def get_module_source(module, exclude_imports: list, installed_package_names: list,
                          builtin_modules: list) -> tuple:
        """Parses a complete module recursively and returns a list of import statements and a source code
        including everything that wasn't an excluded import or an import of an installed package."""

        imports = []
        sources = []

        mod_ast = ast.parse(inspect.getsource(module))

        # iterate over every first order statement
        for b in mod_ast.body:

            if type(b) != ast.Import and type(b) != ast.ImportFrom:
                sources.append(ast.unparse(b))
                continue

            # PROCESS IMPORT

            if type(b) == ast.Import:
                imported_module_name = b.names[0].name
            else:
                imported_module_name = b.module

            if imported_module_name in exclude_imports:
                pass  # ignore excluded

            elif imported_module_name in installed_package_names or imported_module_name in builtin_modules:
                imports.append(ast.unparse(b))  # keep imports of installed packages

            else:
                # parse and add source of custom imported module

                # imported_mod = CodeGenerator._get_module_from_import(imported_module_name, module)

                new_imports, new_source = CodeGenerator.get_module_source(
                    module=__import__(imported_module_name),
                    exclude_imports=exclude_imports,
                    installed_package_names=installed_package_names,
                    builtin_modules=builtin_modules
                )
                imports.extend(new_imports)
                sources.append(new_source)

        return imports, '\n\n\n'.join(sources)


    def generate(self, ignored_imports: list) -> str:

        code = ''

        code += 10*'\n' + self.get_base_classes_code()

        # ------------------------------------------

        # NODES
        installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]
        installed_package_names = [p[0] for p in installed_packages]

        node_modules = set([inspect.getmodule(node) for node in self.nodes])
        imports = []
        sources = []
        for module in node_modules:
            imports_, src = self.get_module_source(
                module=module,
                exclude_imports=ignored_imports,
                installed_package_names=installed_package_names,
                builtin_modules=stdlib_list.stdlib_list()
            )
            imports.extend(imports_)
            sources.append(src)


        code += '\n'.join(imports)
        code += (4*'\n').join(sources)

        # ------------------------------------------

        code += 5*'\n'+self.create_script_code()

        code = autopep8.fix_code(code)

        return code


    def get_base_classes_code(self):
        f = open('custom_src/code_gen/DefaultCode.py')
        code = f.read()
        f.close()
        return code


    def create_script_code(self):

        nodes_decl_list = [f'{n.__class__.__name__}(\n    ' \
                           f'{n.config_data(include_data_inp_values=True)}\n' \
                           '),'.replace('\n', '\n    ') for n in self.nodes]

        nodes_decl = '\n        '.join(nodes_decl_list)

        connections = []
        for i in range(len(self.nodes)):
            n = self.nodes[i]
            for o in range(len(n.outputs)):
                for c in n.outputs[o].connections:
                    c_p = c.inp
                    c_n = c_p.node
                    connections.append(f'c({i}, {o}, {self.nodes.index(c_n)}, {c_n.inputs.index(c_p)})')

        connections_decl = '\n    '.join(connections)

        code = \
f'''
def create_nodes():
    nodes = [
        {nodes_decl}
    ]
    return nodes


def connect_nodes():
    def c(i1, o, i2, i):
        out = nodes[i1].outputs[o]
        inp = nodes[i2].inputs[i]
        if isinstance(out, DataOutputPort):
            c = DataConnection(out, inp)
        else:
            c = ExecConnection(out, inp)
        out.connections.append(c)
        inp.connections.append(c)
    
    {connections_decl}

def init_vars():
    manager = VarsManager(config={self.vars_manager_config})
    return manager

if __name__ == '__main__':
    flow_alg = {'FlowAlg.DATA' if self.flow_algorithm_mode == 'data' else 'FlowAlg.EXEC'}
    vars_manager = init_vars()
    nodes = create_nodes()
    connect_nodes()
    for n in nodes:
        n.update()

    # ...
'''

        return code


# SOME AST REFERENCE
#
# ast.dump(ast.parse('''
# import numpy as np
# import pyside2
# from scipy import linalg
# from opencv import *
# '''))
# Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pyside2')]),
#              ImportFrom(module='scipy', names=[alias(name='linalg')], level=0),
#              ImportFrom(module='opencv', names=[alias(name='*')], level=0)], type_ignores=[])
