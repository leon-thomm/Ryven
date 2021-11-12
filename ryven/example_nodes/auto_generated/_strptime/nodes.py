
from ryven.NENV import *

import _strptime


class NodeBase(Node):
    pass


class _Calc_Julian_From_U_Or_W_Node(NodeBase):
    """
    Calculate the Julian day based on the year, week of the year, and day of
    the week, with week_start_day representing whether the week of the year
    assumes the week starts on Sunday or Monday (6 or 0)."""
    
    title = '_calc_julian_from_U_or_W'
    type_ = '_strptime'
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='week_of_year'),
        NodeInputBP(label='day_of_week'),
        NodeInputBP(label='week_starts_Mon'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _strptime._calc_julian_from_U_or_W(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Calc_Julian_From_V_Node(NodeBase):
    """
    Calculate the Julian day based on the ISO 8601 year, week, and weekday.
    ISO weeks start on Mondays, with week 01 being the week containing 4 Jan.
    ISO week days range from 1 (Monday) to 7 (Sunday).
    """
    
    title = '_calc_julian_from_V'
    type_ = '_strptime'
    init_inputs = [
        NodeInputBP(label='iso_year'),
        NodeInputBP(label='iso_week'),
        NodeInputBP(label='iso_weekday'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _strptime._calc_julian_from_V(self.input(0), self.input(1), self.input(2)))
        

class _Getlang_Node(NodeBase):
    """
    """
    
    title = '_getlang'
    type_ = '_strptime'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _strptime._getlang())
        

class _Strptime_Node(NodeBase):
    """
    Return a 2-tuple consisting of a time struct and an int containing
    the number of microseconds based on the input string and the
    format string."""
    
    title = '_strptime'
    type_ = '_strptime'
    init_inputs = [
        NodeInputBP(label='data_string'),
        NodeInputBP(label='format', dtype=dtypes.Data(default='%a %b %d %H:%M:%S %Y', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _strptime._strptime(self.input(0), self.input(1)))
        

class _Strptime_Datetime_Node(NodeBase):
    """
    Return a class cls instance based on the input string and the
    format string."""
    
    title = '_strptime_datetime'
    type_ = '_strptime'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='data_string'),
        NodeInputBP(label='format', dtype=dtypes.Data(default='%a %b %d %H:%M:%S %Y', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _strptime._strptime_datetime(self.input(0), self.input(1), self.input(2)))
        

class _Strptime_Time_Node(NodeBase):
    """
    Return a time struct based on the input string and the
    format string."""
    
    title = '_strptime_time'
    type_ = '_strptime'
    init_inputs = [
        NodeInputBP(label='data_string'),
        NodeInputBP(label='format', dtype=dtypes.Data(default='%a %b %d %H:%M:%S %Y', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _strptime._strptime_time(self.input(0), self.input(1)))
        

class Re_Compile_Node(NodeBase):
    """
    Compile a regular expression pattern, returning a Pattern object."""
    
    title = 're_compile'
    type_ = '_strptime'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _strptime.re_compile(self.input(0), self.input(1)))
        

class Re_Escape_Node(NodeBase):
    """
    
    Escape special characters in a string.
    """
    
    title = 're_escape'
    type_ = '_strptime'
    init_inputs = [
        NodeInputBP(label='pattern'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _strptime.re_escape(self.input(0)))
        


export_nodes(
    _Calc_Julian_From_U_Or_W_Node,
    _Calc_Julian_From_V_Node,
    _Getlang_Node,
    _Strptime_Node,
    _Strptime_Datetime_Node,
    _Strptime_Time_Node,
    Re_Compile_Node,
    Re_Escape_Node,
)
