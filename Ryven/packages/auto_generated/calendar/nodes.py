import ryvencore_qt as rc
import calendar


class AutoNode_calendar__monthlen(rc.Node):
    title = '_monthlen'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='year'),
rc.NodeInputBP(label='month'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar._monthlen(self.input(0), self.input(1)))
        


class AutoNode_calendar__nextmonth(rc.Node):
    title = '_nextmonth'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='year'),
rc.NodeInputBP(label='month'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar._nextmonth(self.input(0), self.input(1)))
        


class AutoNode_calendar__prevmonth(rc.Node):
    title = '_prevmonth'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='year'),
rc.NodeInputBP(label='month'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar._prevmonth(self.input(0), self.input(1)))
        


class AutoNode_calendar_calendar(rc.Node):
    title = 'calendar'
    description = '''
        Returns a year's calendar as a multi-line string.
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='theyear'),
rc.NodeInputBP(label='w'),
rc.NodeInputBP(label='l'),
rc.NodeInputBP(label='c'),
rc.NodeInputBP(label='m'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.calendar(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_calendar_firstweekday(rc.Node):
    title = 'firstweekday'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.firstweekday(self.input(0)))
        


class AutoNode_calendar_format(rc.Node):
    title = 'format'
    description = '''Prints multi-column formatting for year calendars'''
    init_inputs = [
        rc.NodeInputBP(label='cols'),
rc.NodeInputBP(label='colwidth'),
rc.NodeInputBP(label='spacing'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.format(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_calendar_formatstring(rc.Node):
    title = 'formatstring'
    description = '''Returns a string formatted from n strings, centered within n columns.'''
    init_inputs = [
        rc.NodeInputBP(label='cols'),
rc.NodeInputBP(label='colwidth'),
rc.NodeInputBP(label='spacing'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.formatstring(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_calendar_isleap(rc.Node):
    title = 'isleap'
    description = '''Return True for leap years, False for non-leap years.'''
    init_inputs = [
        rc.NodeInputBP(label='year'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.isleap(self.input(0)))
        


class AutoNode_calendar_leapdays(rc.Node):
    title = 'leapdays'
    description = '''Return number of leap years in range [y1, y2).
       Assume y1 <= y2.'''
    init_inputs = [
        rc.NodeInputBP(label='y1'),
rc.NodeInputBP(label='y2'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.leapdays(self.input(0), self.input(1)))
        


class AutoNode_calendar_main(rc.Node):
    title = 'main'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='args'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.main(self.input(0)))
        


class AutoNode_calendar_month(rc.Node):
    title = 'month'
    description = '''
        Return a month's calendar string (multi-line).
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='theyear'),
rc.NodeInputBP(label='themonth'),
rc.NodeInputBP(label='w'),
rc.NodeInputBP(label='l'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.month(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_calendar_monthcalendar(rc.Node):
    title = 'monthcalendar'
    description = '''
        Return a matrix representing a month's calendar.
        Each row represents a week; days outside this month are zero.
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='year'),
rc.NodeInputBP(label='month'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.monthcalendar(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_calendar_monthrange(rc.Node):
    title = 'monthrange'
    description = '''Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
       year, month.'''
    init_inputs = [
        rc.NodeInputBP(label='year'),
rc.NodeInputBP(label='month'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.monthrange(self.input(0), self.input(1)))
        


class AutoNode_calendar_prcal(rc.Node):
    title = 'prcal'
    description = '''Print a year's calendar.'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='theyear'),
rc.NodeInputBP(label='w'),
rc.NodeInputBP(label='l'),
rc.NodeInputBP(label='c'),
rc.NodeInputBP(label='m'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.prcal(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_calendar_prmonth(rc.Node):
    title = 'prmonth'
    description = '''
        Print a month's calendar.
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='theyear'),
rc.NodeInputBP(label='themonth'),
rc.NodeInputBP(label='w'),
rc.NodeInputBP(label='l'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.prmonth(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_calendar_prweek(rc.Node):
    title = 'prweek'
    description = '''
        Print a single week (no newline).
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='theweek'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.prweek(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_calendar_setfirstweekday(rc.Node):
    title = 'setfirstweekday'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='firstweekday'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.setfirstweekday(self.input(0)))
        


class AutoNode_calendar_timegm(rc.Node):
    title = 'timegm'
    description = '''Unrelated but handy function to calculate Unix timestamp from GMT.'''
    init_inputs = [
        rc.NodeInputBP(label='tuple'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.timegm(self.input(0)))
        


class AutoNode_calendar_week(rc.Node):
    title = 'week'
    description = '''
        Returns a single week in a string (no newline).
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='theweek'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.week(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_calendar_weekday(rc.Node):
    title = 'weekday'
    description = '''Return weekday (0-6 ~ Mon-Sun) for year, month (1-12), day (1-31).'''
    init_inputs = [
        rc.NodeInputBP(label='year'),
rc.NodeInputBP(label='month'),
rc.NodeInputBP(label='day'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.weekday(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_calendar_weekheader(rc.Node):
    title = 'weekheader'
    description = '''
        Return a header for a week.
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, calendar.weekheader(self.input(0), self.input(1)))
        