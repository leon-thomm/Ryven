from NIENV import *


# API METHODS

# self.main_widget        <- access to main widget


# Ports
# self.input(index)                   <- access to input data
# set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------

import time
import Adafruit_CharLCD as LCD


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...


    def update_event(self, input_called=-1):
        if input_called == 0:
            lcd_rs = self.input(1)
            lcd_en = self.input(2)
            lcd_d4 = self.input(3)
            lcd_d5 = self.input(4)
            lcd_d6 = self.input(5)
            lcd_d7 = self.input(6)
            lcd_backlight = self.input(7)
            message = str(self.input(8))

            lcd_columns = 16
            lcd_rows = 2

            lcd = LCD.Adafruit_CharLCD(lcd_rs,
                                       lcd_en,
                                       lcd_d4,
                                       lcd_d5,
                                       lcd_d6,
                                       lcd_d7,
                                       lcd_columns,
                                       lcd_rows,
                                       lcd_backlight)

            lcd.message(message)

            self.exec_output(0)


    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...


    def remove_event(self):
        pass
