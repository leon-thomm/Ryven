from NIENV import *


# API METHODS

# self.main_widget        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# ------------------------------------------------------------------------------
import numpy as np


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['hide preview'] = {'method': M(self.action_hide_mw)}
        self.main_widget_hidden = False
        self.accessed_columns = []
        self.accessed_rows = []

    def update_event(self, input_called=-1):
        matrix = self.input(0)
        self.main_widget.update_matrix(matrix)
        self.set_output_val(0, matrix)

        # also update individual access outputs for rows and columns

        i = 1
        for r in sorted(self.accessed_rows):
            self.set_output_val(i, matrix[r])
            i+=1
        for c in sorted(self.accessed_columns):
            self.set_output_val(i, np.transpose(matrix[:,c][np.newaxis]))
            i+=1

        # update context menu

        if len(matrix) > 0:
            rows_access = {}
            context_rows = set([j for j in range(matrix.shape[0])]) - set(self.accessed_rows)
            for i in context_rows:    # only show row access options for those wo are not used yet
                rows_access['access row '+str(i)] = {'method': M(self.add_row_access),
                                                      'data': i}
            self.special_actions['add row access'] = rows_access
        elif self.special_actions.__contains__('add row access'):
            del self.special_actions['add row access']
        
        if len(matrix.shape) > 1:
            columns_access = {}
            context_columns = set([j for j in range(matrix.shape[1])]) - set(self.accessed_columns)
            for i in context_columns:    # # only show column access options for those wo are not used yet
                columns_access['access column '+str(i)] = {'method': M(self.add_column_access),
                                                           'data': i}
            self.special_actions['add col access'] = columns_access
        elif self.special_actions.__contains__('add col access'):
            del self.special_actions['add col access']


    def add_row_access(self, data):
        row_index = data
        self.accessed_rows.append(row_index)
        self.create_new_output('data', 'row '+str(row_index), pos=sorted(self.accessed_rows).index(row_index)+1)
        
        remove_actions = self.special_actions['remove output'] if self.special_actions.__contains__('remove output') else {}
        remove_actions['row '+str(row_index)] = {'method': M(self.remove_row_access),
                                                 'data': row_index}
        self.special_actions['remove output'] = remove_actions

    def add_column_access(self, data):
        col_index = data
        self.accessed_columns.append(col_index)
        self.create_new_output('data', 'col '+str(col_index), pos=1+len(self.accessed_rows)+sorted(self.accessed_columns).index(col_index))
        
        remove_actions = self.special_actions['remove output'] if self.special_actions.__contains__('remove output') else {}
        remove_actions['col '+str(col_index)] = {'method': M(self.remove_col_access),
                                                 'data': col_index}
        self.special_actions['remove output'] = remove_actions

    def remove_row_access(self, data):
        row_index = data
        self.delete_output(1+sorted(self.accessed_rows).index(row_index))
        self.accessed_rows.remove(row_index)
        del self.special_actions['remove output']['row '+str(row_index)]

    def remove_col_access(self, data):
        col_index = data
        self.delete_output(1+len(self.accessed_rows)+sorted(self.accessed_columns).index(col_index))
        self.accessed_columns.remove(col_index)
        del self.special_actions['remove output']['col '+str(col_index)]

    def action_hide_mw(self):
        self.main_widget.hide()
        del self.special_actions['hide preview']
        self.special_actions['show preview'] = {'method': M(self.action_show_mw)}
        self.main_widget_hidden = True
        self.update_shape()

    def action_show_mw(self):
        self.main_widget.show()
        del self.special_actions['show preview']
        self.special_actions['hide preview'] = {'method': M(self.action_hide_mw)}
        self.main_widget_hidden = False
        self.update_shape()

    def get_data(self):
        data = {'main widget hidden': self.main_widget_hidden,
                'accessed rows': self.accessed_rows,
                'accessed columns': self.accessed_columns}
        return data

    def set_data(self, data):
        self.main_widget_hidden = data['main widget hidden']
        # if self.main_widget_hidden:
        #     self.action_hide_mw()
        # shown by default
        
        self.accessed_rows = data['accessed rows']
        self.accessed_columns = data['accessed columns']

    def removing(self):
        pass
