
from NENV import *

import calendar


class NodeBase(Node):
    pass


class _Monthlen_Node(NodeBase):
    title = '_monthlen'
    type_ = 'calendar'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar._monthlen(self.input(0), self.input(1)))
        

class _Nextmonth_Node(NodeBase):
    title = '_nextmonth'
    type_ = 'calendar'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar._nextmonth(self.input(0), self.input(1)))
        

class _Prevmonth_Node(NodeBase):
    title = '_prevmonth'
    type_ = 'calendar'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar._prevmonth(self.input(0), self.input(1)))
        

class Calendar_Node(NodeBase):
    title = 'calendar'
    type_ = 'calendar'
    doc = """
        Returns a year's calendar as a multi-line string.
        """
    init_inputs = [
        NodeInputBP(label='theyear'),
        NodeInputBP(label='w', dtype=dtypes.Data(default=2, size='s')),
        NodeInputBP(label='l', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='c', dtype=dtypes.Data(default=6, size='s')),
        NodeInputBP(label='m', dtype=dtypes.Data(default=3, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.calendar(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Firstweekday_Node(NodeBase):
    title = 'firstweekday'
    type_ = 'calendar'
    doc = """"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.firstweekday())
        

class Format_Node(NodeBase):
    title = 'format'
    type_ = 'calendar'
    doc = """Prints multi-column formatting for year calendars"""
    init_inputs = [
        NodeInputBP(label='cols'),
        NodeInputBP(label='colwidth', dtype=dtypes.Data(default=20, size='s')),
        NodeInputBP(label='spacing', dtype=dtypes.Data(default=6, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.format(self.input(0), self.input(1), self.input(2)))
        

class Formatstring_Node(NodeBase):
    title = 'formatstring'
    type_ = 'calendar'
    doc = """Returns a string formatted from n strings, centered within n columns."""
    init_inputs = [
        NodeInputBP(label='cols'),
        NodeInputBP(label='colwidth', dtype=dtypes.Data(default=20, size='s')),
        NodeInputBP(label='spacing', dtype=dtypes.Data(default=6, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.formatstring(self.input(0), self.input(1), self.input(2)))
        

class Isleap_Node(NodeBase):
    title = 'isleap'
    type_ = 'calendar'
    doc = """Return True for leap years, False for non-leap years."""
    init_inputs = [
        NodeInputBP(label='year'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.isleap(self.input(0)))
        

class Leapdays_Node(NodeBase):
    title = 'leapdays'
    type_ = 'calendar'
    doc = """Return number of leap years in range [y1, y2).
       Assume y1 <= y2."""
    init_inputs = [
        NodeInputBP(label='y1'),
        NodeInputBP(label='y2'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.leapdays(self.input(0), self.input(1)))
        

class Main_Node(NodeBase):
    title = 'main'
    type_ = 'calendar'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.main(self.input(0)))
        

class Month_Node(NodeBase):
    title = 'month'
    type_ = 'calendar'
    doc = """
        Return a month's calendar string (multi-line).
        """
    init_inputs = [
        NodeInputBP(label='theyear'),
        NodeInputBP(label='themonth'),
        NodeInputBP(label='w', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='l', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.month(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Monthcalendar_Node(NodeBase):
    title = 'monthcalendar'
    type_ = 'calendar'
    doc = """
        Return a matrix representing a month's calendar.
        Each row represents a week; days outside this month are zero.
        """
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.monthcalendar(self.input(0), self.input(1)))
        

class Monthrange_Node(NodeBase):
    title = 'monthrange'
    type_ = 'calendar'
    doc = """Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
       year, month."""
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.monthrange(self.input(0), self.input(1)))
        

class Prcal_Node(NodeBase):
    title = 'prcal'
    type_ = 'calendar'
    doc = """Print a year's calendar."""
    init_inputs = [
        NodeInputBP(label='theyear'),
        NodeInputBP(label='w', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='l', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='c', dtype=dtypes.Data(default=6, size='s')),
        NodeInputBP(label='m', dtype=dtypes.Data(default=3, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.prcal(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Prmonth_Node(NodeBase):
    title = 'prmonth'
    type_ = 'calendar'
    doc = """
        Print a month's calendar.
        """
    init_inputs = [
        NodeInputBP(label='theyear'),
        NodeInputBP(label='themonth'),
        NodeInputBP(label='w', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='l', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.prmonth(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Prweek_Node(NodeBase):
    title = 'prweek'
    type_ = 'calendar'
    doc = """
        Print a single week (no newline).
        """
    init_inputs = [
        NodeInputBP(label='theweek'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.prweek(self.input(0), self.input(1)))
        

class Setfirstweekday_Node(NodeBase):
    title = 'setfirstweekday'
    type_ = 'calendar'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='firstweekday'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.setfirstweekday(self.input(0)))
        

class Timegm_Node(NodeBase):
    title = 'timegm'
    type_ = 'calendar'
    doc = """Unrelated but handy function to calculate Unix timestamp from GMT."""
    init_inputs = [
        NodeInputBP(label='tuple'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.timegm(self.input(0)))
        

class Week_Node(NodeBase):
    title = 'week'
    type_ = 'calendar'
    doc = """
        Returns a single week in a string (no newline).
        """
    init_inputs = [
        NodeInputBP(label='theweek'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.week(self.input(0), self.input(1)))
        

class Weekday_Node(NodeBase):
    title = 'weekday'
    type_ = 'calendar'
    doc = """Return weekday (0-6 ~ Mon-Sun) for year, month (1-12), day (1-31)."""
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
        NodeInputBP(label='day'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.weekday(self.input(0), self.input(1), self.input(2)))
        

class Weekheader_Node(NodeBase):
    title = 'weekheader'
    type_ = 'calendar'
    doc = """
        Return a header for a week.
        """
    init_inputs = [
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.weekheader(self.input(0)))
        


export_nodes(
    _Monthlen_Node,
    _Nextmonth_Node,
    _Prevmonth_Node,
    Calendar_Node,
    Firstweekday_Node,
    Format_Node,
    Formatstring_Node,
    Isleap_Node,
    Leapdays_Node,
    Main_Node,
    Month_Node,
    Monthcalendar_Node,
    Monthrange_Node,
    Prcal_Node,
    Prmonth_Node,
    Prweek_Node,
    Setfirstweekday_Node,
    Timegm_Node,
    Week_Node,
    Weekday_Node,
    Weekheader_Node,
)
