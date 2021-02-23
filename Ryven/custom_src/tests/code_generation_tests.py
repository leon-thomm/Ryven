import inspect
import sys

import pkg_resources
import ast
import stdlib_list


class CodeGenerator:

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



if __name__ == '__main__':
    installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]
    installed_package_names = [p[0] for p in installed_packages]

    # builtin_modules = list(sys.builtin_module_names)
    sys.path.append('C:/Users/nutri/OneDrive - ETH Zurich/projects/ryvencore/testing/')
    node_mod = __import__('open_cv_nodes', fromlist=['Node'])
    Node = getattr(node_mod, 'Node')

    objects = [
        Node()
    ]
    source = ''
    # print(installed_packages)
    for o in objects:
        imports, s = CodeGenerator.get_module_source(
            inspect.getmodule(o), ['B'], installed_package_names, stdlib_list.stdlib_list()
        )
        for i in imports:
            source += '\n'+i
        source += '\n\n\n'+s

    print(source)
