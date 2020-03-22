from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import imaplib
import os
import email

# GENERAL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output

# EDITING
# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True, pos=-1)
# self.delete_output(output or index)
# self.update_shape()                  <- recomputes the whole shape and content positions

# LOGGING
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')


class GetGmails_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(GetGmails_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        # ...

        if configuration:
            self.set_data(configuration['state data'])


    def updating(self, token, input_called=-1):
        if input_called == 0:
            email_user = self.input(1)
            email_pass = self.input(2)

            mail = imaplib.IMAP4_SSL('imap.gmail.com')

            mail.login(email_user, email_pass)
            mail.select('INPBOX') #

            # new_filenames = []
            dates = []
            # new_file_payloads = []
            subjects = []
            # new_froms = []
            messages = []
            mail.select()

            t, data = mail.search(None, 'ALL')
            mail_ids = data[0]
            id_list = mail_ids.split()

            for num in data[0].split():
                t, data = mail.fetch(num, '(RFC822)' )
                raw_email = data[0][1]
                raw_email_string = raw_email.decode('ISO-8859-1')
                email_message = email.message_from_string(raw_email_string)

                dates.append(email_message['date'])
                subjects.append(email_message['Subject'])
                messages.append(self.get_body(email_message))


            mail.close()
            self.set_output_val(1, subjects)
            self.set_output_val(2, dates)
            self.set_output_val(3, messages)
            self.exec_output(0)

    def get_body(self, msg):
        if msg.is_multipart():
            return self.get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None, True)


    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
