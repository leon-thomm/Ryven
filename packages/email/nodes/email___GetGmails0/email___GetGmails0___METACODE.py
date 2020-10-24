from NIENV import *

import imaplib
import email

# GENERAL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output

# EDITING
# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(input or index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(output or index)


# LOGGING
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...


    def update_event(self, input_called=-1):
        if input_called == 0:
            email_user = self.input(1)
            email_pass = self.input(2)

            mail = imaplib.IMAP4_SSL('imap.gmail.com')

            mail.login(email_user, email_pass)
            mail.select('INBOX') #

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


    def remove_event(self):
        pass
