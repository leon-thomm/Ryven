
from ryven.NENV import *

import calendar


class NodeBase(Node):
    pass


class _Monthlen_Node(NodeBase):
    """
    """
    
    title = '_monthlen'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar._monthlen(self.input(0), self.input(1)))
        

class _Nextmonth_Node(NodeBase):
    """
    """
    
    title = '_nextmonth'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar._nextmonth(self.input(0), self.input(1)))
        

class _Prevmonth_Node(NodeBase):
    """
    """
    
    title = '_prevmonth'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar._prevmonth(self.input(0), self.input(1)))
        

class Calendar_Node(NodeBase):
    """
    
        Returns a year's calendar as a multi-line string.
        """
    
    title = 'calendar'
    type_ = 'calendar'
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

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.calendar(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Firstweekday_Node(NodeBase):
    """
    """
    
    title = 'firstweekday'
    type_ = 'calendar'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.firstweekday())
        

class Format_Node(NodeBase):
    """
    Prints multi-column formatting for year calendars"""
    
    title = 'format'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='cols'),
        NodeInputBP(label='colwidth', dtype=dtypes.Data(default=20, size='s')),
        NodeInputBP(label='spacing', dtype=dtypes.Data(default=6, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.format(self.input(0), self.input(1), self.input(2)))
        

class Formatstring_Node(NodeBase):
    """
    Returns a string formatted from n strings, centered within n columns."""
    
    title = 'formatstring'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='cols'),
        NodeInputBP(label='colwidth', dtype=dtypes.Data(default=20, size='s')),
        NodeInputBP(label='spacing', dtype=dtypes.Data(default=6, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.formatstring(self.input(0), self.input(1), self.input(2)))
        

class Isleap_Node(NodeBase):
    """
    Return True for leap years, False for non-leap years."""
    
    title = 'isleap'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='year'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.isleap(self.input(0)))
        

class Leapdays_Node(NodeBase):
    """
    Return number of leap years in range [y1, y2).
       Assume y1 <= y2."""
    
    title = 'leapdays'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='y1'),
        NodeInputBP(label='y2'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.leapdays(self.input(0), self.input(1)))
        

class Main_Node(NodeBase):
    """
    """
    
    title = 'main'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.main(self.input(0)))
        

class Month_Node(NodeBase):
    """
    
        Return a month's calendar string (multi-line).
        """
    
    title = 'month'
    type_ = 'calendar'
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

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.month(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Monthcalendar_Node(NodeBase):
    """
    
        Return a matrix representing a month's calendar.
        Each row represents a week; days outside this month are zero.
        """
    
    title = 'monthcalendar'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.monthcalendar(self.input(0), self.input(1)))
        

class Monthrange_Node(NodeBase):
    """
    Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
       year, month."""
    
    title = 'monthrange'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.monthrange(self.input(0), self.input(1)))
        

class Prcal_Node(NodeBase):
    """
    Print a year's calendar."""
    
    title = 'prcal'
    type_ = 'calendar'
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

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.prcal(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Prmonth_Node(NodeBase):
    """
    
        Print a month's calendar.
        """
    
    title = 'prmonth'
    type_ = 'calendar'
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

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.prmonth(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Prweek_Node(NodeBase):
    """
    
        Print a single week (no newline).
        """
    
    title = 'prweek'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='theweek'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.prweek(self.input(0), self.input(1)))
        

class Setfirstweekday_Node(NodeBase):
    """
    """
    
    title = 'setfirstweekday'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='firstweekday'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.setfirstweekday(self.input(0)))
        

class Timegm_Node(NodeBase):
    """
    Unrelated but handy function to calculate Unix timestamp from GMT."""
    
    title = 'timegm'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='tuple'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.timegm(self.input(0)))
        

class Week_Node(NodeBase):
    """
    
        Returns a single week in a string (no newline).
        """
    
    title = 'week'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='theweek'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.week(self.input(0), self.input(1)))
        

class Weekday_Node(NodeBase):
    """
    Return weekday (0-6 ~ Mon-Sun) for year, month (1-12), day (1-31)."""
    
    title = 'weekday'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='year'),
        NodeInputBP(label='month'),
        NodeInputBP(label='day'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, calendar.weekday(self.input(0), self.input(1), self.input(2)))
        

class Weekheader_Node(NodeBase):
    """
    
        Return a header for a week.
        """
    
    title = 'weekheader'
    type_ = 'calendar'
    init_inputs = [
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
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
