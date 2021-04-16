import ryvencore_qt as rc
import html


class AutoNode_html__replace_charref(rc.Node):
    title = '_replace_charref'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, html._replace_charref(self.input(0)))
        


class AutoNode_html_escape(rc.Node):
    title = 'escape'
    doc = '''
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true (the default), the quotation mark
    characters, both double quote (") and single quote (') characters are also
    translated.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='quote'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, html.escape(self.input(0), self.input(1)))
        


class AutoNode_html_unescape(rc.Node):
    title = 'unescape'
    doc = '''
    Convert all named and numeric character references (e.g. &gt;, &#62;,
    &x3e;) in the string s to the corresponding unicode characters.
    This function uses the rules defined by the HTML 5 standard
    for both valid and invalid character references, and the list of
    HTML 5 named character references defined in html.entities.html5.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, html.unescape(self.input(0)))
        