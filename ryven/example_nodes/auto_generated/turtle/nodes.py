
from ryven.NENV import *

import turtle


class NodeBase(Node):
    pass


class Screen_Node(NodeBase):
    """
    Return the singleton screen object.
    If none exists at the moment, create a new one and return it,
    else return the existing one."""
    
    title = 'Screen'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.Screen())
        

class __Forwardmethods_Node(NodeBase):
    """
    """
    
    title = '__forwardmethods'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='fromClass'),
        NodeInputBP(label='toClass'),
        NodeInputBP(label='toPart'),
        NodeInputBP(label='exclude', dtype=dtypes.Data(default=(), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.__forwardmethods(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class __Methoddict_Node(NodeBase):
    """
    helper function for Scrolled Canvas"""
    
    title = '__methodDict'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.__methodDict(self.input(0)))
        

class __Methods_Node(NodeBase):
    """
    helper function for Scrolled Canvas"""
    
    title = '__methods'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.__methods(self.input(0)))
        

class _Make_Global_Funcs_Node(NodeBase):
    """
    """
    
    title = '_make_global_funcs'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='functions'),
        NodeInputBP(label='cls'),
        NodeInputBP(label='obj'),
        NodeInputBP(label='init'),
        NodeInputBP(label='docrevise'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle._make_global_funcs(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Screen_Docrevise_Node(NodeBase):
    """
    To reduce docstrings from TurtleScreen class for functions
    """
    
    title = '_screen_docrevise'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='docstr'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle._screen_docrevise(self.input(0)))
        

class _Turtle_Docrevise_Node(NodeBase):
    """
    To reduce docstrings from RawTurtle class for functions
    """
    
    title = '_turtle_docrevise'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='docstr'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle._turtle_docrevise(self.input(0)))
        

class Addshape_Node(NodeBase):
    """
    Adds a turtle shape to TurtleScreen's shapelist.

        Arguments:
        (1) name is the name of a gif-file and shape is None.
            Installs the corresponding image shape.
            !! Image-shapes DO NOT rotate when turning the turtle,
            !! so they do not display the heading of the turtle!
        (2) name is an arbitrary string and shape is a tuple
            of pairs of coordinates. Installs the corresponding
            polygon shape
        (3) name is an arbitrary string and shape is a
            (compound) Shape object. Installs the corresponding
            compound shape.
        To use a shape, you have to issue the command shape(shapename).

        call: register_shape("turtle.gif")
        --or: register_shape("tri", ((0,0), (10,10), (-10,10)))

        Example:
        >>> register_shape("triangle", ((5,-3),(0,5),(-5,-3)))

        """
    
    title = 'addshape'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='shape', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.addshape(self.input(0), self.input(1)))
        

class Back_Node(NodeBase):
    """
    Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance, opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example:
        >>> position()
        (0.00, 0.00)
        >>> backward(30)
        >>> position()
        (-30.00, 0.00)
        """
    
    title = 'back'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='distance'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.back(self.input(0)))
        

class Backward_Node(NodeBase):
    """
    Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance, opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example:
        >>> position()
        (0.00, 0.00)
        >>> backward(30)
        >>> position()
        (-30.00, 0.00)
        """
    
    title = 'backward'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='distance'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.backward(self.input(0)))
        

class Begin_Fill_Node(NodeBase):
    """
    Called just before drawing a shape to be filled.

        No argument.

        Example:
        >>> color("black", "red")
        >>> begin_fill()
        >>> circle(60)
        >>> end_fill()
        """
    
    title = 'begin_fill'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.begin_fill())
        

class Begin_Poly_Node(NodeBase):
    """
    Start recording the vertices of a polygon.

        No argument.

        Start recording the vertices of a polygon. Current turtle position
        is first point of polygon.

        Example:
        >>> begin_poly()
        """
    
    title = 'begin_poly'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.begin_poly())
        

class Bgcolor_Node(NodeBase):
    """
    Set or return backgroundcolor of the TurtleScreen.

        Arguments (if given): a color string or three numbers
        in the range 0..colormode or a 3-tuple of such numbers.

        Example:
        >>> bgcolor("orange")
        >>> bgcolor()
        'orange'
        >>> bgcolor(0.5,0,0.5)
        >>> bgcolor()
        '#800080'
        """
    
    title = 'bgcolor'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.bgcolor())
        

class Bgpic_Node(NodeBase):
    """
    Set background image or return name of current backgroundimage.

        Optional argument:
        picname -- a string, name of a gif-file or "nopic".

        If picname is a filename, set the corresponding image as background.
        If picname is "nopic", delete backgroundimage, if present.
        If picname is None, return the filename of the current backgroundimage.

        Example:
        >>> bgpic()
        'nopic'
        >>> bgpic("landscape.gif")
        >>> bgpic()
        'landscape.gif'
        """
    
    title = 'bgpic'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='picname', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.bgpic(self.input(0)))
        

class Bk_Node(NodeBase):
    """
    Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance, opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example:
        >>> position()
        (0.00, 0.00)
        >>> backward(30)
        >>> position()
        (-30.00, 0.00)
        """
    
    title = 'bk'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='distance'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.bk(self.input(0)))
        

class Bye_Node(NodeBase):
    """
    Shut the turtlegraphics window.

        Example:
        >>> bye()
        """
    
    title = 'bye'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.bye())
        

class Circle_Node(NodeBase):
    """
     Draw a circle with given radius.

        Arguments:
        radius -- a number
        extent (optional) -- a number
        steps (optional) -- an integer

        Draw a circle with given radius. The center is radius units left
        of the turtle; extent - an angle - determines which part of the
        circle is drawn. If extent is not given, draw the entire circle.
        If extent is not a full circle, one endpoint of the arc is the
        current pen position. Draw the arc in counterclockwise direction
        if radius is positive, otherwise in clockwise direction. Finally
        the direction of the turtle is changed by the amount of extent.

        As the circle is approximated by an inscribed regular polygon,
        steps determines the number of steps to use. If not given,
        it will be calculated automatically. Maybe used to draw regular
        polygons.

        call: circle(radius)                  # full circle
        --or: circle(radius, extent)          # arc
        --or: circle(radius, extent, steps)
        --or: circle(radius, steps=6)         # 6-sided polygon

        Example:
        >>> circle(50)
        >>> circle(120, 180)  # semicircle
        """
    
    title = 'circle'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='radius'),
        NodeInputBP(label='extent', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='steps', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.circle(self.input(0), self.input(1), self.input(2)))
        

class Clear_Node(NodeBase):
    """
    Delete the turtle's drawings from the screen. Do not move 

        No arguments.

        Delete the turtle's drawings from the screen. Do not move 
        State and position of the turtle as well as drawings of other
        turtles are not affected.

        Examples:
        >>> clear()
        """
    
    title = 'clear'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.clear())
        

class Clearscreen_Node(NodeBase):
    """
    Delete all drawings and all turtles from the TurtleScreen.

        No argument.

        Reset empty TurtleScreen to its initial state: white background,
        no backgroundimage, no eventbindings and tracing on.

        Example:
        >>> clear()

        Note: this method is not available as function.
        """
    
    title = 'clearscreen'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.clearscreen())
        

class Clearstamp_Node(NodeBase):
    """
    Delete stamp with given stampid

        Argument:
        stampid - an integer, must be return value of previous stamp() call.

        Example:
        >>> color("blue")
        >>> astamp = stamp()
        >>> fd(50)
        >>> clearstamp(astamp)
        """
    
    title = 'clearstamp'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='stampid'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.clearstamp(self.input(0)))
        

class Clearstamps_Node(NodeBase):
    """
    Delete all or first/last n of turtle's stamps.

        Optional argument:
        n -- an integer

        If n is None, delete all of pen's stamps,
        else if n > 0 delete first n stamps
        else if n < 0 delete last n stamps.

        Example:
        >>> for i in range(8):
        ...     stamp(); fd(30)
        ...
        >>> clearstamps(2)
        >>> clearstamps(-2)
        >>> clearstamps()
        """
    
    title = 'clearstamps'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='n', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.clearstamps(self.input(0)))
        

class Clone_Node(NodeBase):
    """
    Create and return a clone of the 

        No argument.

        Create and return a clone of the turtle with same position, heading
        and turtle properties.

        Example (for a Turtle instance named mick):
        mick = Turtle()
        joe = mick.clone()
        """
    
    title = 'clone'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.clone())
        

class Color_Node(NodeBase):
    """
    Return or set the pencolor and fillcolor.

        Arguments:
        Several input formats are allowed.
        They use 0, 1, 2, or 3 arguments as follows:

        color()
            Return the current pencolor and the current fillcolor
            as a pair of color specification strings as are returned
            by pencolor and fillcolor.
        color(colorstring), color((r,g,b)), color(r,g,b)
            inputs as in pencolor, set both, fillcolor and pencolor,
            to the given value.
        color(colorstring1, colorstring2),
        color((r1,g1,b1), (r2,g2,b2))
            equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
            and analogously, if the other input format is used.

        If turtleshape is a polygon, outline and interior of that polygon
        is drawn with the newly set colors.
        For more info see: pencolor, fillcolor

        Example:
        >>> color('red', 'green')
        >>> color()
        ('red', 'green')
        >>> colormode(255)
        >>> color((40, 80, 120), (160, 200, 240))
        >>> color()
        ('#285078', '#a0c8f0')
        """
    
    title = 'color'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.color())
        

class Colormode_Node(NodeBase):
    """
    Return the colormode or set it to 1.0 or 255.

        Optional argument:
        cmode -- one of the values 1.0 or 255

        r, g, b values of colortriples have to be in range 0..cmode.

        Example:
        >>> colormode()
        1.0
        >>> colormode(255)
        >>> pencolor(240,160,80)
        """
    
    title = 'colormode'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='cmode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.colormode(self.input(0)))
        

class Config_Dict_Node(NodeBase):
    """
    Convert content of config-file into dictionary."""
    
    title = 'config_dict'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.config_dict(self.input(0)))
        

class Deepcopy_Node(NodeBase):
    """
    Deep copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.
    """
    
    title = 'deepcopy'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='memo', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.deepcopy(self.input(0), self.input(1)))
        

class Degrees_Node(NodeBase):
    """
     Set angle measurement units to degrees.

        Optional argument:
        fullcircle -  a number

        Set angle measurement units, i. e. set number
        of 'degrees' for a full circle. Default value is
        360 degrees.

        Example:
        >>> left(90)
        >>> heading()
        90

        Change angle measurement unit to grad (also known as gon,
        grade, or gradian and equals 1/100-th of the right angle.)
        >>> degrees(400.0)
        >>> heading()
        100

        """
    
    title = 'degrees'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='fullcircle', dtype=dtypes.Data(default=360.0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.degrees(self.input(0)))
        

class Delay_Node(NodeBase):
    """
     Return or set the drawing delay in milliseconds.

        Optional argument:
        delay -- positive integer

        Example:
        >>> delay(15)
        >>> delay()
        15
        """
    
    title = 'delay'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='delay', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.delay(self.input(0)))
        

class Distance_Node(NodeBase):
    """
    Return the distance from the turtle to (x,y) in turtle step units.

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Example:
        >>> pos()
        (0.00, 0.00)
        >>> distance(30,40)
        50.0
        >>> pen = Turtle()
        >>> pen.forward(77)
        >>> distance(pen)
        77.0
        """
    
    title = 'distance'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='y', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.distance(self.input(0), self.input(1)))
        

class Done_Node(NodeBase):
    """
    Starts event loop - calling Tkinter's mainloop function.

        No argument.

        Must be last statement in a turtle graphics program.
        Must NOT be used if a script is run from within IDLE in -n mode
        (No subprocess) - for interactive use of turtle graphics.

        Example:
        >>> mainloop()

        """
    
    title = 'done'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.done())
        

class Dot_Node(NodeBase):
    """
    Draw a dot with diameter size, using color.

        Optional arguments:
        size -- an integer >= 1 (if given)
        color -- a colorstring or a numeric color tuple

        Draw a circular dot with diameter size, using color.
        If size is not given, the maximum of pensize+4 and 2*pensize is used.

        Example:
        >>> dot()
        >>> fd(50); dot(20, "blue"); fd(50)
        """
    
    title = 'dot'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='size', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.dot(self.input(0)))
        

class Down_Node(NodeBase):
    """
    Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example:
        >>> pendown()
        """
    
    title = 'down'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.down())
        

class End_Fill_Node(NodeBase):
    """
    Fill the shape drawn after the call begin_fill().

        No argument.

        Example:
        >>> color("black", "red")
        >>> begin_fill()
        >>> circle(60)
        >>> end_fill()
        """
    
    title = 'end_fill'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.end_fill())
        

class End_Poly_Node(NodeBase):
    """
    Stop recording the vertices of a polygon.

        No argument.

        Stop recording the vertices of a polygon. Current turtle position is
        last point of polygon. This will be connected with the first point.

        Example:
        >>> end_poly()
        """
    
    title = 'end_poly'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.end_poly())
        

class Exitonclick_Node(NodeBase):
    """
    Go into mainloop until the mouse is clicked.

        No arguments.

        Bind bye() method to mouseclick on TurtleScreen.
        If "using_IDLE" - value in configuration dictionary is False
        (default value), enter mainloop.
        If IDLE with -n switch (no subprocess) is used, this value should be
        set to True in turtle.cfg. In this case IDLE's mainloop
        is active also for the client script.

        This is a method of the Screen-class and not available for
        TurtleScreen instances.

        Example:
        >>> exitonclick()

        """
    
    title = 'exitonclick'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.exitonclick())
        

class Fd_Node(NodeBase):
    """
    Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example:
        >>> position()
        (0.00, 0.00)
        >>> forward(25)
        >>> position()
        (25.00,0.00)
        >>> forward(-75)
        >>> position()
        (-50.00,0.00)
        """
    
    title = 'fd'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='distance'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.fd(self.input(0)))
        

class Fillcolor_Node(NodeBase):
    """
     Return or set the fillcolor.

        Arguments:
        Four input formats are allowed:
          - fillcolor()
            Return the current fillcolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - fillcolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - fillcolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - fillcolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the interior of that polygon is drawn
        with the newly set fillcolor.

        Example:
        >>> fillcolor('violet')
        >>> col = pencolor()
        >>> fillcolor(col)
        >>> fillcolor(0, .5, 0)
        """
    
    title = 'fillcolor'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.fillcolor())
        

class Filling_Node(NodeBase):
    """
    Return fillstate (True if filling, False else).

        No argument.

        Example:
        >>> begin_fill()
        >>> if filling():
        ...     pensize(5)
        ... else:
        ...     pensize(3)
        """
    
    title = 'filling'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.filling())
        

class Forward_Node(NodeBase):
    """
    Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example:
        >>> position()
        (0.00, 0.00)
        >>> forward(25)
        >>> position()
        (25.00,0.00)
        >>> forward(-75)
        >>> position()
        (-50.00,0.00)
        """
    
    title = 'forward'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='distance'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.forward(self.input(0)))
        

class Get_Poly_Node(NodeBase):
    """
    Return the lastly recorded polygon.

        No argument.

        Example:
        >>> p = get_poly()
        >>> register_shape("myFavouriteShape", p)
        """
    
    title = 'get_poly'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.get_poly())
        

class Get_Shapepoly_Node(NodeBase):
    """
    Return the current shape polygon as tuple of coordinate pairs.

        No argument.

        Examples:
        >>> shape("square")
        >>> shapetransform(4, -1, 0, 2)
        >>> get_shapepoly()
        ((50, -20), (30, 20), (-50, 20), (-30, -20))

        """
    
    title = 'get_shapepoly'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.get_shapepoly())
        

class Getcanvas_Node(NodeBase):
    """
    Return the Canvas of this TurtleScreen.

        No argument.

        Example:
        >>> cv = getcanvas()
        >>> cv
        <turtle.ScrolledCanvas instance at 0x010742D8>
        """
    
    title = 'getcanvas'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.getcanvas())
        

class Getmethparlist_Node(NodeBase):
    """
    Get strings describing the arguments for the given object

    Returns a pair of strings representing function parameter lists
    including parenthesis.  The first string is suitable for use in
    function definition and the second is suitable for use in function
    call.  The "self" parameter is not included.
    """
    
    title = 'getmethparlist'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='ob'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.getmethparlist(self.input(0)))
        

class Getpen_Node(NodeBase):
    """
    Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <Turtle object at 0x0187D810>
        >>> turtles()
        [<Turtle object at 0x0187D810>]
        """
    
    title = 'getpen'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.getpen())
        

class Getscreen_Node(NodeBase):
    """
    Return the TurtleScreen object, the turtle is drawing  on.

        No argument.

        Return the TurtleScreen object, the turtle is drawing  on.
        So TurtleScreen-methods can be called for that object.

        Example:
        >>> ts = getscreen()
        >>> ts
        <TurtleScreen object at 0x0106B770>
        >>> ts.bgcolor("pink")
        """
    
    title = 'getscreen'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.getscreen())
        

class Getshapes_Node(NodeBase):
    """
    Return a list of names of all currently available turtle shapes.

        No argument.

        Example:
        >>> getshapes()
        ['arrow', 'blank', 'circle', ... , 'turtle']
        """
    
    title = 'getshapes'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.getshapes())
        

class Getturtle_Node(NodeBase):
    """
    Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <Turtle object at 0x0187D810>
        >>> turtles()
        [<Turtle object at 0x0187D810>]
        """
    
    title = 'getturtle'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.getturtle())
        

class Goto_Node(NodeBase):
    """
    Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example:
        >>> tp = pos()
        >>> tp
        (0.00, 0.00)
        >>> setpos(60,30)
        >>> pos()
        (60.00,30.00)
        >>> setpos((20,80))
        >>> pos()
        (20.00,80.00)
        >>> setpos(tp)
        >>> pos()
        (0.00,0.00)
        """
    
    title = 'goto'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='y', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.goto(self.input(0), self.input(1)))
        

class Heading_Node(NodeBase):
    """
     Return the turtle's current heading.

        No arguments.

        Example:
        >>> left(67)
        >>> heading()
        67.0
        """
    
    title = 'heading'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.heading())
        

class Hideturtle_Node(NodeBase):
    """
    Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example:
        >>> hideturtle()
        """
    
    title = 'hideturtle'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.hideturtle())
        

class Home_Node(NodeBase):
    """
    Move turtle to the origin - coordinates (0,0).

        No arguments.

        Move turtle to the origin - coordinates (0,0) and set its
        heading to its start-orientation (which depends on mode).

        Example:
        >>> home()
        """
    
    title = 'home'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.home())
        

class Ht_Node(NodeBase):
    """
    Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example:
        >>> hideturtle()
        """
    
    title = 'ht'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.ht())
        

class Isdown_Node(NodeBase):
    """
    Return True if pen is down, False if it's up.

        No argument.

        Example:
        >>> penup()
        >>> isdown()
        False
        >>> pendown()
        >>> isdown()
        True
        """
    
    title = 'isdown'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.isdown())
        

class Isfile_Node(NodeBase):
    """
    Test whether a path is a regular file"""
    
    title = 'isfile'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.isfile(self.input(0)))
        

class Isvisible_Node(NodeBase):
    """
    Return True if the Turtle is shown, False if it's hidden.

        No argument.

        Example:
        >>> hideturtle()
        >>> print isvisible():
        False
        """
    
    title = 'isvisible'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.isvisible())
        

class Join_Node(NodeBase):
    """
    """
    
    title = 'join'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.join(self.input(0)))
        

class Left_Node(NodeBase):
    """
    Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example:
        >>> heading()
        22.0
        >>> left(45)
        >>> heading()
        67.0
        """
    
    title = 'left'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='angle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.left(self.input(0)))
        

class Listen_Node(NodeBase):
    """
    Set focus on TurtleScreen (in order to collect key-events)

        No arguments.
        Dummy arguments are provided in order
        to be able to pass listen to the onclick method.

        Example:
        >>> listen()
        """
    
    title = 'listen'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='xdummy', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='ydummy', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.listen(self.input(0), self.input(1)))
        

class Lt_Node(NodeBase):
    """
    Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example:
        >>> heading()
        22.0
        >>> left(45)
        >>> heading()
        67.0
        """
    
    title = 'lt'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='angle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.lt(self.input(0)))
        

class Mainloop_Node(NodeBase):
    """
    Starts event loop - calling Tkinter's mainloop function.

        No argument.

        Must be last statement in a turtle graphics program.
        Must NOT be used if a script is run from within IDLE in -n mode
        (No subprocess) - for interactive use of turtle graphics.

        Example:
        >>> mainloop()

        """
    
    title = 'mainloop'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.mainloop())
        

class Mode_Node(NodeBase):
    """
    Set turtle-mode ('standard', 'logo' or 'world') and perform reset.

        Optional argument:
        mode -- one of the strings 'standard', 'logo' or 'world'

        Mode 'standard' is compatible with turtle.py.
        Mode 'logo' is compatible with most Logo-Turtle-Graphics.
        Mode 'world' uses userdefined 'worldcoordinates'. *Attention*: in
        this mode angles appear distorted if x/y unit-ratio doesn't equal 1.
        If mode is not given, return the current mode.

             Mode      Initial turtle heading     positive angles
         ------------|-------------------------|-------------------
          'standard'    to the right (east)       counterclockwise
            'logo'        upward    (north)         clockwise

        Examples:
        >>> mode('logo')   # resets turtle heading to north
        >>> mode()
        'logo'
        """
    
    title = 'mode'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='mode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.mode(self.input(0)))
        

class Numinput_Node(NodeBase):
    """
    Pop up a dialog window for input of a number.

        Arguments: title is the title of the dialog window,
        prompt is a text mostly describing what numerical information to input.
        default: default value
        minval: minimum value for input
        maxval: maximum value for input

        The number input must be in the range minval .. maxval if these are
        given. If not, a hint is issued and the dialog remains open for
        correction. Return the number input.
        If the dialog is canceled,  return None.

        Example:
        >>> numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)

        """
    
    title = 'numinput'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='title'),
        NodeInputBP(label='prompt'),
        NodeInputBP(label='default', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='minval', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='maxval', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.numinput(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Onclick_Node(NodeBase):
    """
    Bind fun to mouse-click event on this turtle on canvas.

        Arguments:
        fun --  a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        btn --  number of the mouse-button defaults to 1 (left mouse button).
        add --  True or False. If True, new binding will be added, otherwise
                it will replace a former binding.

        Example for the anonymous turtle, i. e. the procedural way:

        >>> def turn(x, y):
        ...     left(360)
        ...
        >>> onclick(turn)  # Now clicking into the turtle will turn it.
        >>> onclick(None)  # event-binding will be removed
        """
    
    title = 'onclick'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='fun'),
        NodeInputBP(label='btn', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='add', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.onclick(self.input(0), self.input(1), self.input(2)))
        

class Ondrag_Node(NodeBase):
    """
    Bind fun to mouse-move event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
               the coordinates of the clicked point on the canvas.
        btn -- number of the mouse-button defaults to 1 (left mouse button).

        Every sequence of mouse-move-events on a turtle is preceded by a
        mouse-click event on that 

        Example:
        >>> ondrag(goto)

        Subsequently clicking and dragging a Turtle will move it
        across the screen thereby producing handdrawings (if pen is
        down).
        """
    
    title = 'ondrag'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='fun'),
        NodeInputBP(label='btn', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='add', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.ondrag(self.input(0), self.input(1), self.input(2)))
        

class Onkey_Node(NodeBase):
    """
    Bind fun to key-release event of key.

        Arguments:
        fun -- a function with no arguments
        key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

        In order to be able to register key-events, TurtleScreen
        must have focus. (See method listen.)

        Example:

        >>> def f():
        ...     fd(50)
        ...     lt(60)
        ...
        >>> onkey(f, "Up")
        >>> listen()

        Subsequently the turtle can be moved by repeatedly pressing
        the up-arrow key, consequently drawing a hexagon

        """
    
    title = 'onkey'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='fun'),
        NodeInputBP(label='key'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.onkey(self.input(0), self.input(1)))
        

class Onkeypress_Node(NodeBase):
    """
    Bind fun to key-press event of key if key is given,
        or to any key-press-event if no key is given.

        Arguments:
        fun -- a function with no arguments
        key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

        In order to be able to register key-events, TurtleScreen
        must have focus. (See method listen.)

        Example (for a TurtleScreen instance named screen
        and a Turtle instance named turtle):

        >>> def f():
        ...     fd(50)
        ...     lt(60)
        ...
        >>> onkeypress(f, "Up")
        >>> listen()

        Subsequently the turtle can be moved by repeatedly pressing
        the up-arrow key, or by keeping pressed the up-arrow key.
        consequently drawing a hexagon.
        """
    
    title = 'onkeypress'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='fun'),
        NodeInputBP(label='key', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.onkeypress(self.input(0), self.input(1)))
        

class Onkeyrelease_Node(NodeBase):
    """
    Bind fun to key-release event of key.

        Arguments:
        fun -- a function with no arguments
        key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

        In order to be able to register key-events, TurtleScreen
        must have focus. (See method listen.)

        Example:

        >>> def f():
        ...     fd(50)
        ...     lt(60)
        ...
        >>> onkey(f, "Up")
        >>> listen()

        Subsequently the turtle can be moved by repeatedly pressing
        the up-arrow key, consequently drawing a hexagon

        """
    
    title = 'onkeyrelease'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='fun'),
        NodeInputBP(label='key'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.onkeyrelease(self.input(0), self.input(1)))
        

class Onrelease_Node(NodeBase):
    """
    Bind fun to mouse-button-release event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        btn --  number of the mouse-button defaults to 1 (left mouse button).

        Example (for a MyTurtle instance named joe):
        >>> class MyTurtle(Turtle):
        ...     def glow(self,x,y):
        ...             self.fillcolor("red")
        ...     def unglow(self,x,y):
        ...             self.fillcolor("")
        ...
        >>> joe = MyTurtle()
        >>> joe.onclick(joe.glow)
        >>> joe.onrelease(joe.unglow)

        Clicking on joe turns fillcolor red, unclicking turns it to
        transparent.
        """
    
    title = 'onrelease'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='fun'),
        NodeInputBP(label='btn', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='add', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.onrelease(self.input(0), self.input(1), self.input(2)))
        

class Onscreenclick_Node(NodeBase):
    """
    Bind fun to mouse-click event on canvas.

        Arguments:
        fun -- a function with two arguments, the coordinates of the
               clicked point on the canvas.
        btn -- the number of the mouse-button, defaults to 1

        Example (for a TurtleScreen instance named screen)

        >>> onclick(goto)
        >>> # Subsequently clicking into the TurtleScreen will
        >>> # make the turtle move to the clicked point.
        >>> onclick(None)
        """
    
    title = 'onscreenclick'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='fun'),
        NodeInputBP(label='btn', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='add', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.onscreenclick(self.input(0), self.input(1), self.input(2)))
        

class Ontimer_Node(NodeBase):
    """
    Install a timer, which calls fun after t milliseconds.

        Arguments:
        fun -- a function with no arguments.
        t -- a number >= 0

        Example:

        >>> running = True
        >>> def f():
        ...     if running:
        ...             fd(50)
        ...             lt(60)
        ...             ontimer(f, 250)
        ...
        >>> f()   # makes the turtle marching around
        >>> running = False
        """
    
    title = 'ontimer'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='fun'),
        NodeInputBP(label='t', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.ontimer(self.input(0), self.input(1)))
        

class Pd_Node(NodeBase):
    """
    Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example:
        >>> pendown()
        """
    
    title = 'pd'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.pd())
        

class Pen_Node(NodeBase):
    """
    Return or set the pen's attributes.

        Arguments:
            pen -- a dictionary with some or all of the below listed keys.
            **pendict -- one or more keyword-arguments with the below
                         listed keys as keywords.

        Return or set the pen's attributes in a 'pen-dictionary'
        with the following key/value pairs:
           "shown"      :   True/False
           "pendown"    :   True/False
           "pencolor"   :   color-string or color-tuple
           "fillcolor"  :   color-string or color-tuple
           "pensize"    :   positive number
           "speed"      :   number in range 0..10
           "resizemode" :   "auto" or "user" or "noresize"
           "stretchfactor": (positive number, positive number)
           "shearfactor":   number
           "outline"    :   positive number
           "tilt"       :   number

        This dictionary can be used as argument for a subsequent
        pen()-call to restore the former pen-state. Moreover one
        or more of these attributes can be provided as keyword-arguments.
        This can be used to set several pen attributes in one statement.


        Examples:
        >>> pen(fillcolor="black", pencolor="red", pensize=10)
        >>> pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> penstate=pen()
        >>> color("yellow","")
        >>> penup()
        >>> pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> p.pen(penstate, fillcolor="green")
        >>> p.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        """
    
    title = 'pen'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='pen', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.pen(self.input(0)))
        

class Pencolor_Node(NodeBase):
    """
     Return or set the pencolor.

        Arguments:
        Four input formats are allowed:
          - pencolor()
            Return the current pencolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - pencolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - pencolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - pencolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the outline of that polygon is drawn
        with the newly set pencolor.

        Example:
        >>> pencolor('brown')
        >>> tup = (0.2, 0.8, 0.55)
        >>> pencolor(tup)
        >>> pencolor()
        '#33cc8c'
        """
    
    title = 'pencolor'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.pencolor())
        

class Pendown_Node(NodeBase):
    """
    Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example:
        >>> pendown()
        """
    
    title = 'pendown'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.pendown())
        

class Pensize_Node(NodeBase):
    """
    Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example:
        >>> pensize()
        1
        >>> pensize(10)   # from here on lines of width 10 are drawn
        """
    
    title = 'pensize'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='width', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.pensize(self.input(0)))
        

class Penup_Node(NodeBase):
    """
    Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example:
        >>> penup()
        """
    
    title = 'penup'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.penup())
        

class Pos_Node(NodeBase):
    """
    Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example:
        >>> pos()
        (0.00, 240.00)
        """
    
    title = 'pos'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.pos())
        

class Position_Node(NodeBase):
    """
    Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example:
        >>> pos()
        (0.00, 240.00)
        """
    
    title = 'position'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.position())
        

class Pu_Node(NodeBase):
    """
    Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example:
        >>> penup()
        """
    
    title = 'pu'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.pu())
        

class Radians_Node(NodeBase):
    """
     Set the angle measurement units to radians.

        No arguments.

        Example:
        >>> heading()
        90
        >>> radians()
        >>> heading()
        1.5707963267948966
        """
    
    title = 'radians'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.radians())
        

class Read_Docstrings_Node(NodeBase):
    """
    Read in docstrings from lang-specific docstring dictionary.

    Transfer docstrings, translated to lang, from a dictionary-file
    to the methods of classes Screen and Turtle and - in revised form -
    to the corresponding functions.
    """
    
    title = 'read_docstrings'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='lang'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.read_docstrings(self.input(0)))
        

class Readconfig_Node(NodeBase):
    """
    Read config-files, change configuration-dict accordingly.

    If there is a turtle.cfg file in the current working directory,
    read it from there. If this contains an importconfig-value,
    say 'myway', construct filename turtle_mayway.cfg else use
    turtle.cfg and read it from the import-directory, where
    turtle.py is located.
    Update configuration dictionary first according to config-file,
    in the import directory, then according to config-file in the
    current working directory.
    If no config-file is found, the default configuration is used.
    """
    
    title = 'readconfig'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='cfgdict'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.readconfig(self.input(0)))
        

class Register_Shape_Node(NodeBase):
    """
    Adds a turtle shape to TurtleScreen's shapelist.

        Arguments:
        (1) name is the name of a gif-file and shape is None.
            Installs the corresponding image shape.
            !! Image-shapes DO NOT rotate when turning the turtle,
            !! so they do not display the heading of the turtle!
        (2) name is an arbitrary string and shape is a tuple
            of pairs of coordinates. Installs the corresponding
            polygon shape
        (3) name is an arbitrary string and shape is a
            (compound) Shape object. Installs the corresponding
            compound shape.
        To use a shape, you have to issue the command shape(shapename).

        call: register_shape("turtle.gif")
        --or: register_shape("tri", ((0,0), (10,10), (-10,10)))

        Example:
        >>> register_shape("triangle", ((5,-3),(0,5),(-5,-3)))

        """
    
    title = 'register_shape'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='shape', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.register_shape(self.input(0), self.input(1)))
        

class Reset_Node(NodeBase):
    """
    Delete the turtle's drawings and restore its default values.

        No argument.

        Delete the turtle's drawings from the screen, re-center the turtle
        and set variables to the default values.

        Example:
        >>> position()
        (0.00,-22.00)
        >>> heading()
        100.0
        >>> reset()
        >>> position()
        (0.00,0.00)
        >>> heading()
        0.0
        """
    
    title = 'reset'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.reset())
        

class Resetscreen_Node(NodeBase):
    """
    Reset all Turtles on the Screen to their initial state.

        No argument.

        Example:
        >>> reset()
        """
    
    title = 'resetscreen'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.resetscreen())
        

class Resizemode_Node(NodeBase):
    """
    Set resizemode to one of the values: "auto", "user", "noresize".

        (Optional) Argument:
        rmode -- one of the strings "auto", "user", "noresize"

        Different resizemodes have the following effects:
          - "auto" adapts the appearance of the turtle
                   corresponding to the value of pensize.
          - "user" adapts the appearance of the turtle according to the
                   values of stretchfactor and outlinewidth (outline),
                   which are set by shapesize()
          - "noresize" no adaption of the turtle's appearance takes place.
        If no argument is given, return current resizemode.
        resizemode("user") is called by a call of shapesize with arguments.


        Examples:
        >>> resizemode("noresize")
        >>> resizemode()
        'noresize'
        """
    
    title = 'resizemode'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='rmode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.resizemode(self.input(0)))
        

class Right_Node(NodeBase):
    """
    Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example:
        >>> heading()
        22.0
        >>> right(45)
        >>> heading()
        337.0
        """
    
    title = 'right'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='angle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.right(self.input(0)))
        

class Rt_Node(NodeBase):
    """
    Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example:
        >>> heading()
        22.0
        >>> right(45)
        >>> heading()
        337.0
        """
    
    title = 'rt'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='angle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.rt(self.input(0)))
        

class Screensize_Node(NodeBase):
    """
    Resize the canvas the turtles are drawing on.

        Optional arguments:
        canvwidth -- positive integer, new width of canvas in pixels
        canvheight --  positive integer, new height of canvas in pixels
        bg -- colorstring or color-tuple, new backgroundcolor
        If no arguments are given, return current (canvaswidth, canvasheight)

        Do not alter the drawing window. To observe hidden parts of
        the canvas use the scrollbars. (Can make visible those parts
        of a drawing, which were outside the canvas before!)

        Example (for a Turtle instance named turtle):
        >>> turtle.screensize(2000,1500)
        >>> # e.g. to search for an erroneously escaped turtle ;-)
        """
    
    title = 'screensize'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='canvwidth', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='canvheight', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='bg', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.screensize(self.input(0), self.input(1), self.input(2)))
        

class Seth_Node(NodeBase):
    """
    Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example:
        >>> setheading(90)
        >>> heading()
        90
        """
    
    title = 'seth'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='to_angle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.seth(self.input(0)))
        

class Setheading_Node(NodeBase):
    """
    Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example:
        >>> setheading(90)
        >>> heading()
        90
        """
    
    title = 'setheading'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='to_angle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.setheading(self.input(0)))
        

class Setpos_Node(NodeBase):
    """
    Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example:
        >>> tp = pos()
        >>> tp
        (0.00, 0.00)
        >>> setpos(60,30)
        >>> pos()
        (60.00,30.00)
        >>> setpos((20,80))
        >>> pos()
        (20.00,80.00)
        >>> setpos(tp)
        >>> pos()
        (0.00,0.00)
        """
    
    title = 'setpos'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='y', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.setpos(self.input(0), self.input(1)))
        

class Setposition_Node(NodeBase):
    """
    Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example:
        >>> tp = pos()
        >>> tp
        (0.00, 0.00)
        >>> setpos(60,30)
        >>> pos()
        (60.00,30.00)
        >>> setpos((20,80))
        >>> pos()
        (20.00,80.00)
        >>> setpos(tp)
        >>> pos()
        (0.00,0.00)
        """
    
    title = 'setposition'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='y', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.setposition(self.input(0), self.input(1)))
        

class Settiltangle_Node(NodeBase):
    """
    Rotate the turtleshape to point in the specified direction

        Argument: angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).


        Examples:
        >>> shape("circle")
        >>> shapesize(5,2)
        >>> settiltangle(45)
        >>> stamp()
        >>> fd(50)
        >>> settiltangle(-45)
        >>> stamp()
        >>> fd(50)
        """
    
    title = 'settiltangle'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='angle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.settiltangle(self.input(0)))
        

class Setundobuffer_Node(NodeBase):
    """
    Set or disable undobuffer.

        Argument:
        size -- an integer or None

        If size is an integer an empty undobuffer of given size is installed.
        Size gives the maximum number of turtle-actions that can be undone
        by the undo() function.
        If size is None, no undobuffer is present.

        Example:
        >>> setundobuffer(42)
        """
    
    title = 'setundobuffer'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='size'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.setundobuffer(self.input(0)))
        

class Setup_Node(NodeBase):
    """
     Set the size and position of the main window.

        Arguments:
        width: as integer a size in pixels, as float a fraction of the 
          Default is 50% of 
        height: as integer the height in pixels, as float a fraction of the
           Default is 75% of 
        startx: if positive, starting position in pixels from the left
          edge of the screen, if negative from the right edge
          Default, startx=None is to center window horizontally.
        starty: if positive, starting position in pixels from the top
          edge of the screen, if negative from the bottom edge
          Default, starty=None is to center window vertically.

        Examples:
        >>> setup (width=200, height=200, startx=0, starty=0)

        sets window to 200x200 pixels, in upper left of screen

        >>> setup(width=.75, height=0.5, startx=None, starty=None)

        sets window to 75% of screen by 50% of screen and centers
        """
    
    title = 'setup'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='width', dtype=dtypes.Data(default=0.5, size='s')),
        NodeInputBP(label='height', dtype=dtypes.Data(default=0.75, size='s')),
        NodeInputBP(label='startx', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='starty', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.setup(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Setworldcoordinates_Node(NodeBase):
    """
    Set up a user defined coordinate-system.

        Arguments:
        llx -- a number, x-coordinate of lower left corner of canvas
        lly -- a number, y-coordinate of lower left corner of canvas
        urx -- a number, x-coordinate of upper right corner of canvas
        ury -- a number, y-coordinate of upper right corner of canvas

        Set up user coodinat-system and switch to mode 'world' if necessary.
        This performs a reset. If mode 'world' is already active,
        all drawings are redrawn according to the new coordinates.

        But ATTENTION: in user-defined coordinatesystems angles may appear
        distorted. (see Screen.mode())

        Example:
        >>> setworldcoordinates(-10,-0.5,50,1.5)
        >>> for _ in range(36):
        ...     left(10)
        ...     forward(0.5)
        """
    
    title = 'setworldcoordinates'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='llx'),
        NodeInputBP(label='lly'),
        NodeInputBP(label='urx'),
        NodeInputBP(label='ury'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.setworldcoordinates(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Setx_Node(NodeBase):
    """
    Set the turtle's first coordinate to x

        Argument:
        x -- a number (integer or float)

        Set the turtle's first coordinate to x, leave second coordinate
        unchanged.

        Example:
        >>> position()
        (0.00, 240.00)
        >>> setx(10)
        >>> position()
        (10.00, 240.00)
        """
    
    title = 'setx'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.setx(self.input(0)))
        

class Sety_Node(NodeBase):
    """
    Set the turtle's second coordinate to y

        Argument:
        y -- a number (integer or float)

        Set the turtle's first coordinate to x, second coordinate remains
        unchanged.

        Example:
        >>> position()
        (0.00, 40.00)
        >>> sety(-10)
        >>> position()
        (0.00, -10.00)
        """
    
    title = 'sety'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='y'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.sety(self.input(0)))
        

class Shape_Node(NodeBase):
    """
    Set turtle shape to shape with given name / return current shapename.

        Optional argument:
        name -- a string, which is a valid shapename

        Set turtle shape to shape with given name or, if name is not given,
        return name of current shape.
        Shape with name must exist in the TurtleScreen's shape dictionary.
        Initially there are the following polygon shapes:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
        To learn about how to deal with shapes see Screen-method register_shape.

        Example:
        >>> shape()
        'arrow'
        >>> shape("turtle")
        >>> shape()
        'turtle'
        """
    
    title = 'shape'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='name', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.shape(self.input(0)))
        

class Shapesize_Node(NodeBase):
    """
    Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optional arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples:
        >>> resizemode("user")
        >>> shapesize(5, 5, 12)
        >>> shapesize(outline=8)
        """
    
    title = 'shapesize'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='stretch_wid', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='stretch_len', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='outline', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.shapesize(self.input(0), self.input(1), self.input(2)))
        

class Shapetransform_Node(NodeBase):
    """
    Set or return the current transformation matrix of the turtle shape.

        Optional arguments: t11, t12, t21, t22 -- numbers.

        If none of the matrix elements are given, return the transformation
        matrix.
        Otherwise set the given elements and transform the turtleshape
        according to the matrix consisting of first row t11, t12 and
        second row t21, 22.
        Modify stretchfactor, shearfactor and tiltangle according to the
        given matrix.

        Examples:
        >>> shape("square")
        >>> shapesize(4,2)
        >>> shearfactor(-0.5)
        >>> shapetransform()
        (4.0, -1.0, -0.0, 2.0)
        """
    
    title = 'shapetransform'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='t11', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='t12', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='t21', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='t22', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.shapetransform(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Shearfactor_Node(NodeBase):
    """
    Set or return the current shearfactor.

        Optional argument: shear -- number, tangent of the shear angle

        Shear the turtleshape according to the given shearfactor shear,
        which is the tangent of the shear angle. DO NOT change the
        turtle's heading (direction of movement).
        If shear is not given: return the current shearfactor, i. e. the
        tangent of the shear angle, by which lines parallel to the
        heading of the turtle are sheared.

        Examples:
        >>> shape("circle")
        >>> shapesize(5,2)
        >>> shearfactor(0.5)
        >>> shearfactor()
        >>> 0.5
        """
    
    title = 'shearfactor'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='shear', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.shearfactor(self.input(0)))
        

class Showturtle_Node(NodeBase):
    """
    Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example:
        >>> hideturtle()
        >>> showturtle()
        """
    
    title = 'showturtle'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.showturtle())
        

class Speed_Node(NodeBase):
    """
     Return or set the turtle's speed.

        Optional argument:
        speed -- an integer in the range 0..10 or a speedstring (see below)

        Set the turtle's speed to an integer value in the range 0 .. 10.
        If no argument is given: return current speed.

        If input is a number greater than 10 or smaller than 0.5,
        speed is set to 0.
        Speedstrings  are mapped to speedvalues in the following way:
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6
            'slow'    :  3
            'slowest' :  1
        speeds from 1 to 10 enforce increasingly faster animation of
        line drawing and turtle turning.

        Attention:
        speed = 0 : *no* animation takes place. forward/back makes turtle jump
        and likewise left/right make the turtle turn instantly.

        Example:
        >>> speed(3)
        """
    
    title = 'speed'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='speed', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.speed(self.input(0)))
        

class Split_Node(NodeBase):
    """
    Split a pathname.

    Return tuple (head, tail) where tail is everything after the final slash.
    Either part may be empty."""
    
    title = 'split'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.split(self.input(0)))
        

class St_Node(NodeBase):
    """
    Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example:
        >>> hideturtle()
        >>> showturtle()
        """
    
    title = 'st'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.st())
        

class Stamp_Node(NodeBase):
    """
    Stamp a copy of the turtleshape onto the canvas and return its id.

        No argument.

        Stamp a copy of the turtle shape onto the canvas at the current
        turtle position. Return a stamp_id for that stamp, which can be
        used to delete it by calling clearstamp(stamp_id).

        Example:
        >>> color("blue")
        >>> stamp()
        13
        >>> fd(50)
        """
    
    title = 'stamp'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.stamp())
        

class Textinput_Node(NodeBase):
    """
    Pop up a dialog window for input of a string.

        Arguments: title is the title of the dialog window,
        prompt is a text mostly describing what information to input.

        Return the string input
        If the dialog is canceled, return None.

        Example:
        >>> textinput("NIM", "Name of first player:")

        """
    
    title = 'textinput'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='title'),
        NodeInputBP(label='prompt'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.textinput(self.input(0), self.input(1)))
        

class Tilt_Node(NodeBase):
    """
    Rotate the turtleshape by angle.

        Argument:
        angle - a number

        Rotate the turtleshape by angle from its current tilt-angle,
        but do NOT change the turtle's heading (direction of movement).

        Examples:
        >>> shape("circle")
        >>> shapesize(5,2)
        >>> tilt(30)
        >>> fd(50)
        >>> tilt(30)
        >>> fd(50)
        """
    
    title = 'tilt'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='angle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.tilt(self.input(0)))
        

class Tiltangle_Node(NodeBase):
    """
    Set or return the current tilt-angle.

        Optional argument: angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).
        If angle is not given: return the current tilt-angle, i. e. the angle
        between the orientation of the turtleshape and the heading of the
        turtle (its direction of movement).

        Deprecated since Python 3.1

        Examples:
        >>> shape("circle")
        >>> shapesize(5,2)
        >>> tilt(45)
        >>> tiltangle()
        """
    
    title = 'tiltangle'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='angle', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.tiltangle(self.input(0)))
        

class Title_Node(NodeBase):
    """
    Set title of turtle-window

        Argument:
        titlestring -- a string, to appear in the titlebar of the
                       turtle graphics window.

        This is a method of Screen-class. Not available for TurtleScreen-
        objects.

        Example:
        >>> title("Welcome to the turtle-zoo!")
        """
    
    title = 'title'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='titlestring'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.title(self.input(0)))
        

class Towards_Node(NodeBase):
    """
    Return the angle of the line from the turtle's position to (x, y).

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Return the angle, between the line from turtle-position to position
        specified by x, y and the turtle's start orientation. (Depends on
        modes - "standard" or "logo")

        Example:
        >>> pos()
        (10.00, 10.00)
        >>> towards(0,0)
        225.0
        """
    
    title = 'towards'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='y', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.towards(self.input(0), self.input(1)))
        

class Tracer_Node(NodeBase):
    """
    Turns turtle animation on/off and set delay for update drawings.

        Optional arguments:
        n -- nonnegative  integer
        delay -- nonnegative  integer

        If n is given, only each n-th regular screen update is really performed.
        (Can be used to accelerate the drawing of complex graphics.)
        Second arguments sets delay value (see RawTurtle.delay())

        Example:
        >>> tracer(8, 25)
        >>> dist = 2
        >>> for i in range(200):
        ...     fd(dist)
        ...     rt(90)
        ...     dist += 2
        """
    
    title = 'tracer'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='n', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='delay', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.tracer(self.input(0), self.input(1)))
        

class Turtles_Node(NodeBase):
    """
    Return the list of turtles on the 

        Example:
        >>> turtles()
        [<turtle.Turtle object at 0x00E11FB0>]
        """
    
    title = 'turtles'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.turtles())
        

class Turtlesize_Node(NodeBase):
    """
    Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optional arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples:
        >>> resizemode("user")
        >>> shapesize(5, 5, 12)
        >>> shapesize(outline=8)
        """
    
    title = 'turtlesize'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='stretch_wid', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='stretch_len', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='outline', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.turtlesize(self.input(0), self.input(1), self.input(2)))
        

class Undo_Node(NodeBase):
    """
    undo (repeatedly) the last turtle action.

        No argument.

        undo (repeatedly) the last turtle action.
        Number of available undo actions is determined by the size of
        the undobuffer.

        Example:
        >>> for i in range(4):
        ...     fd(50); lt(80)
        ...
        >>> for i in range(8):
        ...     undo()
        ...
        """
    
    title = 'undo'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.undo())
        

class Undobufferentries_Node(NodeBase):
    """
    Return count of entries in the undobuffer.

        No argument.

        Example:
        >>> while undobufferentries():
        ...     undo()
        """
    
    title = 'undobufferentries'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.undobufferentries())
        

class Up_Node(NodeBase):
    """
    Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example:
        >>> penup()
        """
    
    title = 'up'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.up())
        

class Update_Node(NodeBase):
    """
    Perform a TurtleScreen update.
        """
    
    title = 'update'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.update())
        

class Width_Node(NodeBase):
    """
    Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example:
        >>> pensize()
        1
        >>> pensize(10)   # from here on lines of width 10 are drawn
        """
    
    title = 'width'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='width', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.width(self.input(0)))
        

class Window_Height_Node(NodeBase):
    """
     Return the height of the turtle window.

        Example:
        >>> window_height()
        480
        """
    
    title = 'window_height'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.window_height())
        

class Window_Width_Node(NodeBase):
    """
     Return the width of the turtle window.

        Example:
        >>> window_width()
        640
        """
    
    title = 'window_width'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.window_width())
        

class Write_Node(NodeBase):
    """
    Write text at the current turtle position.

        Arguments:
        arg -- info, which is to be written to the TurtleScreen
        move (optional) -- True/False
        align (optional) -- one of the strings "left", "center" or right"
        font (optional) -- a triple (fontname, fontsize, fonttype)

        Write text - the string representation of arg - at the current
        turtle position according to align ("left", "center" or right")
        and with the given font.
        If move is True, the pen is moved to the bottom-right corner
        of the text. By default, move is False.

        Example:
        >>> write('Home = ', True, align="center")
        >>> write((0,0), True)
        """
    
    title = 'write'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='arg'),
        NodeInputBP(label='move', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='align', dtype=dtypes.Data(default='left', size='s')),
        NodeInputBP(label='font', dtype=dtypes.Data(default=('Arial', 8, 'normal'), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.write(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Write_Docstringdict_Node(NodeBase):
    """
    Create and write docstring-dictionary to file.

    Optional argument:
    filename -- a string, used as filename
                default value is turtle_docstringdict

    Has to be called explicitly, (not used by the turtle-graphics classes)
    The docstring dictionary will be written to the Python script <filname>.py
    It is intended to serve as a template for translation of the docstrings
    into different languages.
    """
    
    title = 'write_docstringdict'
    type_ = 'turtle'
    init_inputs = [
        NodeInputBP(label='filename', dtype=dtypes.Data(default='turtle_docstringdict', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.write_docstringdict(self.input(0)))
        

class Xcor_Node(NodeBase):
    """
     Return the turtle's x coordinate.

        No arguments.

        Example:
        >>> reset()
        >>> left(60)
        >>> forward(100)
        >>> print xcor()
        50.0
        """
    
    title = 'xcor'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.xcor())
        

class Ycor_Node(NodeBase):
    """
     Return the turtle's y coordinate
        ---
        No arguments.

        Example:
        >>> reset()
        >>> left(60)
        >>> forward(100)
        >>> print ycor()
        86.6025403784
        """
    
    title = 'ycor'
    type_ = 'turtle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, turtle.ycor())
        


export_nodes(
    Screen_Node,
    __Forwardmethods_Node,
    __Methoddict_Node,
    __Methods_Node,
    _Make_Global_Funcs_Node,
    _Screen_Docrevise_Node,
    _Turtle_Docrevise_Node,
    Addshape_Node,
    Back_Node,
    Backward_Node,
    Begin_Fill_Node,
    Begin_Poly_Node,
    Bgcolor_Node,
    Bgpic_Node,
    Bk_Node,
    Bye_Node,
    Circle_Node,
    Clear_Node,
    Clearscreen_Node,
    Clearstamp_Node,
    Clearstamps_Node,
    Clone_Node,
    Color_Node,
    Colormode_Node,
    Config_Dict_Node,
    Deepcopy_Node,
    Degrees_Node,
    Delay_Node,
    Distance_Node,
    Done_Node,
    Dot_Node,
    Down_Node,
    End_Fill_Node,
    End_Poly_Node,
    Exitonclick_Node,
    Fd_Node,
    Fillcolor_Node,
    Filling_Node,
    Forward_Node,
    Get_Poly_Node,
    Get_Shapepoly_Node,
    Getcanvas_Node,
    Getmethparlist_Node,
    Getpen_Node,
    Getscreen_Node,
    Getshapes_Node,
    Getturtle_Node,
    Goto_Node,
    Heading_Node,
    Hideturtle_Node,
    Home_Node,
    Ht_Node,
    Isdown_Node,
    Isfile_Node,
    Isvisible_Node,
    Join_Node,
    Left_Node,
    Listen_Node,
    Lt_Node,
    Mainloop_Node,
    Mode_Node,
    Numinput_Node,
    Onclick_Node,
    Ondrag_Node,
    Onkey_Node,
    Onkeypress_Node,
    Onkeyrelease_Node,
    Onrelease_Node,
    Onscreenclick_Node,
    Ontimer_Node,
    Pd_Node,
    Pen_Node,
    Pencolor_Node,
    Pendown_Node,
    Pensize_Node,
    Penup_Node,
    Pos_Node,
    Position_Node,
    Pu_Node,
    Radians_Node,
    Read_Docstrings_Node,
    Readconfig_Node,
    Register_Shape_Node,
    Reset_Node,
    Resetscreen_Node,
    Resizemode_Node,
    Right_Node,
    Rt_Node,
    Screensize_Node,
    Seth_Node,
    Setheading_Node,
    Setpos_Node,
    Setposition_Node,
    Settiltangle_Node,
    Setundobuffer_Node,
    Setup_Node,
    Setworldcoordinates_Node,
    Setx_Node,
    Sety_Node,
    Shape_Node,
    Shapesize_Node,
    Shapetransform_Node,
    Shearfactor_Node,
    Showturtle_Node,
    Speed_Node,
    Split_Node,
    St_Node,
    Stamp_Node,
    Textinput_Node,
    Tilt_Node,
    Tiltangle_Node,
    Title_Node,
    Towards_Node,
    Tracer_Node,
    Turtles_Node,
    Turtlesize_Node,
    Undo_Node,
    Undobufferentries_Node,
    Up_Node,
    Update_Node,
    Width_Node,
    Window_Height_Node,
    Window_Width_Node,
    Write_Node,
    Write_Docstringdict_Node,
    Xcor_Node,
    Ycor_Node,
)
