import json
import os


class PackageTranslator:
    """The PackageTranslator creates working modules out of the metacode files."""

    def __init__(self, package_dir):
        self.module_name_separator = '___'

        self.package_name = os.path.basename(package_dir)

        f = open(package_dir+'/'+self.package_name+'.rpc', 'r')
        package_config = json.loads(f.read())
        f.close()


        # translate nodes
        for n in package_config['nodes']:

            # SRC CODE
            f = open(package_dir+'/nodes/'+n['module name']+'/'+n['module name']+self.module_name_separator+'METACODE.py', 'r')
            code = f.read()
            f.close()
            src_code_target_filename = n['module name']+'.py'

            code = code.replace('%NODE_TITLE%', n['class name'])
            code = code.replace('%CLASS%', n['class name']+'_NodeInstance')
            code = code.replace('%PACKAGE_NAME%', self.package_name)

            self.save(package_dir+'/nodes/'+n['module name']+'/'+src_code_target_filename, code)


            # MAIN WIDGET
            if n['has main widget']:
                f = open(package_dir + '/nodes/' + n['module name'] + '/widgets/' + n['module name'] +
                         self.module_name_separator + 'main_widget' +
                         self.module_name_separator + 'METACODE.py', 'r')
                code = f.read()
                f.close()
                main_widget_target_filename = n['module name'] + self.module_name_separator + 'main_widget.py'

                code = code.replace('%NODE_TITLE%', n['class name'])
                code = code.replace('%CLASS%', n['class name']+'_NodeInstance_MainWidget')

                self.save(package_dir + '/nodes/' + n['module name'] + '/widgets/' + main_widget_target_filename, code)


            # INPUT WIDGETS
            for i_w in n['custom input widgets']:
                f = open(package_dir + '/nodes/' + n['module name'] + '/widgets/' + n['module name'] +
                         self.module_name_separator + i_w +
                         self.module_name_separator + 'METACODE.py', 'r')
                code = f.read()
                f.close()
                input_widget_target_filename = n['module name'] + self.module_name_separator + i_w + '.py'

                code = code.replace('%INPUT_WIDGET_TITLE%', i_w)  # i_w is already class name legal
                code = code.replace('%CLASS%', i_w+'_PortInstanceWidget')

                self.save(package_dir + '/nodes/' + n['module name'] + '/widgets/' + input_widget_target_filename, code)


    def save(self, target_file_path, code):
        """Saves the working Python module"""

        try:
            os.remove(target_file_path)
        except OSError:
            pass

        f = open(target_file_path, 'w')
        f.write(code)
        f.close()
