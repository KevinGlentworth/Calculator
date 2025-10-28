'''
Fonts: I prefer the older version of a & g, used in hand printed, rather than the typed one.
    Space Mono
    Code New Roman

v 3.2: Added cas function.
v 3.3: Added inline help.
v 3.4: Added entryBox recall.
v 3.5: Added Financial calculator
v 3.6: Added Stats calculator
v 3.7: Added rad/deg/grad button
v 4.0: Added unit converter
v 4.1: Reworked the inline help
v 4.2: Modified popup_msg to support Yes & No buttons
v 4.3: Changed Global vars to Class based.
v 4.4: Converted some widgets to customtkinter.
v 4.5: Converted all but Spinbox and Separator to customtkinter.
v 4.6: Changed to import only modules used.
v 4.7: Changed modules to classes.
v 4.8: Added degrees, minutes & seconds display.
v 4.9: Changed all str + str... to ''.join([str, ...])
v 4.10: Added sexagesimal display and entry.
v 4.11: Added subfactorial.
v 4.12: Added equation store.
v 4.13: Modified to allow some basic Complex number stuff
v 4.14: Tidied up various parts.
v 4.15: Added landscape screen layouts.
v 4.16: Changed inline help to use right-click on all objects.
v 4.17: Minor tweaks
v 4.18: Use pickle to save the stack values and redo stack to the registry.
v 5.0 : Moved def's with no class items into external file.
v 5.01: Changed join to f-strings

PYCharm packages etc.
Python 3.12
customtkinter 5.2.2
darkdetect 0.8.0 (via customtkinter)
ExifRead 3.0.0
Fraction 2.2.0
packaging 25.0
pillow 11.0.0
pip 23.2.1
pywin32 308 (installing 310 causes issues)
screeninfo 0.8.1
WMI 1.5.1
==========================================================================

Help.
============
For help, we use the docstring.
It assumes the first line, with the triple double quote, has a single
line description, then a blank line and then the help text.
The help text is followed by a blank line and then the Parameters and
Returns elements.
Help only displays the text between the first blank line and the
text prior to the blank line prior to the Parameters text.
Blocks of 4 spaces are also replaced with a null string, this helps
to reduce the margin on the left of the displayed text. If you want
to keep multiple spaces, use non-breaking spaces.


Things to add.
==============

Info stuff.
===========
  TKinter 8.5 Reference
    https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
  Python Language Reference:
    https://docs.python.org/3/reference/index.html# reference-index
  Tk winfo:
    https://www.tcl.tk/man/tcl8.6/TkCmd/winfo.html
  Ttk info:
    https://docs.python.org/3/library/tkinter.ttk.html
  Customtkinter
    https://customtkinter.tomschimansky.com/
  sys info:
    https://docs.python.org/3/library/sys.html
  Key Symbols:
    https://www.tcl.tk/man/tcl8.6/TkCmd/keysyms.html
  Data Types:
    https://phoenixnap.com/kb/python-data-types
  Cursors:
    https://www.tcl.tk/man/tcl8.4/TkCmd/cursors.html
  ctypes:
    MessageBoxExW:
     https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxexw
    MessageBox:
     https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messagebox
  Unicode Characters:
    https://en.wikipedia.org/wiki/List_of_Unicode_characters
      \N{SUPERSCRIPT THREE}
      pi = \u03C0
      tau = \u03c0
      degree = \u00b0
      middle dot = \u00b7
      mu = \u03BC
      non-breaking space = \u00A0
      check mark = \u2713
      laquo = \u00AB
      raquo = \u00BB
      \u23F4
      \u23F5
      \u0582 = fraction separator
      \u00B2 = superscript 2
      \u00B3 = superscript 3
      \u00B7 = Middle Dot
      \u00B9 = superscript 1
      \u2080 -> \u2089 = superscript 0 to 9

       https://www.tcl.tk/man/tcl8.6/TkCmd/keysyms.htm

  Virtual Keycodes
      https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
  Add a table
    tksheet

Case:
=====
Snake Case:
    variables, method names, filenames
    number_of_donuts = 34
Screaming Snake Case:
    constants
    NUMBER_OF_DONUTS = 34
Kebab Case:
    URL
    number-of-donuts = 34
Camel Case:
    Java, JavaScript, TypeScript
    numberOfDonuts = 34
Pascal Case:
    Java, JavaScript, TypeScript
    NumberOfDonuts = 34


The Google Python Style Guide has the following convention:
    module_name
    package_name
    ClassName
    method_name
    ExceptionName
    function_name
    GLOBAL_CONSTANT_NAME
    global_var_name
    instance_var_name
    function_parameter_name
    local_var_name.

A similar naming scheme should be applied to a CLASS_CONSTANT_NAME
'''
from os import getcwd, path
from os.path import realpath, dirname
from sys import version, version_info, platform, argv, _getframe, getsizeof, modules
from winreg import (OpenKey, QueryValueEx, CloseKey, CreateKeyEx, SetValueEx,
                    HKEY_CURRENT_USER, REG_SZ, REG_BINARY, KEY_WRITE)
from win32 import win32api
from inspect import currentframe
from re import split
import pickle
from typing import Never, Any
from time import sleep
# from timeit import default_timer
from random import randint, seed
from webbrowser import open_new
from getpass import getuser
from socket import gethostname, gethostbyname
from statistics import multimode, median
from datetime import datetime
from typing import Final
from math import (gamma, sqrt, sin, cos, tan, asin, acos, sinh, cosh,
                  tanh, asinh, acosh, atanh, atan, log, log10, pi,
                  tau, e, perm, comb, ceil, floor, gcd, trunc,
                  copysign)
from cmath import (sin as c_sin, sinh as c_sinh, asin as c_asin, asinh as c_asinh,
                   cos as c_cos, cosh as c_cosh, acos as c_acos, acosh as c_acosh,
                   tan as c_tan, tanh as c_tanh, atan as c_atan, atanh as c_atanh,
                   log as c_log, exp as c_exp)
from fraction import Fraction
from PIL import Image #  pip install pillow
from tkinter import Menu, IntVar, StringVar, LEFT, RIGHT, INSERT, GROOVE, RAISED, SUNKEN
from tkinter.ttk import Spinbox, Separator, Combobox
from customtkinter import (CTk, CTkButton, CTkFrame,
                           CTkLabel, CTkToplevel, CTkTextbox,
                           CTkSlider, CTkRadioButton, CTkOptionMenu,
                           CTkTabview, CTkFont, CTkEntry)

#  Stuff I've done # 
# 
from my_functions import (float_to_dms, integer_to_roman, float_to_word,
                          roman_to_integer, float_to_sexagesimal, sexagesimal_to_float,
                          combine_uom, eng_format, retrieve_object, get_tag_config)
from TextWidgetLink import TextWidgetLink
from TextWidgetHighlight import TextWidgetHighlight
from PopupMessage import PopupMessage

#  Constants
# 
BUTTON_WIDTH: Final [int] = 80
BUTTON_HEIGHT: Final [int] = 30
ENTRY_WIDTH: Final [int] = BUTTON_WIDTH * 6 + 50
MENU_FONT: Final [tuple] = ('Code New Roman', 12) # -17)

CALC_VERSION: Final [int] = 5
CALC_SUBVERSION: Final [int] = 0
PYTHON_MAJOR_VERSION: Final [int] = 3
PYTHON_MINOR_VERSION: Final [int] = 10

STACK_DEPTH: Final [int] = 10

#  Colours defined by stdout.shell keywords
ORANGE: Final = 'KEYWORD'
GREEN: Final = 'STRING'
BLACK: Final = 'SYNC'
PURPLE: Final = 'BUILTIN'
RED: Final = 'COMMENT'
BLUE: Final = 'DEFINITION'
BLACK_ON_RED: Final = 'ERROR'

# 
#  Extensions to existing classes.
class CTkTextbox(CTkTextbox):
    '''CTkTextbox extension'''
    def replace_text(self, new_text: str, tags = None) -> None:
        ''' Changes textbox text with one line of code, rather than two.'''
        super(CTkTextbox, self).delete('0.0', 'end')
        super(CTkTextbox, self).insert('end', new_text, tags)


class CTkEntry(CTkEntry):
    '''CTkEntry extension'''
    def replace_text(self, new_text: str) -> None:
        ''' Changes entry text with one line of code, rather than two.'''
        super(CTkEntry, self).delete(0, 'end')
        super(CTkEntry, self).insert('end', new_text)

class Helping:
    '''Provides all of the help functions'''

    def __init__(self):
        self.general_help: str = ('ctrl-left-click any item for specific help on that item.\n'
                                 'ctrl-right-click an item for object details.'
                                  )
        self.suffix_message = ('Factor      Name    Symbol  Factor  Name    Symbol\n'
                              '10^30       quetta  Q       10^-30  quecto  q\n'
                              '10^27       ronna   R       10^-27  ronto   r\n'
                              '10^24       yotta   Y       10^-24  yocto   y\n'
                              '10^21       zetta   Z       10^-21  zepto   z\n'
                              '10^18       exa     E       10^-18  atto    a\n'
                              '10^15       peta    P       10^-15  femto   f\n'
                              '10^12       tera    T       10^-12  pico    p\n'
                              '10^9        giga    G       10^-9   nano    n\n'
                              '10^6        mega    M       10^-6   micro   µ\n'
                              '10^3        kilo    k       10^-3   milli   m\n'
                              '10^2        hecto   h       10^-2   centi   c\n'
                              '10^1        deka    da      10^-1   deci    d')

        self.controlkeys_message = ('Control Keys.\n'
                                    'k    - Show this help\n'
                                    'y|q  - quit\n'
                                    'b    - Binary\n'
                                    'c    - Cycle screen layout\n'
                                    'd    - DMS\n'
                                    'e    - Engineering\n'
                                    'f    - Fraction\n'
                                    'h    - Hexadecimal\n'
                                    'o    - Octal\n'
                                    'r    - Roman\n'
                                    's    - Scientific\n'
                                    't    - Transparent toggle\n'
                                    'u    - Suffix mode\n'
                                    'w    - Words\n'
                                    'x    - Sexagesimal\n'
                                    'z    - Restore stack\n'
                                    'Home - Bring window back on screen\n'
                                    '1    - Scientific calculator\n'
                                    '2    - Financial Calculator\n'
                                    '3    - Statistical Calculator\n'
                                    '4    - Unit Converter')

        self.entry_help = ('This box is where keystrokes are added and equations are entered. '
                           '+, -, *, /, ^, % and ! can be entered directly. [Email]\n'
                          '\nComplex Numbers:\n'
                          'Enter complex numbers in brackets, (a+bj).\n'
                          '\nBase Numbers:\n'
                          'Enter a number starting with 0b, 0o, 0d, 0x, &b, &o, &d, &h or enter a number '
                          'followed by _n to enter a base n number. You can use '
                          '_b, _o, _d, _h for binary, octal, decimal and hex. Enter _n to display '
                          'current values as base n.\n'
                          '\nRoman Numbers:\n'
                          'Start with 0r or &r, or follow the roman number with _r, e.g. MCMVII_r or 0rMCMVII. Note '
                          'that Roman numbers aren\'t validated. MMIIVV_r is not a valid Roman number '
                          'but the app will process it as MM = 2000, I = 1, IV = 4, V = 5 giving 2010.\n'
                          'alt digit = digit * 1,000, alt-shift digit = digit * 1,000,000. M=1,000, M\u0305=1,000,00 & M\u033F=1,000,000,000.\n'
                          '\nComments:\n'
                          'Enter a number then # followed by text. e.g 3.1415927#pi. '
                          'Entering #comment, adds the comment to R0.\n'
                          '\nUnits:\n'
                          'Enter a number then @ followed by units separated by spaces. e.g. 23@kg m2 or '
                          '14.66@m-2 kg s3 etc. Entering @units add the units to R0.\n'
                          '\nEquations/Assignments:\n'
                          'An = as the first character implies an equation follows. The equation can '
                          'be stored or evaluated by pressing enter.\n'
                          'An = anywhere else assumes variable assignments. Separate multiple '
                          'assignments with ;. '
                          'e.g. =1+2*3 results in 7. a=22;b=19 defines 2 variables, a and b.\n'
                          '\nVariables:\n'
                          'Variables can be used in equations. Registers R0 thru R5 can also '
                          'be used, they MUST be in upper case, R1 NOT r1. '
                          'To remove a variable, assign a null string to it, e.g. B=\'\'\n'
                           'last use of this')

    def help_about(self) -> None:
        '''Shows the about message.'''
        popup_message.show(title='About', message='Wroten by Kev')

    def show_help(self, help_topic: str = '') -> None:
        '''Show the help for the button clicked.'''

        def format_doc_string(docstring: str) -> str:
            '''Extracts part of the doc string for Help.

            Skips the first line, assumes it is the short description, then
            skips the next line if it is blank.

            Uses the text from this point down to the location of Parameters
            in the docstring. Note, this routine adds the string 'Parameters'
            to the end of the text, in case 'Parameters' has been omitted
            from the docstring.

            Parameters:
                docstring. This is the docstring text from the Function.

            Returns:
                Text to display.
            '''
            if not docstring:
                return "No help for this item yet."
            help_text = docstring + 'Parameters'
            while '  ' in help_text:
                help_text = help_text.replace('  ', ' ')
            start_location = help_text.find('\n') + 1
            if help_text[start_location] == '\n':
                start_location += 1
            end_location = help_text.find('Parameters', start_location + 1) - 2
            if help_text[end_location] == '\n':
                end_location -= 1
            return help_text[start_location:end_location]

        if help_topic is None:
            match_text = ''
        else:
            match_text = help_topic.lower()
        wait: bool = True
        alignment: str = LEFT
        multiline: bool = False
        usetextbox: bool = False
        match match_text:
            case '':
                help_text = 'No Help for this item yet.'
            case 'general':
                help_text = self.general_help + '\n' + self.controlkeys_message
            case '_':
                help_text = ('Used to specify a base number. 23_8 = 23 in base 8.\n'
                             'Valid base numbers range from 2 to 62. You can use b, o, h\n'
                             'for Binary, Octal, and Hex.\n'
                             '_r indicates that a Roman number has been entered, e.g. MCDIV_r is 1404.')
            case 'blank area':
                help_text = 'This is a blank area of the window, no help available'
            case '@':
                help_text = ('Used to append units. 23.6@m2 kg-2. Units/powers must be separated by a '
                             'space, semi-colon or comma.\n44@kg s-2 m, not 44kgs-2m. If 2 or more @ are '
                             'entered, the units will be combined.\n@ and # can be used together, '
                             '23@m3#Comment will generate both a unit and a comment.')
            case '# ':
                help_text = ('Used to add a comment. 3.14159#pi. If 2 or more # are entered, the comments '
                             'will be combined.\n@ and # can be used together, 23#Comment@m3 will generate both '
                             'a comment and a unit.')
            case 'status box':
                help_text = 'Shows current display type, # decimals, base and screen orientation.'
            case 'enter':
                help_text = 'Processes the data in E: or duplicates the top stack item if E: is empty.'
            case 'percent':
                help_text = 'Calculates R0: percent of R1:.'
            case 'percentof':
                help_text = 'Calculates the percent of R0: compared to R1:'
            case 'percentchg':
                help_text = 'Calculates Percent change of R0: compared to R1:.'
            case 'complex':
                help_text = format_doc_string(app.scientific.my_complex.__doc__)
            case 'swap':
                help_text = format_doc_string(app.scientific.swap_stack.__doc__)
            case 'show':
                help_text = format_doc_string(app.scientific.show_stack.__doc__)
            case 'undo':
                help_text = format_doc_string(app.scientific.restore_stack.__doc__)
            case 'clear':
                help_text = format_doc_string(app.scientific.clear_stack.__doc__)
            case 'roll':
                help_text = format_doc_string(app.scientific.roll_stack.__doc__)
            case 'drop':
                help_text = format_doc_string(app.scientific.drop_stack.__doc__)
            case 'cas':
                help_text = format_doc_string(app.scientific.my_cas.__doc__)
            case 'acas':
                help_text = format_doc_string(app.scientific.my_acas.__doc__)
            case 'cash':
                help_text = format_doc_string(app.scientific.my_acash.__doc__)
            case 'acash':
                help_text = format_doc_string(app.scientific.my_cas.__doc__)
            case 'factorial':
                help_text = format_doc_string(app.scientific.my_factorial.__doc__)
            case 'mfactorial':
                help_text = format_doc_string(app.scientific.my_multi_factorial.__doc__)
            case 'subfactorial':
                help_text = format_doc_string(app.scientific.my_subfactorial.__doc__)
            case 'combination':
                help_text = format_doc_string(app.scientific.my_combination.__doc__)
            case 'permutation':
                help_text = format_doc_string(app.scientific.my_permutation.__doc__)
            case 'cubed':
                help_text = format_doc_string(app.scientific.my_cubed.__doc__)
            case 'square':
                help_text = format_doc_string(app.scientific.my_square.__doc__)
            case 'inverse':
                help_text = format_doc_string(app.scientific.my_inverse.__doc__)
            case 'squareroot':
                help_text = format_doc_string(app.scientific.my_sqrt.__doc__)
            case 'power':
                help_text = format_doc_string(app.scientific.my_power.__doc__)
            case 'invpower':
                help_text = format_doc_string(app.scientific.my_inv_power.__doc__)
            case 'log':
                help_text = format_doc_string(app.scientific.my_log_10.__doc__)
            case 'power10':
                help_text = format_doc_string(app.scientific.my_power_10.__doc__)
            case 'ln':
                help_text = format_doc_string(app.scientific.my_log_e.__doc__)
            case 'exp':
                help_text = format_doc_string(app.scientific.my_power_e.__doc__)
            case 'ln2':
                help_text = format_doc_string(app.scientific.my_log_2.__doc__)
            case 'power2':
                help_text = format_doc_string(app.scientific.my_power_2.__doc__)
            case 'rad':
                help_text = format_doc_string(app.scientific.my_radians.__doc__)
            case 'sin':
                help_text = format_doc_string(app.scientific.my_sin.__doc__)
            case 'asin':
                help_text = format_doc_string(app.scientific.my_asin.__doc__)
            case 'sinh':
                help_text = format_doc_string(app.scientific.my_sinh.__doc__)
            case 'cos':
                help_text = format_doc_string(app.scientific.my_cos.__doc__)
            case 'cosh':
                help_text = format_doc_string(app.scientific.my_cosh.__doc__)
            case 'acos':
                help_text = format_doc_string(app.scientific.my_acos.__doc__)
            case 'acosh':
                help_text = format_doc_string(app.scientific.my_acosh.__doc__)
            case 'tan':
                help_text = format_doc_string(app.scientific.my_tan.__doc__)
            case 'atan':
                help_text = format_doc_string(app.scientific.my_atan.__doc__)
            case 'tanh':
                help_text = format_doc_string(app.scientific.my_tanh.__doc__)
            case 'atanh':
                help_text = format_doc_string(app.scientific.my_atanh.__doc__)
            case 'arc':
                help_text = format_doc_string(app.scientific.arc_pressed.__doc__)
            case 'hyp':
                help_text = format_doc_string(app.scientific.hyp_pressed.__doc__)
            case 'rtop':
                help_text = format_doc_string(app.scientific.my_rtop.__doc__)
            case 'ptor':
                help_text = format_doc_string(app.scientific.my_ptor.__doc__)
            case 'vars':
                help_text = format_doc_string(app.scientific.show_variables.__doc__)
            case 'int':
                help_text = format_doc_string(app.scientific.my_int.__doc__)
            case 'dec':
                help_text = format_doc_string(app.scientific.my_dec.__doc__)
            case 'floor':
                help_text = format_doc_string(app.scientific.my_floor.__doc__)
            case 'ceil':
                help_text = format_doc_string(app.scientific.my_ceil.__doc__)
            case 'real':
                help_text = format_doc_string(app.scientific.my_real.__doc__)
            case 'imag':
                help_text = format_doc_string(app.scientific.my_imag.__doc__)
            case 'conj':
                help_text = format_doc_string(app.scientific.my_conj.__doc__)
            case 'fraction':
                help_text = format_doc_string(app.scientific.fraction_format.__doc__)
            case 'show units':
                help_text = format_doc_string(app.converter.show_units.__doc__)
            case 'swap units':
                help_text = format_doc_string(app.converter.swap_units.__doc__)
            case 'Store Equation':
                help_text = format_doc_string(app.scientific.store_equation.__doc__)
            case 'Recall Equation':
                help_text = format_doc_string(app.scientific.recall_equation.__doc__)
            case 'entry box':
                help_text = self.entry_help
                wait = False
                multiline = True
                usetextbox = True
            case 'stack area':
                help_text = 'Shows the current stack values.'
            case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
                help_text = f'Adds the digit {match_text} to the Entry Box.'
            case 'eex':
                help_text = 'Specifies the power of 10. 3.6E3 -> 3,600.'
            case '.':
                help_text = 'Adds a decimal point to the Entry Box.'
            case '+':
                help_text = 'Adds the top 2 items in the stack.'
            case '-':
                help_text = 'Subtracts the value in R0 from R1.'
            case '*':
                help_text = 'Multiplies the value in R0 by R1.'
            case '/':
                help_text = 'Divides the value in R1 by R0.'
            case 'e':
                help_text = 'Inserts the value of e into the R0 register.'
            case 'pi':
                help_text = 'Inserts the value of pi into the R0 register.'
            case 'tau':
                help_text = 'Inserts the value of tau into the R0 register.'
            case 'gm':
                help_text = 'Geometric Mean. (x1 * x2 * x3 ... * xn)**(1/n).'
            case 'hm':
                help_text = 'Harmonic Mean. n / sum( 1 / x).'
            case 'dataentry':
                help_text = 'Enter values separated by spaces, commas or semi-colons.'
            case 'temperature':
                help_text = ('Converts between Celsius (C), Kelvin (K), Fahrenheit (F)'
                            ', Rankine (r) & Reaumur (R).')
            case 'scientific':
                help_text = 'Shows the Scientific calculator.'
            case 'finance':
                help_text = 'Shows the Financial calculator.'
            case 'statistics':
                help_text = 'Shows the Statistics calculator.'
            case 'converter':
                help_text = 'Shows the Converter calculator.'
            case _:
                help_text = f'No Help for {match_text} yet.'
        popup_message.show(title=help_topic, message=help_text, multi_line=multiline, use_text_box = usetextbox,
                           m_height=30, m_width=30, alignment='l', wait=wait, font=('Code New Roman', 13))
        if wait is False and (tb := popup_message.get_textbox()) is not None:
                text_widget_link.add(text_widget=tb, the_text='Complex Numbers:', highlight_name='Complex',
                                 new_text='Complex Numbers',
                                 popup_fg='red', popup_bg='lightgreen', popup_border='purple',
                                 the_link='https://en.wikipedia.org/wiki/Complex_number')
                text_widget_link.add(text_widget=tb, the_text='Base Numbers:', highlight_name='Base', bg_color='gold',
                                 the_link='https://en.wikipedia.org/wiki/Radix')
                text_widget_link.add(text_widget=tb, the_text='Roman Numbers:', highlight_name='Roman',
                                 the_link='https://en.wikipedia.org/wiki/Roman_numerals')
                text_widget_link.add(text_widget=tb, the_text='3.1415927', highlight_name='pi',
                                 the_link='https://en.wikipedia.org/wiki/Pi')
                text_widget_link.add(text_widget=tb, the_text='[Email]', new_text='Email',
                                 popup_font=('Courier New', 18), show_url=False,
                                 highlight_name='email', the_link='mailto:kevin.glentworth@gmail.com')
                text_widget_highlight.add(text_widget=tb, the_text='Comments:', highlight_name='0')
                text_widget_highlight.add(text_widget=tb, the_text='Units:', highlight_name='0')
                text_widget_highlight.add(text_widget=tb, the_text='Equations/Assignments:', highlight_name='0')
                text_widget_highlight.add(text_widget=tb, the_text='Variables:', highlight_name='0')
                text_widget_highlight.add(text_widget=tb, highlight_name='0', fg_color='blue', bg_color='lightyellow',
                                      underline=True, underlinefg='red', italic=True)
                text_widget_highlight.add(text_widget=tb, highlight_name='and', the_text='and', new_text='as well as',
                                      qty=1, fg_color='yellow',bg_color='green', bold=True, relief=RAISED)
                text_widget_highlight.add(text_widget=tb, highlight_name='number', the_text='number', fg_color='blue',
                                      bg_color='lightblue', underline=False, relief=GROOVE)
                text_widget_highlight.add(text_widget=tb, highlight_name='are', the_text='are',
                                      fg_color='blue', bg_color='lightblue', underline=False, relief=SUNKEN, qty=2)
                text_widget_highlight.add(text_widget=tb, highlight_name='enter', the_text='eNTer', superscript=True,
                                      ignore_case=True, fg_color='orange')
                text_widget_highlight.add(text_widget=tb, highlight_name='is', the_text='is', ignore_case=True,
                                       subscript=True, offset=3, fg_color='blue', bg_color='yellow', alpha_adjacent=True)
                app.after(5000, lambda: get_tag_config(tb))
                text_widget_highlight.add(text_widget=tb, highlight_name='black_range', by_position=[22, 100, False], fg_color='black', bold=True)
                app.after(1000, lambda: text_widget_highlight.add(text_widget=tb, highlight_name='green_range', by_position=[22, 200, True], fg_color='green', bold=True))
                app.after(2000, lambda: text_widget_highlight.add(text_widget=tb, highlight_name='orange_range', by_position=[22, 300, False], fg_color='orange', bold=True))
                app.after(3000, lambda: text_widget_highlight.add(text_widget=tb, highlight_name='red_range', by_position=[250, 350, None], fg_color='red', bold=False))


    def formulae_help(self) -> None:
        popup_message.show(title='Formul\u00e6', message='Formulae help.')

    def suffix_help(self) -> None:
        '''Display the suffix help msg.'''
        popup_message.show(title='Suffixes', message=self.suffix_message)

    def controlkeys_help(self) -> None:
        '''Display the suffix help msg.'''
        popup_message.show(title='Control Keys', message=self.controlkeys_message, alignment=LEFT)

    def clicked_help(self, help_subject: str) -> str:
        '''Rather than try to see if the window already exists, try to close it, if it succeeds,
            fine, if it fails, that's fine too as it is not there. Then open the help window.
            '''
        if help_subject == 'SI':
            open_new('https://en.wikipedia.org/wiki/Metric_prefix')
        else:
            try:
                help_subject + 'window'.destroy()
            except:
                pass
            finally:
                eval(f'app.helping.{help_subject}_help()')
        return 'break'  #  terminate event processing

    def some_stuff(self) -> None:
        '''Print various things.'''
        o_str = ''
        o_str += f'I am a {first_bit.what_i_am}, running from {first_bit.my_file_path}\n'
        o_str += f'Me:{currentframe().f_code.co_name}:\n'
        o_str += f'Previous:{currentframe().f_back.f_code.co_name}:\n'
        o_str += f'Version:{version}\n'
        o_str += f'Window dimensions:{app.winfo_width()} {app.winfo_height()}\n'
        o_str += f'Name={self.some_stuff.__name__}\n'
        o_str += f'Qualname={self.some_stuff.__qualname__}\n'
        o_str += f'Module={self.some_stuff.__module__}\n'
        o_str += f'Code={self.some_stuff.__code__}\n'
        o_str += f'Code.stacksize={self.some_stuff.__code__.co_stacksize}\n'
        o_str += f'Code.filename={self.some_stuff.__code__.co_filename}\n'
        o_str += 'BOX DRAWINGS DOUBLE DOWN AND RIGHT=\N{BOX DRAWINGS DOUBLE DOWN AND RIGHT}\n'
        o_str += 'BOX DRAWINGS DOUBLE DOWN AND LEFT=\N{BOX DRAWINGS DOUBLE DOWN AND LEFT}\n'
        o_str += 'BOX DRAWINGS DOUBLE UP AND RIGHT=\N{BOX DRAWINGS DOUBLE UP AND RIGHT}\n'
        o_str += 'BOX DRAWINGS DOUBLE UP AND LEFT=\N{BOX DRAWINGS DOUBLE UP AND LEFT}\n'
        o_str += 'VARIATION SELECTOR-1=\N{VARIATION SELECTOR-1}\n'
        o_str += 'VARIATION SELECTOR-2=\N{VARIATION SELECTOR-2}\n'
        a = [1, 2, 3, 4]
        square = lambda x: x ** 2
        o_str += f'{list(a)}**2={list(map(square, map(square, a)))}\n'
        o_str += f'{app.scientific.my_entry.winfo_x()} {app.scientific.my_entry.winfo_y()}\n'
        o_str += f'{app.scientific.created_vars}\n'
        o_str += f'app screenwidth={app.winfo_screenwidth()}\n'
        o_str += f'app screenheight={app.winfo_screenheight()}\n'
        x, y, cx, cy = app.scientific.my_entry.bbox()
        o_str += f'my_entry.bbox={x} {y} {cx} {cy}\n'
        o_str += '** Range **\n'
        for _1 in range(0, 5):
            o_str += str(_1)
        o_str += '\n'
        o_str += (f'{app.scientific.stack_values[0][0]}='
                  f'{float_to_word(app.scientific.stack_values[0][0], app.scientific.settings_dict['significant_digits'])}\n')
        o_str += f'Menu height={app.winfo_height()}\n'
        o_str += f'Req Menu height={app.winfo_reqheight()}\n'
        o_str += 'IV=4, I\u0305V\u0305=4,000, I\u033FV\u033F=4,000,000\n'
        o_str += f'{Fraction(2, 3)}\n'
        o_str += f'{Fraction(.333)}\n'
        o_str += f'my_username={getuser()}, Host={gethostname().strip()}, IP={gethostbyname(gethostname())}\n'
        o_str += f'{app.scientific.proper(21, 3)}\n'
        o_str += f'{app.scientific.proper(16, 3)}\n'
        o_str += f'{app.scientific.proper(25, 4, ':')}\n'
        o_str += f'{app.scientific.proper((25, 4), sep=':')}\n'
        o_str += f'{app.scientific.proper(-42, 12)}\n'
        o_str += f'{app.scientific.proper(42, -12)}\n'
        o_str += f'{app.scientific.proper((-42, -12))}\n'
        o_str += f'{app.scientific.proper.__name__}\n'
        o_str += ('\N{SUPERSCRIPT ONE}\N{SUPERSCRIPT TWO}\N{SUPERSCRIPT THREE}\N{SUPERSCRIPT FOUR}'
                 '\N{SUPERSCRIPT FIVE}\N{SUPERSCRIPT SIX}\N{SUPERSCRIPT SEVEN}\N{SUPERSCRIPT EIGHT}'
                 '\N{SUPERSCRIPT NINE}\N{SUPERSCRIPT ZERO}\n')
        d = dir()
        for _1 in d:
            if not _1.startswith('__'):
                ev = eval(_1)
                o_str += f'{_1} is {type(ev)} and is equal to {ev}\n'
        o_str += f'BUTTON_HEIGHT ={BUTTON_HEIGHT} BUTTON_WIDTH ={BUTTON_WIDTH}\n'
        o_str += (f'sin: button height ={app.scientific.sin_button.winfo_height()}'
                  f'button width ={app.scientific.sin_button.winfo_width()}\n')
        o_str += (f'cos: button height ={app.scientific.cos_button.winfo_height()}'
                  f'button width ={app.scientific.cos_button.winfo_width()}\n')
        o_str += f'app-w={app.winfo_width()}, app_h={app.winfo_height()}\n'
        o_str += 'app.scientific.__dict__ '
        for dict_item, value in app.scientific.__dict__.items():
            o_str += f'{dict_item}\n'
            if type(value) is list:
                for list_item_0 in value:
                    if type(list_item_0) is list:
                        for list_item_1 in list_item_0:
                            o_str += f'    {list_item_1}\n'
                    else:
                        o_str += f'  {list_item_0}\n'
            else:
                o_str += f'  {value}\n'
        popup_message.show(title='Some stuff', message=o_str, alignment=LEFT, use_text_box=True,
                           multi_line=True, m_height=30, wait=False)


class Scientific:
    '''Scientific calculator'''
    def __init__(self, my_frame):
        self.my_frame = my_frame
        self.arc_status: str = ''
        self.hyp_status: str = ''
        self.radians_conv: int = 1
        self.stack_values: list[float, float, str, {}] = []
        self.redo_stack: list[list[float, float, str, {}], str] = []
        self.redo_counter: int = 0
        self.settings_dict: dict = {}
        self.not_permitted: list[str] = ['e', 'pi', 'tau',
                                         'log', 'log10', 'log2',
                                         'sin', 'cos', 'tan', 'cas',
                                         'asin', 'acos', 'atan', 'acas',
                                         'sinh', 'cosh', 'tanh', 'cash',
                                         'asinh', 'acosh', 'atanh', 'acash',
                                         'int', 'dec', 'ceil', 'floor',
                                         'rtop', 'ptor',
                                         'fact', 'perm', 'comb',
                                         'R0', 'R1', 'R2', 'R3', 'R4', 'R5']
        try:
            my_key = OpenKey(HKEY_CURRENT_USER, r'Software\KevCalc\Scientific')
            key_val = QueryValueEx(my_key, 'created_vars')
            kv = pickle.loads(key_val[0])
            self.created_vars: dict = kv.copy()
            CloseKey(my_key)
        except:
            self.created_vars: dict = {}
        try:
            my_key = OpenKey(HKEY_CURRENT_USER, r'Software\KevCalc\Scientific')
        except:
            my_key = None
        if my_key is not None:
            try:
                key_val = QueryValueEx(my_key, 'stack_values')
                kv = pickle.loads(key_val[0])
                self.stack_values = kv.copy()
            except:
                self.stack_values.append([0.0, 0.0, '', {}])  #  [0]=real part, [1]=imaginary part, [2]=desc, [3]=units
            try:
                key_val = QueryValueEx(my_key, 'redo_stack')
                kv = pickle.loads(key_val[0])
                self.redo_stack = kv.copy()
            except:
                self.redo_stack = []
            try:
                key_val = QueryValueEx(my_key, 'settings_dict')
                kv = pickle.loads(key_val[0])
                self.settings_dict = kv.copy()
            except:
                self.settings_dict: dict = {'significant_digits': 8,
                                            'display_base': 10,
                                            'format_type': self.DisplayFormat.FORMAT_SCI,
                                            'screen_orientation': 'p',
                                            'left': 100,
                                            'top': 100}
                if app.winfo_screenheight() <= app.winfo_screenwidth():
                    self.settings_dict['screen_orientation'] = 'r'
            self.fmtString: str = '{:.' + str(self.settings_dict['significant_digits']) + 'f}'
            try:
                key_val = QueryValueEx(my_key, 'equations')
                kv = pickle.loads(key_val[0])
                self.equations = kv.copy()
            except:
                self.equations = []
        self.fracfmtproper: bool = True
        self.assign_r_vars()
        self.hundreds = ['', 'one', 'two', 'three', 'four', 'five',
                         'six', 'seven', 'eight', 'nine']
        self.tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
                     'seventy', 'eighty', 'ninety']
        self.teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                      'sixteen', 'seventeen', 'eighteen', 'nineteen']
        self.units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.base_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        #  fonts: Code New Roman, Space Mono
        FONT_NAME = 'Code New Roman'
        FONT_SIZE = 19
        self.button_font: CTkFont = CTkFont(family=FONT_NAME, size=FONT_SIZE, weight='normal')
        self.eq_but_font: CTkFont = CTkFont(family=FONT_NAME, size=FONT_SIZE, weight='normal')
        self.text_font: CTkFont = CTkFont(family=FONT_NAME, size=FONT_SIZE, weight='normal')
        self.entry_font: CTkFont = CTkFont(family=FONT_NAME, size=FONT_SIZE - 1, weight='normal')
        self.status_font: CTkFont = CTkFont(family=FONT_NAME, size=FONT_SIZE - 1, weight='normal')

        self.status_box = CTkTextbox(master=self.my_frame,
                                     height=1,
                                     width=400,
                                     pady=0,
                                     padx=0,
                                     corner_radius=0,
                                     border_width=0,
                                     border_spacing=0,
                                     fg_color='thistle',
                                     wrap='none',
                                     font=self.status_font)
        self.status_box.bind('<Control-Button-1>', lambda e: app.ctrl_left_click(e, textstr='Status Box'))
        self.status_box.tag_config('center', justify='center')
        label_config = {'corner_radius': 0,
                        'fg_color': 'lightyellow',
                        'text_color': 'blue',
                        'font': self.text_font}
        reg_label_config = {'corner_radius': 0,
                            'height': 25,
                            'fg_color': 'lightyellow',
                            'font': self.text_font}
        reg_data_config = {'corner_radius': 0,
                           'border_width': 0,
                           'border_spacing': 0,
                           'padx': 0,
                           'pady': 5,
                           'width': ENTRY_WIDTH,
                           'height': 35,
                           'fg_color': 'lightcyan',
                           'text_color': 'blue',
                           'wrap': 'none',
                           'activate_scrollbars': False,
                           'font': self.text_font}
        reg_left_config = {'corner_radius': 0,
                           'width': 8,
                           'fg_color': 'yellow',
                           'padx': 0,
                           'pady': 0,
                           'text': '<'}
        reg_right_config = {'corner_radius': 0,
                            'width': 8,
                            'fg_color': 'yellow',
                            'padx': 0,
                            'pady': 0,
                            'text': '>'}
        self.stack_box_frame = CTkFrame(master=self.my_frame, fg_color='lightyellow')
        self.reg0_label = CTkLabel(self.stack_box_frame, text=' R0:', **reg_label_config)
        self.reg0_left = CTkLabel(self.stack_box_frame, **reg_left_config)
        self.reg0_data = CTkTextbox(self.stack_box_frame, **reg_data_config)
        self.reg0_right = CTkLabel(self.stack_box_frame, **reg_right_config)
        self.reg0_data.insert('0.0', '')
        self.reg0_data.configure(state='disabled')
        self.reg1_label = CTkLabel(self.stack_box_frame, text=' R1:', **reg_label_config)
        self.reg1_left = CTkLabel(self.stack_box_frame, **reg_left_config)
        self.reg1_data = CTkTextbox(self.stack_box_frame, **reg_data_config)
        self.reg1_right = CTkLabel(self.stack_box_frame, **reg_right_config)
        self.reg1_data.insert('0.0', '')
        self.reg1_data.configure(state='disabled')
        self.reg2_label = CTkLabel(self.stack_box_frame, text=' R2:', **reg_label_config)
        self.reg2_left = CTkLabel(self.stack_box_frame, **reg_left_config)
        self.reg2_data = CTkTextbox(self.stack_box_frame, **reg_data_config)
        self.reg2_right = CTkLabel(self.stack_box_frame, **reg_right_config)
        self.reg2_data.insert('0.0', '')
        self.reg2_data.configure(state='disabled')
        self.reg3_label = CTkLabel(self.stack_box_frame, text=' R3:', **reg_label_config)
        self.reg3_left = CTkLabel(self.stack_box_frame, **reg_left_config)
        self.reg3_data = CTkTextbox(self.stack_box_frame, **reg_data_config)
        self.reg3_right = CTkLabel(self.stack_box_frame, **reg_right_config)
        self.reg3_data.insert('0.0', '')
        self.reg3_data.configure(state='disabled')
        self.reg4_label = CTkLabel(self.stack_box_frame, text=' R4:', **reg_label_config)
        self.reg4_left = CTkLabel(self.stack_box_frame, **reg_left_config)
        self.reg4_data = CTkTextbox(self.stack_box_frame, **reg_data_config)
        self.reg4_right = CTkLabel(self.stack_box_frame, **reg_right_config)
        self.reg4_data.insert('0.0', '')
        self.reg4_data.configure(state='disabled')
        self.reg5_label = CTkLabel(self.stack_box_frame, text=' R5:', **reg_label_config)
        self.reg5_left = CTkLabel(self.stack_box_frame, **reg_left_config)
        self.reg5_data = CTkTextbox(self.stack_box_frame, **reg_data_config)
        self.reg5_right = CTkLabel(self.stack_box_frame, **reg_right_config)
        self.reg5_data.insert('0.0', '')
        self.reg5_data.configure(state='disabled')
        self.reg0_data.bind('<MouseWheel>', self.mouse_wheel)
        self.reg1_data.bind('<MouseWheel>', self.mouse_wheel)
        self.reg2_data.bind('<MouseWheel>', self.mouse_wheel)
        self.reg3_data.bind('<MouseWheel>', self.mouse_wheel)
        self.reg4_data.bind('<MouseWheel>', self.mouse_wheel)
        self.reg5_data.bind('<MouseWheel>', self.mouse_wheel)
        self.reg0_left.bind('<Button-1>', self.left_mouse_0)
        self.reg0_right.bind('<Button-1>', self.right_mouse_0)
        self.reg1_left.bind('<Button-1>', self.left_mouse_1)
        self.reg1_right.bind('<Button-1>', self.right_mouse_1)
        self.reg2_left.bind('<Button-1>', self.left_mouse_2)
        self.reg2_right.bind('<Button-1>', self.right_mouse_2)
        self.reg3_left.bind('<Button-1>', self.left_mouse_3)
        self.reg3_right.bind('<Button-1>', self.right_mouse_3)
        self.reg4_left.bind('<Button-1>', self.left_mouse_4)
        self.reg4_right.bind('<Button-1>', self.right_mouse_4)
        self.reg5_left.bind('<Button-1>', self.left_mouse_5)
        self.reg5_right.bind('<Button-1>', self.right_mouse_5)
        self.reg0_data.bind('<Control-Button-1>', lambda e: app.ctrl_left_click(e, textstr='Stack Area'))
        self.reg1_data.bind('<Control-Button-1>', lambda e: app.ctrl_left_click(e, textstr='Stack Area'))
        self.reg2_data.bind('<Control-Button-1>', lambda e: app.ctrl_left_click(e, textstr='Stack Area'))
        self.reg3_data.bind('<Control-Button-1>', lambda e: app.ctrl_left_click(e, textstr='Stack Area'))
        self.reg4_data.bind('<Control-Button-1>', lambda e: app.ctrl_left_click(e, textstr='Stack Area'))
        self.reg5_data.bind('<Control-Button-1>', lambda e: app.ctrl_left_click(e, textstr='Stack Area'))
        self.reg0_data.bind('<Button-3>', lambda e: self.right_click(e, '0'))
        self.reg1_data.bind('<Button-3>', lambda e: self.right_click(e, '1'))
        self.reg2_data.bind('<Button-3>', lambda e: self.right_click(e, '2'))
        self.reg3_data.bind('<Button-3>', lambda e: self.right_click(e, '3'))
        self.reg4_data.bind('<Button-3>', lambda e: self.right_click(e, '4'))
        self.reg5_data.bind('<Button-3>', lambda e: self.right_click(e, '5'))

        self.my_entry_frame = CTkFrame(self.my_frame)
        self.my_entry_label = CTkLabel(self.my_entry_frame,
                                       corner_radius=0,
                                       text=' E: ',
                                       fg_color='lightyellow',
                                       text_color='blue',
                                       font=self.text_font)
        self.my_entry = CTkEntry(master=self.my_entry_frame,
                                 corner_radius=0,
                                 width=ENTRY_WIDTH,
                                 fg_color='pink',
                                 bg_color='yellow',
                                 font=self.entry_font)
        if my_key is not None:
            try:
                key_val = QueryValueEx(my_key, 'entry_box')
                self.my_entry.insert(0, key_val[0])
            except:
                pass
        if my_key is not None:
            CloseKey(my_key)
        self.my_entry.bind('<Return>', (lambda event: self.my_enter()))
        self.my_entry.bind('?', (lambda event: app.ctrl_left_click(e, 'Entry Box')))
        self.my_entry.bind('+', (lambda event: self.pressed_op('+', event)))
        self.my_entry.bind('-', (lambda event: self.pressed_op('-', event)))
        self.my_entry.bind('*', (lambda event: self.pressed_op('*', event)))
        self.my_entry.bind('/', (lambda event: self.pressed_op('/', event)))
        self.my_entry.bind('^', (lambda event: self.pressed_op('^', event)))
        self.my_entry.bind('!', (lambda event: self.pressed_op('!', event)))
        self.my_entry.bind('%', (lambda event: self.pressed_op('%', event)))
        #  \u0305 represents overstrike. This is for roman numeral x 1,000
        self.my_entry.bind("<Alt-m>", lambda event: self.my_entry.insert(INSERT, 'M\u0305'))
        self.my_entry.bind("<Alt-M>", lambda event: self.my_entry.insert(INSERT, 'M\u0305'))
        self.my_entry.bind("<Alt-d>", lambda event: self.my_entry.insert(INSERT, 'D\u0305'))
        self.my_entry.bind("<Alt-D>", lambda event: self.my_entry.insert(INSERT, 'D\u0305'))
        self.my_entry.bind("<Alt-c>", lambda event: self.my_entry.insert(INSERT, 'C\u0305'))
        self.my_entry.bind("<Alt-C>", lambda event: self.my_entry.insert(INSERT, 'C\u0305'))
        self.my_entry.bind("<Alt-l>", lambda event: self.my_entry.insert(INSERT, 'L\u0305'))
        self.my_entry.bind("<Alt-L>", lambda event: self.my_entry.insert(INSERT, 'L\u0305'))
        self.my_entry.bind("<Alt-x>", lambda event: self.my_entry.insert(INSERT, 'X\u0305'))
        self.my_entry.bind("<Alt-X>", lambda event: self.my_entry.insert(INSERT, 'X\u0305'))
        self.my_entry.bind("<Alt-v>", lambda event: self.my_entry.insert(INSERT, 'V\u0305'))
        self.my_entry.bind("<Alt-V>", lambda event: self.my_entry.insert(INSERT, 'V\u0305'))
        self.my_entry.bind("<Alt-i>", lambda event: self.my_entry.insert(INSERT, 'I\u0305'))
        self.my_entry.bind("<Alt-I>", lambda event: self.my_entry.insert(INSERT, 'I\u0305'))
        #  \u033F represents double overstrike. This is for roman numeral x 1,000,000
        self.my_entry.bind("<Alt-Shift-m>", lambda event: self.my_entry.insert(INSERT, 'M\u033F'))
        self.my_entry.bind("<Alt-Shift-M>", lambda event: self.my_entry.insert(INSERT, 'M\u033F'))
        self.my_entry.bind("<Alt-Shift-d>", lambda event: self.my_entry.insert(INSERT, 'D\u033F'))
        self.my_entry.bind("<Alt-Shift-D>", lambda event: self.my_entry.insert(INSERT, 'D\u033F'))
        self.my_entry.bind("<Alt-Shift-c>", lambda event: self.my_entry.insert(INSERT, 'C\u033F'))
        self.my_entry.bind("<Alt-Shift-C>", lambda event: self.my_entry.insert(INSERT, 'C\u033F'))
        self.my_entry.bind("<Alt-Shift-l>", lambda event: self.my_entry.insert(INSERT, 'L\u033F'))
        self.my_entry.bind("<Alt-Shift-L>", lambda event: self.my_entry.insert(INSERT, 'L\u033F'))
        self.my_entry.bind("<Alt-Shift-x>", lambda event: self.my_entry.insert(INSERT, 'X\u033F'))
        self.my_entry.bind("<Alt-Shift-X>", lambda event: self.my_entry.insert(INSERT, 'X\u033F'))
        self.my_entry.bind("<Alt-Shift-v>", lambda event: self.my_entry.insert(INSERT, 'V\u033F'))
        self.my_entry.bind("<Alt-Shift-V>", lambda event: self.my_entry.insert(INSERT, 'V\u033F'))
        self.my_entry.bind("<Alt-Shift-i>", lambda event: self.my_entry.insert(INSERT, 'I\u033F'))
        self.my_entry.bind("<Alt-Shift-I>", lambda event: self.my_entry.insert(INSERT, 'I\u033F'))
        self.my_entry.bind('<Down>', (lambda event: self.roll_stack()))
        self.my_entry.bind('<Up>', (lambda event: self.roll_stack(1)))
        self.my_entry.bind('<Control-Button-1>', lambda e: app.ctrl_left_click(e, 'Entry Box'))
        help_text = app.helping.entry_help
        button_config = {'corner_radius': 0,
                         'width': BUTTON_WIDTH,
                         'height': BUTTON_HEIGHT,
                         'border_width': 1,
                         'border_spacing': 0,
                         'hover_color': 'lightyellow',
                         'fg_color': 'silver',
                         'text_color': 'blue',
                         'border_color': 'blue',
                         'background_corner_colors': ('white',
                                                      'white',
                                                      'white',
                                                      'white'),
                         'font': self.button_font}
        self.drop_button = CTkButton(master=self.my_frame,
                                     text='drop',
                                     command=self.drop_stack,
                                     **button_config)
        self.bind_an_object(self.drop_button, 'Drop')
        self.swap_button = CTkButton(master=self.my_frame,
                                     text='swap',
                                     command=self.swap_stack,
                                     **button_config)
        self.bind_an_object(self.swap_button, 'Swap')
        self.roll_button = CTkButton(master=self.my_frame,
                                     text='roll',
                                     command=self.roll_stack,
                                     **button_config)
        self.bind_an_object(self.roll_button, 'Roll')
        self.stack_button = CTkButton(master=self.my_frame,
                                      text='show',
                                      command=self.show_stack,
                                      **button_config)
        self.bind_an_object(self.stack_button, 'Show')
        self.undo_button = CTkButton(master=self.my_frame,
                                     text='undo',
                                     command=self.restore_stack,
                                     **button_config)
        self.bind_an_object(self.undo_button, 'Undo')
        self.clear_button = CTkButton(master=self.my_frame,
                                      text='clear',
                                      command=self.clear_stack,
                                      **button_config)
        self.bind_an_object(self.clear_button, 'Clear')
        button_config = {'corner_radius': 0,
                         'width': BUTTON_WIDTH,
                         'height': BUTTON_HEIGHT,
                         'border_width': 1,
                         'border_spacing': 0,
                         'hover_color': 'lightyellow',
                         'fg_color': 'lavender',
                         'text_color': 'blue',
                         'border_color': 'blue',
                         'background_corner_colors': ('white',
                                                      'white',
                                                      'white',
                                                      'white'),
                         'font': self.button_font}
        self.square_button = CTkButton(master=self.my_frame,
                                       text='x\u00b2',
                                       command=self.my_square,
                                       **button_config)
        self.bind_an_object(self.square_button, 'Square')
        self.root_button = CTkButton(master=self.my_frame,
                                     text='\u221a',
                                     command=self.my_sqrt,
                                     **button_config)
        self.bind_an_object(self.root_button, 'SquareRoot')
        self.inverse_button = CTkButton(master=self.my_frame,
                                        text=' 1/x ',
                                        command=self.my_inverse,
                                        **button_config)
        self.bind_an_object(self.inverse_button, 'Inverse')
        self.cubed_button = CTkButton(master=self.my_frame,
                                      text=' x³ ',
                                      command=self.my_cubed,
                                      **button_config)
        self.bind_an_object(self.cubed_button, 'Cubed')
        self.power_button = CTkButton(master=self.my_frame,
                                      text=' y\u02E3 ',
                                      command=self.my_power,
                                      **button_config)
        self.bind_an_object(self.power_button, 'Power')
        self.inv_power_button = CTkButton(master=self.my_frame,
                                          text='y\u00B9\u2044x',
                                          command=self.my_inv_power,
                                          **button_config)
        self.bind_an_object(self.inv_power_button, 'InvPower')

        self.log_button = CTkButton(master=self.my_frame,
                                    text='log10', # \u2081\u2080',
                                    command=self.my_log_10,
                                    **button_config)
        self.bind_an_object(self.log_button, 'Log')
        self.power10_button = CTkButton(master=self.my_frame,
                                        text=' 10\u02E3 ',
                                        command=self.my_power_10,
                                        **button_config)
        self.bind_an_object(self.power10_button, 'Power10')
        self.ln_button = CTkButton(master=self.my_frame,
                                   text='loge', # \u2091',
                                   command=self.my_log_e,
                                   **button_config)
        self.bind_an_object(self.ln_button, 'ln')
        self.exp_button = CTkButton(master=self.my_frame,
                                    text=' e\u02E3 ',
                                    command=self.my_power_e,
                                    **button_config)
        self.bind_an_object(self.exp_button, 'exp')
        self.ln2_button = CTkButton(master=self.my_frame,
                                    text='log2', # 'log\u2082',
                                    command=self.my_log_2,
                                    **button_config)
        self.bind_an_object(self.ln2_button, 'ln2')
        self.exp2_button = CTkButton(master=self.my_frame,
                                     text=' 2\u02E3 ',
                                     command=self.my_power_2,
                                     **button_config)
        self.bind_an_object(self.exp2_button, 'power2')

        button_config = {'corner_radius': 0,
                         'width': BUTTON_WIDTH,
                         'height': BUTTON_HEIGHT,
                         'border_width': 1,
                         'border_spacing': 0,
                         'hover_color': 'lightyellow',
                         'fg_color': 'PaleGreen1',
                         'text_color': 'blue',
                         'border_color': 'green',
                         'background_corner_colors': ('white',
                                                      'white',
                                                      'white',
                                                      'white'),
                         'font': self.button_font}
        self.comb_button = CTkButton(master=self.my_frame,
                                     text='nCr',
                                     command=self.my_combination,
                                     **button_config)
        self.bind_an_object(self.comb_button, 'Combination')
        self.perm_button = CTkButton(master=self.my_frame,
                                     text='nPr',
                                     command=self.my_permutation,
                                     **button_config)
        self.bind_an_object(self.perm_button, 'Permutation')
        self.fact_button = CTkButton(master=self.my_frame,
                                     text='n!',
                                     command=self.my_factorial,
                                     **button_config)
        self.bind_an_object(self.fact_button, 'Factorial')
        self.mfact_button = CTkButton(master=self.my_frame,
                                      text='n!!',
                                      command=self.my_multi_factorial,
                                      **button_config)
        self.bind_an_object(self.mfact_button, 'MFactorial')
        self.subfactorial_button = CTkButton(master=self.my_frame,
                                             text='!n (n\u00A1)',
                                             command=self.my_subfactorial,
                                             **button_config)
        self.bind_an_object(self.subfactorial_button, 'subfactorial')

        button_config = {'corner_radius': 0,
                         'width': BUTTON_WIDTH,
                         'height': BUTTON_HEIGHT,
                         'border_width': 1,
                         'border_spacing': 0,
                         'hover_color': 'lightyellow',
                         'fg_color': 'sky blue',
                         'text_color': 'blue',
                         'border_color': 'green',
                         'background_corner_colors': ('white',
                                                      'white',
                                                      'white',
                                                      'white'),
                         'font': self.button_font}
        self.arc_button = CTkButton(master=self.my_frame,
                                    text='arc',
                                    command=self.arc_pressed,
                                    **button_config)
        self.bind_an_object(self.arc_button, 'arc')
        self.hyp_button = CTkButton(master=self.my_frame,
                                    text='hyp',
                                    command=self.hyp_pressed,
                                    **button_config)
        self.bind_an_object(self.hyp_button, 'hyp')
        self.sin_button = CTkButton(master=self.my_frame,
                                    text='sin',
                                    command=lambda: self.trig_functions(self.sin_button.cget('text')),
                                    **button_config)

        self.bind_an_object(self.sin_button, '')
        self.cos_button = CTkButton(master=self.my_frame,
                                    text='cos',
                                    command=lambda: self.trig_functions(self.cos_button.cget('text')),
                                    **button_config)
        self.bind_an_object(self.cos_button, '')
        self.tan_button = CTkButton(master=self.my_frame,
                                    text='tan',
                                    command=lambda: self.trig_functions(self.tan_button.cget('text')),
                                    **button_config)
        self.bind_an_object(self.tan_button, '')
        self.cas_button = CTkButton(master=self.my_frame,
                                    text='cas',
                                    command=lambda: self.trig_functions(self.cas_button.cget('text')),
                                    **button_config)
        self.bind_an_object(self.cas_button, '')
        self.radians_button = CTkButton(master=self.my_frame,
                                        text='rad',
                                        command=self.my_radians,
                                        **button_config)
        self.bind_an_object(self.radians_button, 'rad')
        button_config = {'corner_radius': 0,
                         'width': BUTTON_WIDTH,
                         'height': BUTTON_HEIGHT,
                         'border_width': 1,
                         'border_spacing': 0,
                         'hover_color': 'lightyellow',
                         'fg_color': 'plum',
                         'text_color': 'blue',
                         'border_color': 'green',
                         'background_corner_colors': ('white',
                                                      'white',
                                                      'white',
                                                      'white'),
                         'font': self.button_font}
        self.var_button = CTkButton(master=self.my_frame,
                                    text='vars',
                                    command=self.show_variables,
                                    **button_config)
        self.bind_an_object(self.var_button, 'vars')

        button_config = {'corner_radius': 0,
                         'width': BUTTON_WIDTH,
                         'height': BUTTON_HEIGHT,
                         'border_width': 1,
                         'border_spacing': 0,
                         'hover_color': 'lightyellow',
                         'fg_color': 'thistle',
                         'text_color': 'blue',
                         'border_color': 'green',
                         'background_corner_colors': ('white',
                                                      'white',
                                                      'white',
                                                      'white'),
                         'font': self.eq_but_font}
        self.store_button = CTkButton(master=self.my_frame,
                                      text='eq stor',
                                      command=self.store_equation,
                                      **button_config,
                                      )
        self.bind_an_object(self.store_button, 'Store Equation')
        self.recall_button = CTkButton(master=self.my_frame,
                                       text='eq rcl',
                                       command=self.recall_equation,
                                       **button_config,
                                       )
        self.bind_an_object(self.recall_button, 'Recall Equation')
        button_config = {'corner_radius': 0,
                         'width': BUTTON_WIDTH * 0.8,
                         'height': BUTTON_HEIGHT,
                         'border_width': 1,
                         'border_spacing': 0,
                         'hover_color': 'lightyellow',
                         'fg_color': 'sandybrown',
                         'text_color': 'blue',
                         'border_color': 'green',
                         'background_corner_colors': ('white',
                                                      'white',
                                                      'white',
                                                      'white'),
                         'font': self.button_font}
        self.e_button = CTkButton(master=self.my_frame,
                                  text='e',
                                  command=lambda: self.insert_constant(e),
                                  **button_config,
                                  )
        self.bind_an_object(self.e_button, 'e')
        self.pi_button = CTkButton(master=self.my_frame,
                                   text='  \u03C0  ',
                                   command=lambda: self.insert_constant(pi),
                                   **button_config)
        self.bind_an_object(self.pi_button, 'pi')
        self.tau_button = CTkButton(master=self.my_frame,
                                    text='  \u03C4  ',
                                    command=lambda: self.insert_constant(tau),
                                    **button_config)
        self.bind_an_object(self.tau_button, 'tau')
        button_config = {'corner_radius': 0,
                         'width': BUTTON_WIDTH,
                         'height': BUTTON_HEIGHT,
                         'border_width': 1,
                         'border_spacing': 0,
                         'hover_color': 'lightyellow',
                         'fg_color': 'paleturquoise',
                         'text_color': 'blue',
                         'border_color': 'green',
                         'background_corner_colors': ('white',
                                                      'white',
                                                      'white',
                                                      'white'),
                         'font': self.button_font}
        self.int_button = CTkButton(master=self.my_frame,
                                    text='int',
                                    command=self.my_int,
                                    **button_config)
        self.bind_an_object(self.int_button, 'int')
        self.dec_button = CTkButton(master=self.my_frame,
                                    text='dec',
                                    command=self.my_dec,
                                    **button_config)
        self.bind_an_object(self.dec_button, 'dec')
        self.real_button = CTkButton(master=self.my_frame,
                                    text='real',
                                    command=self.my_real,
                                    **button_config)
        self.bind_an_object(self.real_button, 'real')
        self.imag_button = CTkButton(master=self.my_frame,
                                    text='imag',
                                    command=self.my_imag,
                                    **button_config)
        self.bind_an_object(self.imag_button, 'imag')
        self.conj_button = CTkButton(master=self.my_frame,
                                    text='conj',
                                    command=self.my_conj,
                                    **button_config)
        self.bind_an_object(self.conj_button, 'conj')
        self.complex_button = CTkButton(master=self.my_frame,
                                        text='complex',
                                        command=self.my_complex,
                                        **button_config)
        self.bind_an_object(self.complex_button, 'complex')
        self.ceil_button = CTkButton(master=self.my_frame,
                                     text='ceil',
                                     command=self.my_ceil,
                                     **button_config)
        self.bind_an_object(self.ceil_button, 'ceil')
        self.floor_button = CTkButton(master=self.my_frame,
                                      text='floor',
                                      command=self.my_floor,
                                      **button_config)
        self.bind_an_object(self.floor_button, 'floor')
        self.rtop_button = CTkButton(master=self.my_frame,
                                     text='R\u21feP',
                                     command=self.my_rtop,
                                     **button_config)
        self.bind_an_object(self.rtop_button, 'rtop')
        self.ptor_button = CTkButton(master=self.my_frame,
                                     text='P\u21feR',
                                     command=self.my_ptor,
                                     **button_config)
        self.bind_an_object(self.ptor_button, 'ptor')

        button_config = {'corner_radius': 0,
                         'width': BUTTON_WIDTH,
                         'height': BUTTON_HEIGHT,
                         'border_width': 1,
                         'border_spacing': 0,
                         'hover_color': 'aquamarine',
                         'fg_color': 'peachpuff',
                         'text_color': 'blue',
                         'border_color': 'red',
                         'background_corner_colors': ('white',
                                                      'white',
                                                      'white',
                                                      'white'),
                         'font': self.button_font}
        self._7_button = CTkButton(master=self.my_frame,
                                   text=' 7 ',
                                   command=lambda: self.clicked_it('7'),
                                   **button_config)
        self.bind_an_object(self._7_button, '7')
        self._8_button = CTkButton(master=self.my_frame,
                                   text=' 8 ',
                                   command=lambda: self.clicked_it('8'),
                                   **button_config)
        self.bind_an_object(self._8_button, '8')
        self._9_button = CTkButton(master=self.my_frame,
                                   text=' 9 ',
                                   command=lambda: self.clicked_it('9'),
                                   **button_config)
        self.bind_an_object(self._9_button, '9')
        self.divide_button = CTkButton(master=self.my_frame,
                                       text=' / ',
                                       command=self.my_divide,
                                       **button_config)
        self.bind_an_object(self.divide_button, '/')
        self.chgsgn_button = CTkButton(master=self.my_frame,
                                       text=' \u00B1 ',
                                       command=self.my_change_sign,
                                       **button_config)
        self.bind_an_object(self.chgsgn_button, 'Change Sign')
        self.fraction_button = CTkButton(master=self.my_frame,
                                         text='a_b/c',
                                         command=self.fraction_format,
                                         **button_config)
        self.bind_an_object(self.fraction_button, 'Fraction')

        self._4_button = CTkButton(master=self.my_frame,
                                   text=' 4 ',
                                   command=lambda: self.clicked_it('4'),
                                   **button_config)
        self.bind_an_object(self._4_button, '4')
        self._5_button = CTkButton(master=self.my_frame,
                                   text=' 5 ',
                                   command=lambda: self.clicked_it('5'),
                                   **button_config)
        self.bind_an_object(self._5_button, '5')
        self._6_button = CTkButton(master=self.my_frame,
                                   text=' 6 ',
                                   command=lambda: self.clicked_it('6'),
                                   **button_config)
        self.bind_an_object(self._6_button, '6')
        self.multiply_button = CTkButton(master=self.my_frame,
                                         text=' \u2736 ',
                                         command=self.my_multiply,
                                         **button_config)
        self.bind_an_object(self.multiply_button, '*')
        self.uscore_button = CTkButton(master=self.my_frame,
                                       text=' _ ',
                                       command=lambda: self.clicked_it('_'),
                                       **button_config)
        self.bind_an_object(self.uscore_button, '_')
        self.athash_frame = CTkFrame(self.my_frame, width=BUTTON_WIDTH)
        button_config_1 = {'corner_radius': 0,
                           'width': BUTTON_WIDTH / 2,
                           'height': BUTTON_HEIGHT,
                           'border_width': 1,
                           'border_spacing': 0,
                           'hover_color': 'aquamarine',
                           'fg_color': 'peachpuff',
                           'text_color': 'blue',
                           'border_color': 'red',
                           'background_corner_colors': ('white',
                                                        'white',
                                                        'white',
                                                        'white'),
                           'font': self.button_font}
        self.at_button = CTkButton(master=self.athash_frame,
                                   text=' @ ',
                                   command=lambda: self.clicked_it('@'),
                                   **button_config_1)
        self.bind_an_object(self.at_button, '@')
        self.hash_button = CTkButton(master=self.athash_frame,
                                     text=' #  ',
                                     command=lambda: self.clicked_it('# '),
                                     **button_config_1)
        self.bind_an_object(self.hash_button, '# ')
        self.percent_button = CTkButton(master=self.my_frame,
                                        text=' % ',
                                        command=self.my_percent,
                                        **button_config)
        self.bind_an_object(self.percent_button, 'Percent')

        self._1_button = CTkButton(master=self.my_frame,
                                   text=' 1 ',
                                   command=lambda: self.clicked_it('1'),
                                   **button_config)
        self.bind_an_object(self._1_button, '1')
        self._2_button = CTkButton(master=self.my_frame,
                                   text=' 2 ',
                                   command=lambda: self.clicked_it('2'),
                                   **button_config)
        self.bind_an_object(self._2_button, '2')
        self._3_button = CTkButton(master=self.my_frame,
                                   text=' 3 ',
                                   command=lambda: self.clicked_it('3'),
                                   **button_config)
        self.bind_an_object(self._3_button, '3')
        self.minus_button = CTkButton(master=self.my_frame,
                                      text=' - ',
                                      command=self.my_subtract,
                                      **button_config)
        self.bind_an_object(self.minus_button, '-')
        self.percentof_button = CTkButton(master=self.my_frame,
                                          text='% of',
                                          command=self.my_percent_of,
                                          **button_config)
        self.bind_an_object(self.percentof_button, 'Percentof')

        self._0_button = CTkButton(master=self.my_frame,
                                   text=' 0 ',
                                   command=lambda: self.clicked_it('0'),
                                   **button_config)
        self.bind_an_object(self._0_button, '0')
        self.dot_button = CTkButton(master=self.my_frame,
                                    text=' . ',
                                    command=lambda: self.clicked_it('.'),
                                    **button_config)
        self.bind_an_object(self.dot_button, '.')
        self.eex_button = CTkButton(master=self.my_frame,
                                    text='Eex',
                                    command=lambda: self.clicked_it('E'),
                                    **button_config)
        self.bind_an_object(self.eex_button, 'eex')
        self.add_button = CTkButton(master=self.my_frame,
                                    text=' + ',
                                    command=self.my_add,
                                    **button_config)
        self.bind_an_object(self.add_button, '+')
        self.enter_button = CTkButton(master=self.my_frame,
                                      text='enter',
                                      command=self.my_enter,
                                      **button_config)
        self.bind_an_object(self.enter_button, 'enter')
        self.percentchg_button = CTkButton(master=self.my_frame,
                                           text=' \u0394% ',
                                           command=self.my_percentchg,
                                           **button_config)
        self.bind_an_object(self.percentchg_button, 'Percentchg')
        self.set_format(self.settings_dict['format_type'])
        self.popup_clear_menu = Menu(self.my_frame, tearoff=0, font=self.text_font)
        self.popup_clear_menu.add_command(label='Clear stack', command=lambda: self.clear_menu_actions('cs'))
        self.popup_clear_menu.add_command(label='Clear comments', command=lambda: self.clear_menu_actions('cc'))
        self.popup_clear_menu.add_command(label='Clear units', command=lambda: self.clear_menu_actions('cu'))
        self.popup_clear_menu.add_command(label='Clear imaginary parts', command=lambda: self.clear_menu_actions('ci'))
        self.popup_clear_menu.add_command(label='Clear variables', command=lambda: self.clear_menu_actions('cv'))
        self.popup_clear_menu.add_command(label='Clear equations', command=lambda: self.clear_menu_actions('ce'))
        self.popup_clear_menu.add_command(label='Exit', command=None)
        #app.withdraw()
        #print('withdraw')
        match self.settings_dict['screen_orientation']:
            case 'l':
                self.arrange_landscape_left()
            case 'r':
                self.arrange_landscape_right()
            case 'p':
                self.arrange_portrait()
        #app.after(500, lambda: (print('deiconify', app.deiconify())))
        self.display_stack()


    def ctrl_right_click(self, event, object: CTkButton = None):
        out_str: str = ''
        out_str += str(object) + '\n'
        out_str += 'name=' + object.winfo_name() + '\n'
        out_str += 'bbox=' + str(object.bbox()) + '\n'
        out_str += 'geometry=' + object.winfo_geometry() + '\n'
        children = object.winfo_children()
        for child in children:
            out_str += 'childname=' + child.winfo_name() + '\n'
            out_str += 'geometry=' + child.winfo_geometry() + '\n'
            if child.winfo_name() == '!label':
                out_str += 'label=' + child.cget('text') + '\n'
        popup_message.show(title='Button Info', message=out_str)


    def right_click(self, event, item):
        print('right-click', item)


    def bind_an_object(self, object_name: Any, object_label: str=''):
        object_name.bind('<Control-Button-1>', lambda e: app.ctrl_left_click(e, object_label))
        object_name.bind('<Control-Button-3>', lambda e: self.ctrl_right_click(e, object_name))


    def arrange_stack_box(self) -> None:
        '''Layout for the stack box.'''
        label_row = 0
        label_column = -1
        self.reg5_label.grid(row=label_row, column=(label_column := label_column + 1))
        self.reg5_left.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg5_data.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg5_right.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        label_row += 1
        label_column = -1
        self.reg4_label.grid(row=label_row, column=(label_column := label_column + 1))
        self.reg4_left.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg4_data.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg4_right.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        label_row += 1
        label_column = -1
        self.reg3_label.grid(row=label_row, column=(label_column := label_column + 1))
        self.reg3_left.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg3_data.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg3_right.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        label_row += 1
        label_column = -1
        self.reg2_label.grid(row=label_row, column=(label_column := label_column + 1))
        self.reg2_left.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg2_data.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg2_right.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        label_row += 1
        label_column = -1
        self.reg1_label.grid(row=label_row, column=(label_column := label_column + 1))
        self.reg1_left.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg1_data.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg1_right.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        label_row += 1
        label_column = -1
        self.reg0_label.grid(row=label_row, column=(label_column := label_column + 1))
        self.reg0_left.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg0_data.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')
        self.reg0_right.grid(row=label_row, column=(label_column := label_column + 1), sticky='news')

    def arrange_portrait(self):
        '''Arrange buttons etc in portrait.'''
        app.resizable(True, True)
        button_row = 0
        self.status_box.grid(row=button_row, column=0, columnspan=6)

        button_row += 1
        self.stack_box_frame.grid(row=button_row, column=0, columnspan=6, sticky='news')
        self.arrange_stack_box()

        button_row += 1
        self.my_entry_frame.grid(row=button_row, column=0, columnspan=6)
        self.my_entry['font'] = ('Roboto Mono Medium', '10')
        self.my_entry_label.grid(row=0, column=0)
        self.my_entry.grid(row=0, column=1, sticky='news')

        button_row += 1
        i_column = -1
        self.drop_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.swap_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.roll_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.stack_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.undo_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.clear_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.real_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.imag_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.conj_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.complex_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.square_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.root_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.inverse_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.cubed_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.power_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.inv_power_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.log_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.power10_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ln_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.exp_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ln2_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.exp2_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.comb_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.perm_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.fact_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.mfact_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.subfactorial_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.var_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.sin_button.grid(row=button_row, column=0, sticky='news')
        self.cos_button.grid(row=button_row, column=1, sticky='news')
        self.tan_button.grid(row=button_row, column=2, sticky='news')
        self.cas_button.grid(row=button_row, column=3, sticky='news')
        self.store_button.grid(row=button_row, column=4, sticky='news')
        self.recall_button.grid(row=button_row, column=5, sticky='news')

        button_row += 1
        i_column = -1
        self.radians_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.arc_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.hyp_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.e_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.pi_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.tau_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.int_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.dec_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ceil_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.floor_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.rtop_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ptor_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self._7_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._8_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._9_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.divide_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.chgsgn_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.fraction_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self._4_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._5_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._6_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.multiply_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.uscore_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.percent_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self._1_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._2_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._3_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.minus_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.athash_frame.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.at_button.pack(side=LEFT, fill='x', expand=True)
        self.hash_button.pack(side=RIGHT, fill='x', expand=True)
        self.percentof_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self._0_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.dot_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.eex_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.add_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.enter_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.percentchg_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.my_frame.forget()
        self.my_frame.pack()
        app.update_idletasks()
        app.resizable(False, False)
        app.geometry(f'+{self.settings_dict['left']}+{self.settings_dict['top']}')
        retrieve_object(app, 4000, 2000) # If offscreen, brings it back.
        self.settings_dict['screen_orientation'] = 'p'
        self.update_status_box()

    def arrange_landscape_left(self):
        '''Arrange buttons etc in landscape with keypad on the left.'''
        app.resizable(True, True)
        button_row = 0
        self.status_box.grid(row=button_row, column=0, columnspan=6)

        button_row += 1
        self.stack_box_frame.grid(row=button_row, column=0, columnspan=6, sticky='news')
        self.arrange_stack_box()

        button_row += 1
        self.my_entry_frame.grid(row=button_row, column=0, columnspan=6)
        self.my_entry['font'] = ('Roboto Mono Medium', '10')
        self.my_entry_label.grid(row=0, column=0)
        self.my_entry.grid(row=0, column=1, sticky='news')
        button_row += 1
        i_column = -1
        self.my_entry_frame.grid(row=button_row, column=(i_column := i_column + 1), columnspan=6)
        self.my_entry['font'] = ('Roboto Mono Medium', '10')
        self.my_entry_label.grid(row=0, column=0)
        self.my_entry.grid(row=0, column=1, sticky='news')

        button_row += 1
        i_column = -1
        self.drop_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.swap_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.roll_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.stack_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.undo_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.clear_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.real_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.imag_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.conj_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.complex_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.fraction_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.percent_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.percentof_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.percentchg_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.rtop_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ptor_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.int_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.dec_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ceil_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.floor_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self._7_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._8_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._9_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.divide_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.square_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.root_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.inverse_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.cubed_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.power_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.inv_power_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self._4_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._5_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._6_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.multiply_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.log_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.power10_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ln_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.exp_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ln2_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.exp2_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self._1_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._2_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._3_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.minus_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.e_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.comb_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.perm_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.fact_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.mfact_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.subfactorial_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self._0_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.dot_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.eex_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.add_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.pi_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.sin_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.cos_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.tan_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.cas_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.radians_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.chgsgn_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.uscore_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.enter_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.tau_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.arc_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.hyp_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.var_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.store_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.recall_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.athash_frame.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.at_button.pack(side=LEFT, fill='x', expand=True)
        self.hash_button.pack(side=RIGHT, fill='x', expand=True)
        self.my_frame.forget()
        self.my_frame.pack()
        #app.geometry('950x530')
        app.resizable(False, False)
        app.geometry(f'+{self.settings_dict['left']}+{self.settings_dict['top']}')
        self.settings_dict['screen_orientation'] = 'l'
        self.update_status_box()

    def arrange_landscape_right(self):
        '''Arrange buttons etc in landscape with keypad on the right.'''
        app.resizable(True, True)
        button_row = 0
        self.status_box.grid(row=button_row, column=0, columnspan=6)

        button_row += 1
        self.stack_box_frame.grid(row=button_row, column=0, columnspan=9, sticky='news')
        self.arrange_stack_box()

        button_row += 1
        self.my_entry_frame.grid(row=button_row, column=0, columnspan=9)
        self.my_entry['font'] = ('Roboto Mono Medium', '10')
        self.my_entry_label.grid(row=0, column=0)
        self.my_entry.grid(row=0, column=1, sticky='news')
        button_row += 1
        i_column = -1
        self.my_entry_frame.grid(row=button_row, column=(i_column := i_column + 1), columnspan=6)
        self.my_entry['font'] = ('Roboto Mono Medium', '10')
        self.my_entry_label.grid(row=0, column=0)
        self.my_entry.grid(row=0, column=1, sticky='news')

        button_row += 1
        i_column = -1
        self.drop_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.swap_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.roll_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.stack_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.undo_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.clear_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.real_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.imag_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.conj_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.complex_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.rtop_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ptor_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.int_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.dec_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ceil_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.floor_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.fraction_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.percentof_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.percentchg_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.percent_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.square_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.root_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.inverse_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.cubed_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.power_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.inv_power_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.e_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._7_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._8_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._9_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.divide_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.log_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.power10_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ln_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.exp_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.ln2_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.exp2_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.pi_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._4_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._5_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._6_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.multiply_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.comb_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.perm_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.fact_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.mfact_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.subfactorial_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.var_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.tau_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._1_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._2_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self._3_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.minus_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.sin_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.cos_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.tan_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.cas_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.store_button.grid(row=button_row, column=(i_column := i_column + 2), sticky='news')
        self.enter_button.grid(row=button_row, rowspan=2, column=(i_column := i_column + 1), sticky='news')
        self._0_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.dot_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.eex_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.add_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')

        button_row += 1
        i_column = -1
        self.radians_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.arc_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.hyp_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.recall_button.grid(row=button_row, column=(i_column := i_column + 3), sticky='news')
        self.uscore_button.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.chgsgn_button.grid(row=button_row, column=(i_column := i_column + 2), sticky='news')
        self.athash_frame.grid(row=button_row, column=(i_column := i_column + 1), sticky='news')
        self.at_button.pack(side=LEFT, fill='x', expand=True)
        self.hash_button.pack(side=RIGHT, fill='x', expand=True)
        self.my_frame.forget()
        self.my_frame.pack()
        app.resizable(False, False)
        app.geometry(f'+{self.settings_dict['left']}+{self.settings_dict['top']}')
        self.settings_dict['screen_orientation'] = 'r'
        self.update_status_box()

    def cycle_orientation(self):
        '''Rotate layout between portrait and landscape.'''
        #app.withdraw()
        match self.settings_dict['screen_orientation']:
            case 'l':
                self.arrange_landscape_right()
            case 'r':
                self.arrange_portrait()
            case 'p':
                self.arrange_landscape_left()
        #self.update_status_box()
        #self.display_stack()
        #app.update_idletasks()
        #app.after(200, lambda: app.deiconify())

    class DisplayFormat:
        ''' Define the display formats.
            Constants cannot be used in match - case, but they do work if
            they are part of a class.
        '''
        FORMAT_SCI = 0
        FORMAT_ENG = 1
        FORMAT_BASE = 2
        FORMAT_SUFFIX = 3
        FORMAT_ROMAN = 4
        FORMAT_WORD = 5
        FORMAT_FRACTION = 6
        FORMAT_DMS = 7
        FORMAT_SEXAGESIMAL = 8

    def mouse_wheel(self, event) -> None:
        if event.delta == 120:
            self.roll_stack()
        if event.delta == -120:
            self.roll_stack(1)

    def left_mouse_0(self, event) -> None:
        self.move_field('0', 'left')
        return 'break'

    def right_mouse_0(self, event) -> None:
        self.move_field('0', 'right')
        return 'break'

    def left_mouse_1(self, event) -> None:
        self.move_field('1', 'left')
        return 'break'

    def right_mouse_1(self, event) -> None:
        self.move_field('1', 'right')
        return 'break'

    def left_mouse_2(self, event) -> None:
        self.move_field('2', 'left')
        return 'break'

    def right_mouse_2(self, event) -> None:
        self.move_field('2', 'right')
        return 'break'

    def left_mouse_3(self, event) -> None:
        self.move_field('3', 'left')
        return 'break'

    def right_mouse_3(self, event) -> None:
        self.move_field('3', 'right')
        return 'break'

    def left_mouse_4(self, event) -> None:
        self.move_field('4', 'left')
        return 'break'

    def right_mouse_4(self, event) -> None:
        self.move_field('4', 'right')
        return 'break'

    def left_mouse_5(self, event) -> None:
        self.move_field('5', 'left')
        return 'break'

    def right_mouse_5(self, event) -> None:
        self.move_field('5', 'right')
        return 'break'

    def move_field(self, f_num: str, direction: str) -> None:
        data_name = eval('self.reg' + f_num + '_data')
        left_name = eval('self.reg' + f_num + '_left')
        right_name = eval('self.reg' + f_num + '_right')
        if direction == 'left':
            data_name.xview_scroll(-44, 'units')
        else:
            data_name.xview_scroll(44, 'units')
        if data_name.xview()[0] > 0.0:
            left_name.configure(text='<', fg_color='yellow')
        else:
            left_name.configure(text='', fg_color='lightyellow')
        if data_name.xview()[1] < 1.0:
            right_name.configure(text='>', fg_color='yellow')
        else:
            right_name.configure(text='', fg_color='lightyellow')

    def clear_menu_actions(self, choice):
        '''Clears comments and/or stack.
        '''
        match choice:
            case 'cc':
                c_str = 'Clear comments'
            case 'cs':
                c_str = 'Clear stack'
            case 'ci':
                c_str = 'Clear imaginary parts'
            case 'cu':
                c_str = 'Clear units'
            case 'cv':
                c_str = 'Clear variables'
            case 'ce':
                c_str = 'Clear equations'
        popup_message.show(title='Confirm', message=c_str, yesno=True)
        response = popup_message.get()
        #print(f'response={response}')
        if response == 'y':
            l = len(self.stack_values)
            self.save_stack()
            match choice:
                case 'cc':
                    for _1 in range(l):
                        self.stack_values[_1][2] = ''
                case 'cs':
                    for _1 in range(l):
                        self.stack_values[_1] = [0.0, 0.0, '', {}]
                case 'ci':
                    for _1 in range(l):
                        self.stack_values[_1][1] = 0.0
                case 'cu':
                    for _1 in range(l):
                        self.stack_values[_1][3] = {}
                case 'cv':
                    self.created_vars = {}
                case 'ce':
                    self.equations = []
            self.my_entry.delete(0, 'end')
        self.display_stack()

    def store_equation(self) -> None:
        ''' Stores the equation in E to the equation store.

        Stores the contents of E into the equation store.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) == 0:
            popup_message.show(title='Equation', message='No valid equation entered in E.')
            return
        self.equations.append(self.my_entry.get()[1:]) #  Store without leading =
        self.my_entry.delete(0, 'end')

    def recall_equation(self) -> None:
        ''' Recalls an equation from the equation store to R0.

        Shows the currently stored equations, selecting one will append it to R0.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.equations) == 0:
            popup_message.show(title='Equation', message='No equations have been stored yet.')
            return
        geo = split('x', self.recall_button.winfo_geometry().replace('+', 'x'))
        left = int(geo[2])
        top = int(geo[3])
        self.eq_win = CTkToplevel(app)
        # self.eq_win.geometry(''.join(['+', str(left), '+', str(top)]))
        self.eq_win.geometry(f'+{left}+{top}')
        self.eq_win.grab_set()
        self.eq_win.configure(corner_radius=0)
        self.eq_win.configure(fg_color='lightblue')
        eq_label = CTkLabel(self.eq_win, text='Choose an equation')
        eq_label.pack()
        for equation in self.equations:
            CTkButton(self.eq_win,
                      border_width=1,
                      corner_radius=0,
                      fg_color='lightyellow',
                      text_color='blue',
                      text=equation,
                      command=lambda x=equation: self.button(x)).pack()
        CTkButton(self.eq_win,
                  text='Cancel',
                  width=45,
                  command=lambda: self.button('cancel')).pack()
        app.wait_window(self.eq_win)

    def button(self, choice) -> None:
        if choice != 'cancel':
            self.my_entry.insert('end', '=' + choice)
        self.eq_win.destroy()

    def update_status_box(self) -> None:
        '''Update the status box.'''
        s = ''
        match self.settings_dict['format_type']:
            case self.DisplayFormat.FORMAT_SCI:
                s = 'Scientific'
            case self.DisplayFormat.FORMAT_ENG:
                s = 'Engineering'
            case self.DisplayFormat.FORMAT_BASE:
                s = 'Base'
            case self.DisplayFormat.FORMAT_SUFFIX:
                s = 'Suffix'
            case self.DisplayFormat.FORMAT_ROMAN:
                s = 'Roman'
            case self.DisplayFormat.FORMAT_WORD:
                s = 'Words'
            case self.DisplayFormat.FORMAT_FRACTION:
                s = 'Fraction'
            case self.DisplayFormat.FORMAT_DMS:
                s = '\u00b0 \' "'
            case self.DisplayFormat.FORMAT_SEXAGESIMAL:
                s = 'Sexagesimal'
            case _:
                s = 'General'
        # s = ''.join([s, '. ', str(self.settings_dict['significant_digits']), ' decimals',
        #              '. base ', str(self.settings_dict['display_base']),
        #              '. [', self.settings_dict['screen_orientation'], ']'])
        s = (f"{s}. "
             f"{str(self.settings_dict['significant_digits'])} decimals."
             f" base {str(self.settings_dict['display_base'])}. "
             f"[{self.settings_dict['screen_orientation']}]")
        self.status_box.configure(state='normal')
        self.status_box.replace_text(s, 'center')
        self.status_box.configure(state='disabled')


    def show_variables(self) -> None:
        '''Shows currently defined variables.

        Shows a list of all variables that have been defined.
        '''
        if len(self.created_vars) == 0:
            popup_message.show(title='Variables', message='no variables have been defined')
            return
        self.var_popup = Menu(self.my_frame, tearoff=0, font=('Arial', 12))
        for var, val in self.created_vars.items():
            s_val = str(val)
            self.var_popup.add_command(label=var + ' = ' + s_val,
                                       foreground='blue',
                                       background='yellow',
                                       command=lambda x=s_val: self.my_entry.insert('end', x))
        x = self.var_button.winfo_rootx() + BUTTON_WIDTH
        y = self.var_button.winfo_rooty()
        self.var_popup.tk_popup(x, y, 0)

    def pressed_op(self, operand: str, the_event=None) -> None:
        ''' An operand, +, -, *, /, ^, !, % has been pressed.
        If the entry box is empty, execute it.
        If there is no = in the entry box and it doesn't start with
        a (, then execute it.
        Otherwise, just add it on to the entry box.'''
        # print(f'operand={operand}. Event={the_event}')
        # Check for Control or Alt keys. Dont process if pressed.
        if str(the_event).find('state=Control') >= 0:
            # print('Control')
            return
        if str(the_event).find('|0x20000') >= 0:
            # print('Alt')
            return
        if str(the_event).find('|0x60000') >= 0: # Adds 0x40000 for numeric pad key
            # print('Alt + keypad')
            return
        if (len(self.my_entry.get()) == 0 or
           (self.my_entry.get().find('=') == -1) and
                (self.my_entry.get()[0] != '(')):
            match operand:
                case '+':
                    self.my_add()
                case '-':
                    self.my_subtract()
                case '*':
                    self.my_multiply()
                case '/':
                    self.my_divide()
                case '^':
                    self.my_power()
                case '!':
                    self.my_factorial()
                case '%':
                    self.my_percent()
        else:
            self.my_entry.insert(INSERT, operand)
        return 'break'

    def assign_r_vars(self):
        try:
            for _1 in range(6):
                s = 'R' + str(_1)
                del globals()[s]
        except:
            pass
        for _1 in range(min(6, len(self.stack_values))):
            s = 'R' + str(_1)
            try:
                if self.stack_values[_1][1] == 0:
                    globals()[s] = self.stack_values[_1][0]
                else:
                    globals()[s] = complex(self.stack_values[_1][0], self.stack_values[_1][1])
            except:
                globals()[s] = complex(0, 0)

    def show_stack(self) -> None:
        '''Display the stack values.'''
        #  out_str = ''
        this_str = ''
        this_str += f' E: {self.my_entry.get()}'
        for _1 in range(len(self.stack_values)):
            this_str += f'\nR{_1}: '
            for _2 in range(4):
                this_str += f'{self.stack_values[_1][_2]}: '
        popup_message.show(title='Stack', message=this_str[:-1], alignment=LEFT)

    def display_stack(self) -> None:
        '''Update the stack.'''

        def format_line(text_field: CTkTextbox, left_label: CTkLabel, right_label: CTkLabel) -> None:
            '''Format the line in the stack.'''
            text_field.configure(state='normal')
            text_field.replace_text(curr_str)
            text_field.configure(state='disabled')
            if text_field.xview()[0] > 0.0:
                left_label.configure(text='<', fg_color='yellow')
            if text_field.xview()[1] < 1.0:
                right_label.configure(text='>', fg_color='yellow')
            text_field.tag_delete('brown3')
            text_field.tag_delete('green')
            text_field.tag_delete('power')
            if len(s) > 0:
                text_field.tag_add('brown3', s_p, 'end')
                text_field.tag_config('brown3', foreground='brown3')
            if uom_start > -1:
                ''' Units of measure are coloured green.'''
                for x in range(uom_start, uom_start + uom_len):
                    s_s = '1.0 linestart+' + str(uom_start) + 'c'
                    s_e = '1.0 linestart+' + str(uom_start + uom_len) + 'c'
                    text_field.tag_add('green', s_s, s_e)
                    text_field.tag_config('green', foreground='green')
                    #  Units powers are offset up by 4 and reduced in size by 3 pixels.
                    if '0123456789-./'.find(curr_str[x : x+1]) > -1:
                        s_s = '1.0 linestart+' + str(x) + 'c'
                        s_e = '1.0 linestart+' + str(x + 1) + 'c'
                        text_field.tag_add('power', s_s, s_e)
                        text_field.tag_config('power', offset='+4')
                        f = text_field.cget('font')
                        text_field._textbox.tag_config('power',
                                                       {'font': (f.cget('family'), -f.cget('size') + 3)})
                        #  This bypasses the 'font' check in ctk_textbox.py (CustomTkinter:CTkTextbox).
                        #  NOTE: font.cget('size') returns pixel height as positive, but it needs to be negative
                        #  to set size to pixels. Setting font size to positive number uses points.
            if self.settings_dict['format_type'] == self.DisplayFormat.FORMAT_WORD:
                text_widget_highlight.add(text_field, the_text='point', highlight_name='point', fg_color='blue', bg_color='lightyellow')
                text_widget_highlight.add(text_field, the_text='minus', highlight_name='minus', fg_color='blue', bg_color='lavenderblush')

        def clear_line(text_field: CTkTextbox, left_label: CTkLabel, right_label: CTkLabel) -> None:
            text_field.configure(state='normal')
            text_field.replace_text('')
            text_field.configure(state='disabled')
            left_label.configure(text='', fg_color='lightyellow')
            right_label.configure(text='', fg_color='lightyellow')

        clear_line(self.reg0_data, self.reg0_left, self.reg0_right)
        clear_line(self.reg1_data, self.reg1_left, self.reg1_right)
        clear_line(self.reg2_data, self.reg2_left, self.reg2_right)
        clear_line(self.reg3_data, self.reg3_left, self.reg3_right)
        clear_line(self.reg4_data, self.reg4_left, self.reg4_right)
        clear_line(self.reg5_data, self.reg5_left, self.reg5_right)

        while len(self.stack_values) < 6:
            self.stack_values.append([0.0, 0.0, '', {}])
        for sv_ctr in range(min(6, len(self.stack_values))):
            try:
                if len(self.stack_values[sv_ctr]) != 4:
                    self.stack_values[sv_ctr] = [0.0, 0.0, '', {}]
            except:
                self.stack_values[sv_ctr] = [0.0, 0.0, '', {}]
            real_part = self.stack_values[sv_ctr][0]  #  Real part
            if not isinstance(real_part, (int, float)):
                real_part = 0
            imag_part = self.stack_values[sv_ctr][1]  #  Imaginary part
            if not isinstance(imag_part, (int, float)):
                imag_part = 0
            s = ' ' + str(self.stack_values[sv_ctr][2])  #  Comment
            # remove zero values keys from units
            if len(self.stack_values[sv_ctr][3]) > 0:
                for k, v in self.stack_values[sv_ctr][3].copy().items():
                    if v == 0:
                        del self.stack_values[sv_ctr][3][k]
            unit_part = self.stack_values[sv_ctr][3].copy() #  Units part
            if imag_part == 0:
                curr_str = self.format_number(real_part)
            else:
                real_sign = ''
                imag_sign = '+'
                if real_part < 0:
                    real_sign = '-'
                    real_part *= -1
                if imag_part < 0:
                    imag_sign = '-'
                    imag_part *= -1
                real_part_s = self.format_number(real_part)
                imag_part_s = self.format_number(imag_part)
                if real_part_s in ['0', '-0']:
                    real_part_s = ''
                if imag_part_s in ['1', 'one']:
                    imag_part_s = ''
                if imag_part_s and imag_part_s[-1].isalpha():
                    j_part = ' j'
                else:
                    j_part = 'j'
                if real_part == 0 and imag_sign == '+':
                    imag_sign = ''
                curr_str = f'{real_sign}{real_part_s}{imag_sign}{imag_part_s}{j_part}'
            uom_str = self.format_uom(unit_part)
            uom_start = -1
            uom_len = len(uom_str)
            if uom_len > 0:
                curr_str += ' '
                uom_start = len(curr_str)
                curr_str += uom_str
            l = len(curr_str)
            curr_str += s
            s_p = '1.0 linestart+' + str(l + 1) + 'c'
            match sv_ctr:
                case 0:
                    format_line(self.reg0_data, self.reg0_left, self.reg0_right)
                case 1:
                    format_line(self.reg1_data, self.reg1_left, self.reg1_right)
                case 2:
                    format_line(self.reg2_data, self.reg2_left, self.reg2_right)
                case 3:
                    format_line(self.reg3_data, self.reg3_left, self.reg3_right)
                case 4:
                    format_line(self.reg4_data, self.reg4_left, self.reg4_right)
                case 5:
                    format_line(self.reg5_data, self.reg5_left, self.reg5_right)
        self.assign_r_vars()


    def format_uom(self, uom_dict: dict) -> str:
        if type(uom_dict) != dict or len(uom_dict) == 0:
            return ''
        out_str: str = ''
        for key, value in uom_dict.items():
            if value != 0:
                out_str += key
                if value != 1:
                    if value == int(value):
                        out_str+= str(int(value))
                    else:
                        out_str += str(Fraction(value))
                        # out_str += self.my_fraction(value)
                out_str += ' ' # '\u00b7'

        #  If there are decimal points in any of the powers, we use a space
        #   between the items, otherwise we use middle dot, \u00b7.
        #  if out_str.find('.') > -1:
        #      out_str = out_str.replace('\u00b7', ' ')
        return out_str[:-1]


    def set_format(self, fmt_type: int) -> None:
        '''Set the format for the stack display.'''
        self.settings_dict['format_type'] = fmt_type
        match self.settings_dict['format_type']:
            case self.DisplayFormat.FORMAT_SCI:  #  Scientific
                self.settings_dict['display_base'] = 10
                self.fmtString = '{:e}'
            case self.DisplayFormat.FORMAT_ENG:  #  Engineering
                self.fmtString = ''
            case self.DisplayFormat.FORMAT_BASE:  #  Base 2 - 62
                self.fmtString = ''
            case self.DisplayFormat.FORMAT_ROMAN:  #  Roman
                self.settings_dict['display_base'] = 10
                self.fmtString = ''
            case self.DisplayFormat.FORMAT_WORD:  #  Word
                self.settings_dict['display_base'] = 10
                self.fmtString = ''
            case self.DisplayFormat.FORMAT_FRACTION:  #  Fraction
                self.fmtString = ''
            case self.DisplayFormat.FORMAT_DMS:  #  DMS
                self.settings_dict['display_base'] = 10
                self.fmtString = ''
                self.radians_button.configure(text='deg')
                self.radians_conv = 180 / pi
            case self.DisplayFormat.FORMAT_SUFFIX:  #  Suffix
                self.settings_dict['display_base'] = 10
                self.fmtString = ''
            case self.DisplayFormat.FORMAT_SEXAGESIMAL:
                self.settings_dict['display_base'] = 10
                self.fmtString = ''
            case _:
                print(' Invalid format_type:' + str(self.settings_dict['format_type']))
                self.fmtString = '{:.' + str(self.settings_dict['significant_digits']) + 'f}'
        self.update_status_box()
        self.display_stack()

    def set_base(self, basetoset: int) -> None:
        self.settings_dict['display_base'] = basetoset
        if self.settings_dict['display_base'] == 10:
            self.set_format(self.DisplayFormat.FORMAT_SCI)
        else:
            self.set_format(self.DisplayFormat.FORMAT_BASE)
        self.display_stack()

    def fraction_to_base(self, fraction_part: float, base: int) -> str:
        '''Convert fraction to the base.'''
        fbase_num: str = ''
        num: int = 1
        while num <= self.settings_dict['significant_digits']:
            temp = int(base ** num * fraction_part)
            fbase_num += self.base_digits[temp]
            fraction_part -= temp / (base ** num)
            num += 1
        fbase_num = fbase_num.rstrip('0')
        return fbase_num

    def decimal_to_base(self, num: float, to_base: int=10) -> str:  #  Maximum base - 62: 0-9, A-Z & a-z
        if num < 0:
            neg = True
            num = -num
        else:
            neg = False
        newnum = int(num) + round(num - int(num), self.settings_dict['significant_digits'])  #  round to sig_digits decimal places.
        tbase_num = ''
        decimal_part = int(newnum)
        fraction_part = round(newnum - decimal_part, self.settings_dict['significant_digits'])
        while newnum > 0:
            dig = int(newnum % self.settings_dict['display_base'])
            tbase_num += self.base_digits[dig]
            newnum //= self.settings_dict['display_base']
        tbase_num = tbase_num[::-1]
        if tbase_num == '':
            tbase_num = '0'
        if fraction_part > 0:
            tbase_num += '.'
            tbase_num += self.fraction_to_base(fraction_part, self.settings_dict['display_base'])
        if self.settings_dict['display_base'] != 10:
            tbase_num += '_'
            tbase_num += str(self.settings_dict['display_base'])
        if neg:
            tbase_num = '-' + tbase_num
        return tbase_num

    def base_to_decimal(self, num_str: str, base: int) -> (bool, float):
        '''Convert base n number to decimal.'''
        converted_ok = True
        if not 2 <= base <= 62:
            popup_message.show(title='base_to_dec', message='Base must be between 2 and 62.')
            return False, 0.0
        if base <= 36:  #  Only uppercase for base <= 36, base 37 to 62 uses lower case
            num_str = num_str.upper()
        errchars = ''
        neg: int = 1
        if num_str[0] == '-':
            num_str = num_str[1:]
            neg = -1
        cf = self.base_digits[:base] + '.'
        for k in range(len(num_str)):  #  check the digits are valid in base
            dig = num_str[k]
            if dig not in cf:
                if len(errchars) == 0:
                    errchars = dig
                else:
                    errchars = errchars.replace(' and', ', ')
                    errchars += ' and '
                    errchars += dig
        if len(errchars) > 0:
            if len(errchars) == 1:
                t = ' is not a '
                c = ''
            else:
                t = ' are not '
                c = 's'
            popup_message.show(title='base_to_desc',
                          message=f'{errchars}{t}valid base {base} character{c}')
            return False, 0.0
        fraction_part = ''
        x = num_str.split('.')
        integer_part = x[0]
        if len(x) == 2:
            fraction_part = x[1]
        integer_part = integer_part[::-1]
        num_1 = 0
        if integer_part != '':
            for k in range(len(integer_part)):
                dig = integer_part[k]
                dig_1 = self.base_digits.find(dig)
                num_1 += dig_1 * (base ** k)
        num_1 = float(num_1)
        f_num = 0.0
        if fraction_part != '':
            for k in range(len(fraction_part)):
                dig = fraction_part[k]
                dig_1 = self.base_digits.find(dig)
                f_num += dig_1 * (base ** -(k + 1))
        if f_num != 0.0:
            num_1 += f_num
        return converted_ok, neg*num_1

    def fraction_format(self) -> None:
        '''Configures the display of fractions.

            This button causes the display of vulgar fractions to swap between
        simple d/c and mixed fractions a_b/c.
        e.g. 23/7 expressed as a_b/c is 3_2/7.

        Parameters:

        Returns:
            Nothing

        '''
        self.set_format(self.DisplayFormat.FORMAT_FRACTION)
        if self.fracfmtproper:
            self.fraction_button.configure(text='d/c')
        else:
            self.fraction_button.configure(text='a_b/c')
        self.fracfmtproper = not self.fracfmtproper
        self.display_stack()

    def my_fraction(self, number_to_format: float) -> str:
        '''Convert number to fraction format.'''
        str0 = str(Fraction(round(number_to_format, self.settings_dict['significant_digits'])))
        if str0.endswith('/1'):
            str0 = str0[0:-2]
        elif self.fracfmtproper is False:
            str1 = str0.split('/')
            i1 = int(str1[0])
            i2 = int(str1[1])
            if abs(i1) > abs(i2):  #  We have improper fraction
                str0 = self.proper(i1, i2)
        return str0

    def format_number(self, number_to_format: float) -> str:
        '''Formats passed number according to the format type.'''

        def formatter(number_to_format: float) -> str:
            self.settings_dict['display_base'] = 10
            if (number_to_format >= 10 ** self.settings_dict['significant_digits']
                    or number_to_format <= -10 ** self.settings_dict['significant_digits']
                    or (-10 ** -4 < number_to_format < 10 ** -4
                        and number_to_format != 0)):
                str1 = '{:.' + str(self.settings_dict['significant_digits']) + 'e}'
            else:
                str1 = '{:.' + str(self.settings_dict['significant_digits']) + 'f}'
            str0 = str1.format(number_to_format)
            if str0.find('e') == -1:
                str0 = str0.rstrip('0').rstrip('.')
            else:
                str1 = str0.split('e')
                str0 = str1[0].rstrip('0').rstrip('.') + 'e' + str1[1]
            return str0

        match self.settings_dict['format_type']:
            case self.DisplayFormat.FORMAT_SCI:
                str0 = formatter(number_to_format)
            case self.DisplayFormat.FORMAT_FRACTION:
                if number_to_format >= 1000000 or number_to_format <= -1000000:
                    str0 = formatter(number_to_format)
                else:
                    str0 = self.my_fraction(number_to_format)
            case self.DisplayFormat.FORMAT_ENG:
                str0 = eng_format(number_to_format, self.settings_dict['significant_digits'], False)
            case self.DisplayFormat.FORMAT_BASE:
                str0 = self.decimal_to_base(number_to_format, self.settings_dict['display_base'])
            case self.DisplayFormat.FORMAT_SUFFIX:
                str0 = eng_format(number_to_format, self.settings_dict['significant_digits'], True)
            case self.DisplayFormat.FORMAT_ROMAN:
                if (-4_000_000_000 < number_to_format < 4_000_000_000 and
                        number_to_format == int(number_to_format)):
                    str0 = integer_to_roman(int(number_to_format))
                else:
                    str0 = self.decimal_to_base(number_to_format)
            case self.DisplayFormat.FORMAT_WORD:
                self.save_stack()
                str0 = float_to_word(number_to_format, self.settings_dict['significant_digits'])
            case self.DisplayFormat.FORMAT_DMS:
                str0 = float_to_dms(number_to_format)
            case self.DisplayFormat.FORMAT_SEXAGESIMAL:
                str0 = float_to_sexagesimal(number_to_format, self.settings_dict['significant_digits'])
            case _:
                str0 = '?????'

        if str0 in ('0', '-0') and number_to_format != 0:  #  non-zero value displaying as zero
            str1 = '{:.' + str(self.settings_dict['significant_digits']) + 'e}'  #  force to scientific display
            str0 = str1.format(number_to_format)
        #print('end_format_number: str0=', str0)
        return str0

    def equation_entered(self, entered_string: str) -> None:
        '''
        The input box text starts with =
        '''
        try:
            temp_value = eval(entered_string[1:len(entered_string)])
        except Exception as ex:
            popup_message.show(title='Equation error', message=str(ex))
            return
        self.save_stack()
        if len(self.stack_values) == 10:
            self.stack_values.pop()
        self.stack_values.insert(0, [temp_value.real, temp_value.imag, '', {}])
        self.clear_myentry()
        self.display_stack()


    def process_unit_string(self, unit_string:str) -> dict:
        unit_dict: dict = {}
        unit_parts = unit_string.replace(';', ' ').replace(',', ' ').split()
        for unit_part in unit_parts:
            numbers = ''
            letters = ''
            numbers_found: Bool = False
            for char in unit_part:
                if char.isalpha():
                    if numbers_found:
                        popup_message.show(title='units', message=unit_part + ', units are out of order.')
                        return '', False
                    else:
                        letters += char
                elif char.isdigit() or char == '-' or char == '.':
                    numbers += char
                    numbers_found = True
                else:
                    popup_message.show(title='units', message=char + ' is not a valid character.')
                    return '', False
            if numbers == '':
                numbers = '1'
            try:
                num = float(numbers)
            except:
                popup_message.show(title='units', message='an invalid value was found, ' + numbers)
                return '', False
            if num == int(num):
                num = int(num)
            try:
                unit_dict[letters] += num
            except:
                unit_dict[letters] = num
        return unit_dict, True


    # def overbar(self):
    #     popup_message.show(title='Overbar', message='To be implemented.')
    #     t_ext = self.my_entry.get()

        pass

    def my_enter(self) -> bool:
        '''Enter key pressed.'''
        self.save_stack()
        entered_string = self.my_entry.get()
        comment_entered = False
        unit_entered = False
        comment_string = ''
        unit_string = ''
        unit_dict = ''
        entered_string = entered_string.replace('@', '@u').replace('#', '@c')
        res = entered_string.split('@')
        for i in res[1:]:
            if i[:1] == 'c':
                comment_string += i[1:]# + ' '
            else:
                unit_string += i[1:] + ' '
        entered_string = res[0]
        if comment_string:
            comment_entered = True
        if unit_string:
            unit_entered = True
        if unit_entered:
            unit_dict, od_status = self.process_unit_string(unit_string)
            if not od_status:
                return
        entered_string = entered_string.replace(' ', '')
        if len(entered_string) == 0:  #  Nothing in the input buffer, duplicate the top stack element
            if not (unit_entered or comment_entered):
                self.save_stack()
                if len(self.stack_values) == 10:
                    self.stack_values.pop()
                self.stack_values.insert(0,
                                            [self.stack_values[0][0],
                                             self.stack_values[0][1],
                                             self.stack_values[0][2],
                                             self.stack_values[0][3].copy()])
            self.clear_myentry()
        else:
            prefix = entered_string[:2].lower()
            if (prefix := entered_string[:2].lower()) in '0b0o0d0h0r0x&b&o&d&h&r&x':
                match prefix:
                    case '0b' | '&b':
                        entered_string = entered_string[2:] + '_2'
                    case '0o' | '&o':
                        entered_string = entered_string[2:] + '_8'
                    case '0d' | '&d':
                        entered_string = entered_string[2:] + '_10'
                    case '0h' | '0x'| '&h' | '&x':
                        entered_string = entered_string[2:] + '_16'
                    case '0r' | '&r':
                        entered_string = entered_string[2:] + '_r'
            if entered_string[0] == '=':  #  We have an equation
                self.equation_entered(entered_string)
            elif entered_string.find('=') > 0:  #  An = somewhere other than the first character.
                self.other_equals(entered_string)
            elif entered_string.lower().find('_r') >= 0:
                if entered_string.lower().find('_r') == 0:
                    self.set_format(self.DisplayFormat.FORMAT_ROMAN)
                    self.clear_myentry()
                else:
                    entered_string = entered_string[0:len(entered_string) - 2].replace('1', 'i').upper()
                    #  In case 1's entered rather than i's
                    #  roman_value = roman_to_integer(entered_string)
                    try:
                        roman_value = roman_to_integer(entered_string)
                        self.save_stack()
                        if len(self.stack_values) == 10:
                            self.stack_values.pop()
                        self.stack_values.insert(0, [roman_value, 0.0, '', {}])
                        self.clear_myentry()
                    except Exception as e1:
                        popup_message.show(title='Entry error', message=e1, y_pos=.6)
                        return False
            elif entered_string.find("'") >= 0:  #  We have DMS number
                x = entered_string.split("'")
                #  Ensure we have at least 3 elements
                x.append('0')
                x.append('0')
                if x[0] == '':
                    x[0] = '0'
                if x[1] == '':
                    x[1] = '0'
                if x[2] == '':
                    x[2] = '0'
                self.save_stack()
                if len(self.stack_values) == 10:
                    self.stack_values.pop()
                self.stack_values.insert(0, [float(x[0]) + float(x[1]) / 60 + float(x[2]) / 3600, 0.0, '', {}])
                self.clear_myentry()
            elif entered_string.find(';') > -1: #  Sexagesimal number
                (err_value, ret_value) = sexagesimal_to_float(entered_string, self.settings_dict['significant_digits'])
                match err_value:
                    case 0:
                        if len(self.stack_values) == 10:
                            self.stack_values.pop()
                        self.stack_values.insert(0, [ret_value, 0.0, '', {}])
                        self.clear_myentry()
                    case 1:
                        popup_message.show(title='sexagesimal_to_float', message='sexagesimal number needs a single ;', y_pos=0.2)
                    case 2:
                        popup_message.show(title='sexagesimal_to_float', message='values must be integers.', y_pos=0.2)
            elif entered_string.find('_') > -1:  #  We have entered a base number
                if entered_string[-1] == '_':
                    popup_message.show(title=entered_string, message='No base number has been supplied.')
                    return False
                if entered_string.count('_') > 1:
                    popup_message.show(title=entered_string, message='Too many _ characters.')
                    return False
                entered_string = entered_string.replace('_h', '_16')
                entered_string = entered_string.replace('_d', '_10')
                entered_string = entered_string.replace('_o', '_8')
                entered_string = entered_string.replace('_b', '_2')
                entered_string = entered_string.replace('_H', '_16')
                entered_string = entered_string.replace('_D', '_10')
                entered_string = entered_string.replace('_O', '_8')
                entered_string = entered_string.replace('_B', '_2')
                underscore = entered_string.find('_')
                try:
                    entered_base = int(entered_string[underscore + 1:])
                except:
                    popup_message.show(title=entered_string[underscore + 2:], message=' base portion invalid.')
                    return False
                if not 2 <= entered_base <= 62:
                    popup_message.show(title=str(entered_base), message='Invalid base, valid values are 2 to 62.')
                    return False
                leading_part = entered_string[:underscore]
                if leading_part == '':
                    self.settings_dict['display_base'] = int(entered_base)
                    self.settings_dict['format_type'] = self.DisplayFormat.FORMAT_BASE
                    self.update_status_box()
                    self.display_stack()
                    self.clear_myentry()
                    #return True
                else:
                    converted_ok, new_value = self.base_to_decimal(leading_part, entered_base)
                    if converted_ok:
                        self.save_stack()
                        if len(self.stack_values) == 10:
                            self.stack_values.pop()
                        self.stack_values.insert(0, [new_value, 0.0, '', {}])
                        self.stack_values[0][0] = new_value
                        self.clear_myentry()
                    else:
                        popup_message.show(leading_part + entered_base, message=' something wrong.')
                        return
            elif entered_string.find('j)') != -1 or entered_string.find('i)') != -1:  #  We have a complex number
                entered_string = entered_string.replace('i)', 'j)')
                entered_string = entered_string.replace('+j)', '+1j)')
                entered_string = entered_string.replace('-j)', '-1j)')
                try:
                    c = complex(entered_string)
                except:
                    popup_message.show(title='Invalid Complex number', message=entered_string)
                    return False
                self.save_stack()
                if len(self.stack_values) == 10:
                    self.stack_values.pop()
                self.stack_values.insert(0, [c.real, c.imag, '', {}])
                self.clear_myentry()
            else:  #  Convert buffer to number and put on top of stack
                try:
                    temp_value = float(entered_string)
                except ValueError:
                    popup_message.show(title='Invalid number', message=entered_string)
                    return False
                self.save_stack()
                if len(self.stack_values) == 10:
                    self.stack_values.pop()
                self.stack_values.insert(0, [temp_value, 0.0, '', {}])
                self.clear_myentry()
        if comment_entered:
            self.stack_values[0][2] = comment_string
        if unit_entered:
            self.stack_values[0][3] = unit_dict # self.combine_uom(unit_dict, self.stack_values[0][3], '+')
        self.display_stack()
        return True

    def other_equals(self, entered_string: str) -> None:
        '''
        The input box text has = somewhere other than the first character.
        '''
        try:
            exec(entered_string, None, self.created_vars)
            self.created_vars = dict(sorted(self.created_vars.items(), key=lambda item: item[0]))
        except Exception as e:
            popup_message.show(title='Equation error', message=str(e))
            return
        #  Go through the variables (keys) found and check they are valid.
        #  items in not_permitted are unable to be assigned values.
        #  A variable with no value means delete the variable.
        #  Only int, float and complex are allowed.
        #  Make a list of invalid variables.
        error_msg = ''
        keys_to_delete = []
        for key, value in self.created_vars.items():
            if key in self.not_permitted:  #  These are reserved
                error_msg += key + ', '
                keys_to_delete.append(key)
            elif value == '':
                keys_to_delete.append(key)
            elif not isinstance(value, (int, float, complex)):
                error_msg += 'Only int, float and complex allowed (' + str(value) + ')\n'
                keys_to_delete.append(key)
            else:
                globals()[key] = value
        for item in keys_to_delete:
            del self.created_vars[item]
        if error_msg != '':
            popup_message.show(title='Vars:', message='Cannot use ' + error_msg[:-2])
        else:
            self.clear_myentry()


    def roll_stack(self, direction: int=0) -> None:
        '''Rolls the stack up or down.

        Rolls the stack up or down.
        '''
        if len(self.stack_values) > 0:
            if direction == 0:
                self.stack_values.append(self.stack_values.pop(0))
            else:
                self.stack_values.insert(0, self.stack_values.pop())
            self.display_stack()

    def swap_stack(self) -> None:
        '''Swap the top 2 elements of the stack.

        Swaps the values in the top 2 elements of the stack.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.stack_values) > 0:
            self.stack_values[0], self.stack_values[1] = self.stack_values[1], self.stack_values[0]
            self.display_stack()

    def drop_stack(self) -> None:
        '''Deletes the value in R1.

        Pops the top value off the stack.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.stack_values) > 0:
            self.save_stack()
            self.stack_values.pop(0)
        if len(self.stack_values)< 6:
            self.stack_values.append([0.0, 0.0, '', {}])
        self.display_stack()

    def clear_stack(self) -> None:
        '''Shows the Clear menu.

        Shows the Clear menu.
        '''
        self.save_stack()
        #  Position popup window so it doesn't cover the button.
        x = self.clear_button.winfo_rootx() + self.clear_button.winfo_width()
        y = self.clear_button.winfo_rooty()
        self.popup_clear_menu.tk_popup(x, y, 0)
        self.display_stack()


    def proper(self, numerator: int | tuple, denominator: int=1, sep: str='_') -> str:
        '''Return a proper fraction.'''
        if isinstance(numerator, tuple):
            the_numerator = numerator[0]
            the_denominator = numerator[1]
        else:
            the_numerator = numerator
            the_denominator = denominator
        if the_numerator != int(the_numerator) or the_denominator != int(the_denominator):
            raise Exception('numerator and denominator MUST be integers')
        if the_denominator == 0:
            raise Exception('denominator cannot be 0')
        if the_numerator == the_denominator:
            return '1'
        if the_denominator < 0:
            the_denominator *= -1
            the_numerator *= -1
        if the_numerator < 0:
            neg = '-'
            the_numerator *= -1
        else:
            neg = ''
        if the_numerator < the_denominator:
            return neg + str(the_numerator) + '/' + str(the_denominator)
        integer_part = the_numerator // the_denominator
        the_numerator %= the_denominator
        if the_numerator == 0:
            return str(neg + str(integer_part))
        g = gcd(the_numerator, the_denominator)
        the_numerator = the_numerator // g
        the_denominator = the_denominator // g
        return neg + str(integer_part) + sep + str(the_numerator) + '/' + str(the_denominator)

    def clear_myentry(self) -> None:
        '''Clear the my_entry field.'''
        self.my_entry.delete(0, 'end')


    def save_stack(self) -> None:
        '''Saves the current stack, my_entry and format_type.'''
        #  if self.my_entry_had_data:
        if len(self.redo_stack) >= 9: # STACK_DEPTH - 1:
            self.redo_stack.pop()
        if len(self.redo_stack) == 0 or self.redo_stack[0] != [self.stack_values, self.my_entry.get()]:  #  Update redo if different
            self.redo_stack.insert(0, [self.stack_values.copy(), self.my_entry.get()])
        self.redo_counter = 0
        #  self.my_entry_had_data = False

    def restore_stack(self) -> None:
        '''Restore the stack. Used when there is an error.

        Restore the stack to the previous values.

        Parameters:
            None

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0:
            self.my_entry.replace_text(self.my_entry.get()[:-1])
        elif self.redo_counter < len(self.redo_stack):
            self.stack_values = self.redo_stack[self.redo_counter][0].copy()
            self.my_entry.replace_text(self.redo_stack[self.redo_counter][1])
            self.redo_counter += 1
        self.display_stack()

    def standardise_stack(self) -> bool:
        '''
            If there is something in the entry buffer (E), push it onto the stack.
        '''
        # self.save_stack()
        if len(self.my_entry.get()) > 0:
            self.save_stack()
            return self.my_enter()
        else:
            return True

    def my_percent(self) -> None:
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] != 0:
            popup_message.show(title='Percentage', message='Cannot be Complex.')
            return
        self.save_stack()
        self.stack_values[0] = [self.stack_values[1][0] * self.stack_values[0][0] / 100,
                                self.stack_values[1][1] * self.stack_values[0][0] / 100,
                                '', {}]
        self.stack_values.pop(1)
        self.display_stack()

    def my_percent_of(self) -> None:
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][0] == 0:
            popup_message.show(title='Percent of', message='Cannot be zero')
            return
        if self.stack_values[0][1] != 0:
            popup_message.show(title='Percent of', message='Cannot be complex')
            return
        self.save_stack()
        self.stack_values[0] = [(self.stack_values[0][0] / self.stack_values[1][0]) * 100, 0.0, '', {}]
        self.stack_values.pop(1)
        self.display_stack()

    def my_percentchg(self) -> None:
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][0] == 0:
            popup_message.show(title='Percent change', message='Cannot be zero')
            return
        if self.stack_values[0][1] != 0:
            popup_message.show(title='Percent change', message='Cannot be complex')
            return
        self.save_stack()
        self.stack_values[0] = [(self.stack_values[0][0] - self.stack_values[1][0]) / self.stack_values[1][0] * 100,
                                0.0, '', {}]
        self.stack_values.pop(1)
        self.display_stack()

    def my_change_sign(self) -> None:
        # if not self.standardise_stack():
        #     return
        self.save_stack()
        s: str = self.my_entry.get()
        if len(s) > 0:
            if s.find('j') != -1:
                if s.find('+') > -1:
                    #  s = s.replace('j-', 'j')
                    s = s.replace('+', '-')
                else:
                    s = s.replace('-', '+')
                self.my_entry.replace_text(s)
            elif s[0] == '-':
                temp_str = s[1:]
                self.my_entry.replace_text(temp_str)
            else:
                self.my_entry.insert(0, '-')
        else:
            self.stack_values[0][0] = -self.stack_values[0][0]
            self.stack_values[0][1] = -self.stack_values[0][1]
        self.display_stack()

    def my_ceil(self) -> None:
        '''Round to the largest integer greater than or equal to R0 or R1.

        Round to the largest integer greater than or equal to R0 or R1.
        ceil(3.5) = 4
        ceil(-3.5) = -3
        For Complex numbers, both components are ceil'd.
        e.g. ceil(1.1+2.5j) = 2+3j
        '''
        if not self.standardise_stack():
            return
        self.save_stack()
        self.stack_values[0][0] = ceil(self.stack_values[0][0])
        self.stack_values[0][1] = ceil(self.stack_values[0][1])
        self.display_stack()

    def my_floor(self) -> None:
        '''Round to the largest integer smaller than or equal to E or R1.

        Round to the largest integer smaller than or equal to R0 or R1.
        floor(3.5) = 3
        floor(-3.5) = -4
        For complex numbers, both components are floor'd.
        e.g. floor(1.1+2.5j) = 1+2j.
        '''
        if not self.standardise_stack():
            return
        self.save_stack()
        self.stack_values[0][0] = floor(self.stack_values[0][0])
        self.stack_values[0][1] = floor(self.stack_values[0][1])
        self.display_stack()

    def my_int(self) -> None:
        '''Remove decimal part, leaving only the integer value.

        Removes the decimal part of either R0 or R1.
        int(3.5) = 3
        int(-3.5) = -3
        '''
        if not self.standardise_stack():
            return
        self.save_stack()
        self.stack_values[0][0] = trunc(self.stack_values[0][0])
        self.stack_values[0][1] = trunc(self.stack_values[0][1])
        self.display_stack()

    def my_dec(self) -> None:
        '''Remove integer portion, leaving only the decimal value.

        Removes the integer part of either R0 or R1.
        dec(3.5) = 0.5
        dec(-3.5) = -0.5
        '''
        if not self.standardise_stack():
            return
        self.save_stack()
        self.stack_values[0][0] = self.stack_values[0][0] - trunc(self.stack_values[0][0])
        self.stack_values[0][1] = self.stack_values[0][1] - trunc(self.stack_values[0][1])
        self.display_stack()

    def my_real(self) -> None:
        '''Remove imaginary portion, leaving only the real value.

        Removes the imaginary part of either R0 or R1 leaving
        just the real part.
        real(2+3.5j) = 2
        '''
        if not self.standardise_stack():
            return
        self.save_stack()
        self.stack_values[0][1] = 0.0
        self.display_stack()


    def my_imag(self) -> None:
        '''Remove real portion, leaving only the imaginary value.

        Removes the real part of either R0 or R1, leaving
        just the imaginary part.
        imag(2+3.5j) = 3.5j
        '''
        if not self.standardise_stack():
            return
        self.save_stack()
        self.stack_values[0][0] = 0.0
        self.display_stack()


    def my_conj(self) -> None:
        '''Take the conjugate of a complex number.

        Takes the conjugate of the complex number.
        conj(2+3.5j) = 2-3.5j
        '''
        if not self.standardise_stack():
            return
        self.save_stack()
        self.stack_values[0][1] = - self.stack_values[0][1]
        self.display_stack()

    def my_rtop(self) -> None:
        '''Convert rectangular to polar.

        X co-ordinate & Y co-ordinate are in either R0/R1 or R1/R2
        After conversion, distance & angle are in R1/R2
        '''
        if not self.standardise_stack():
            return
        x = self.stack_values[0][0]
        y = self.stack_values[1][0]
        if x < 0:
            a = pi
        else:
            a = 0
        self.save_stack()
        self.stack_values[0] = [sqrt(x ** 2 + y ** 2), 0.0, ' distance', {}]
        self.stack_values[1] = [(atan(y / x) + a) * self.radians_conv, 0.0, ' angle', {}]
        self.display_stack()

    def my_ptor(self) -> None:
        '''Convert polar to rectangular.

        distance & angle are in either R0/R1 or R1/R2
        '''
        if not self.standardise_stack():
            return
        d = self.stack_values[0][0]
        a = self.stack_values[1][0]
        self.save_stack()
        self.stack_values[0] = [d * cos(a / self.radians_conv), 0.0, ' x', {}]
        self.stack_values[1] = [d * sin(a / self.radians_conv), 0.0, ' y', {}]
        self.display_stack()

    def reset_trig_buttons(self) -> None:
        '''Resets trig button to default names and clears arc and hyp.

        Set the names on trig buttons to 'sin', 'cos', 'tan' & 'cas'.
        Set the arc and hyp button labels to blank.

        Parameters:

        Returns:
        --------
        Nothing
        '''
        self.arc_status = ''
        self.hyp_status = ''
        self.sin_button.configure(text='sin')
        self.cos_button.configure(text='cos')
        self.tan_button.configure(text='tan')
        self.cas_button.configure(text='cas')

    def arc_pressed(self) -> None:
        '''Processes the arc keypress.

        The arc button toggles the labels on the trig buttons, sin, cos,
        tan, cas, preceding tham with an a. E.G. asin, atan etc

        Parameters:

        Returns:
        --------
        Nothing
        '''
        if self.arc_status == '':
            self.arc_status = 'a'
        else:
            self.arc_status = ''
        self.sin_button.configure(text=self.arc_status + 'sin' + self.hyp_status)
        self.cos_button.configure(text=self.arc_status + 'cos' + self.hyp_status)
        self.tan_button.configure(text=self.arc_status + 'tan' + self.hyp_status)
        self.cas_button.configure(text=self.arc_status + 'cas' + self.hyp_status)

    def hyp_pressed(self) -> None:
        '''Processes the hyp keypress.

        The hyp button toggles the labels on the trig buttons, sin, cos,
        tan, cas, adding an h. e.g sinh, tanh.

        Parameters:

        Returns:
        --------
        Nothing

        '''
        if self.hyp_status == '':
            self.hyp_status = 'h'
        else:
            self.hyp_status = ''
        self.sin_button.configure(text=self.arc_status + 'sin' + self.hyp_status)
        self.cos_button.configure(text=self.arc_status + 'cos' + self.hyp_status)
        self.tan_button.configure(text=self.arc_status + 'tan' + self.hyp_status)
        self.cas_button.configure(text=self.arc_status + 'cas' + self.hyp_status)

    def my_complex(self) -> None:
        ''' Create a complex number from the top 2 items on the stack.

        The Complex button creates a complex number from the last 2 values entered. The values used
        can be complex numbers. Complex(a+jb, c+jd) is evaluated as (a+jb) + j(c+jd) -> (ac-bd) + j(ad+bc).

        Parameters:

        Returns:
        --------
        Nothing
        '''
        if not self.standardise_stack():
            return
        self.save_stack()
        a = self.stack_values[1][0] - self.stack_values[0][1]
        b = self.stack_values[0][0] + self.stack_values[1][1]
        self.stack_values[0][0] = a
        self.stack_values[0][1] = b
        self.stack_values[0][2] = self.stack_values[0][2] + ' ' + self.stack_values[1][2]
        self.stack_values[0][3] = {}
        self.stack_values.pop(1)
        self.display_stack()


    def trig_functions(self, button_label:str) -> None:
        ''' This is a jump off for trig functions. Executes the appropriate
            trig function based upon the button label.
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', button_label + '()')
            self.reset_trig_buttons()
            return
        if eval('self.my_' + button_label + '()') is None:
            self.reset_trig_buttons()
            self.display_stack()


    def my_sin(self) -> None:
        '''Calculate the Sine.

           Calculates the sine of the item in R0.
           Will honour the setting of the Deg/Rad/Grad button.

           Parameters:

           Returns:
               Nothing
        '''
        if not self.standardise_stack():
            return
        self.save_stack()
        if self.stack_values[0][1] == 0:  #  No complex part
            self.stack_values[0][0] = sin(self.stack_values[0][0] / self.radians_conv)
        else: #  complex
            z = c_sin(complex(self.stack_values[0][0], self.stack_values[0][1]))
            self.stack_values[0][0] = z.real
            self.stack_values[0][1] = z.imag
        self.reset_trig_buttons()
        self.display_stack()

    def my_asin(self) -> None:
        '''Calculate the ArcSine (Inverse Sine).

           Calculates the arcsine of the item in R0.
           Will honour the setting of the Deg/Rad/Grad button.

           Parameters:

           Returns:
               Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            if -1 <= self.stack_values[0][0] <= 1:
                self.save_stack()
                self.stack_values[0] = [asin(self.stack_values[0][0]) * self.radians_conv, 0.0, '', {}]
            else:
                popup_message.show(title='asin', message='Value must be from -1 to 1')
                return False
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_asin(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_sinh(self) -> None:
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [sinh(self.stack_values[0][0]), 0.0, '', {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_sinh(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_asinh(self) -> None:
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [asinh(self.stack_values[0][0]), 0.0, '', {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_asinh(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_cos(self) -> None:
        '''Calculate the cosine.

           Calculates the cosine of the item in R0.
           Will honour the setting of the Deg/Rad/Grad button.

           Parameters:

           Returns:
               Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [cos(self.stack_values[0][0] / self.radians_conv), 0.0, '', {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_cos(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_acos(self) -> None:
        '''Calculate the inverse cosine.

           Calculates the inverse cosine of the item in R0.
           Will honour the setting of the Deg/Rad/Grad button.

           Parameters:

           Returns:
               Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            if -1 <= self.stack_values[0][0] <= 1:
                self.save_stack()
                self.stack_values[0] = [acos(self.stack_values[0][0]) * self.radians_conv, 0.0, '', {}]
            else:
                popup_message.show(title='asin', message='Value must be from -1 to 1.')
                return False
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_acos(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_cosh(self) -> None:
        '''Calculate the hyperbolic cosine.

           Calculates the hyperbolic cosine of the item in R0.
           Will honour the setting of the Deg/Rad/Grad button.

           Parameters:

           Returns:
               Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [cosh(self.stack_values[0][0]), 0.0, '', {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_cosh(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_acosh(self) -> None:
        '''Calculate the inverse hyperbolic cosine.

           Calculates the inverse hyperbolic cosine of the item in R0.
           Will honour the setting of the Deg/Rad/Grad button.

           Parameters:

           Returns:
               Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [acosh(self.stack_values[0][0]), 0.0, '', {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_acosh(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_tan(self) -> None:
        '''Calculate the tangent.

           Calculates the tangent of the item in R0.
           Will honour the setting of the Deg/Rad/Grad button.

           Parameters:

           Returns:
               Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [tan(self.stack_values[0][0] / self.radians_conv), 0.0, '', {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_tan(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_atan(self) -> None:
        '''Calculate the inverse tangent.

           Calculates the inverse tangent of the item in R0.
           Will honour the setting of the Deg/Rad/Grad button.

           Parameters:

           Returns:
               Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [atan(self.stack_values[0][0]) * self.radians_conv, 0.0, '', {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_atan(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_tanh(self) -> None:
        '''Calculate the hyperbolic tangent.

           Calculates the hyperbolic tangent of the item in R0.
           Will honour the setting of the Deg/Rad/Grad button.

           Parameters:

           Returns:
               Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [tanh(self.stack_values[0][0]), 0.0, '', {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_tanh(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_atanh(self) -> None:
        '''Calculate the inverse hyperbolic tangent.

           Calculates the inverse hyperbolic tangentof the item in R0.
           Will honour the setting of the Deg/Rad/Grad button.

           Parameters:

           Returns:
               Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [atanh(self.stack_values[0][0]), 0.0, '', {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_atanh(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_cas(self) -> None:
        '''
        cas(x) = sin(x) + cos(x)

        Parameters:

        Returns:
            Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [sin(self.stack_values[0][0] / self.radians_conv) +
                                    cos(self.stack_values[0][0] / self.radians_conv), 0.0, '', {}]
        else: #  complex
            self.save_stack()
            z = c_sin(z) + c_cos(z)
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_acas(self):
        '''
        acas(x) = asin(x/sqrt(2)) - \u03C0/4
             \u00A0\u00A0Answer returned in range -\u03C0/4 \u2B0C \u03C0/4

        Parameters:

        Returns:
            Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            if -sqrt(2) <= self.stack_values[0][0] <= sqrt(2):
                self.save_stack()
                self.stack_values[0] = [(asin(self.stack_values[0][0] / sqrt(2)) - pi / 4) * self.radians_conv,
                                        0.0, '', {}]
            else:
                popup_message.show(title=acas, message='Value must be from -\u221a2 to \u221a2')
                return
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            self.save_stack()
            z = c_asin(z / (2 ** 0.5)) - (pi / 4)
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_cash(self):
        '''
        cash(x) = sinh(x) + cosh(x)

        Parameters:

        Returns:
            Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [sinh(self.stack_values[0][0]) + cosh(self.stack_values[0][0]), 0.0, '',
                                    {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            self.save_stack()
            z = c_sinh(z) + c_cosh(z)
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_acash(self):
        '''
        acash(x) = log(x)

        Parameters:

        Returns:
            Nothing
        '''
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:  #  No complex part
            self.save_stack()
            self.stack_values[0] = [sinh(self.stack_values[0][0]) + cosh(self.stack_values[0][0]), 0.0, '', {}]
        else: #  complex
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            self.save_stack()
            z = c_log(z)
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.reset_trig_buttons()
        self.display_stack()

    def my_square(self) -> None:
        '''Calculate the Square.

        Calculates the square of the item in R0.

        (a+bi)^2 = a^2 + 2abi + bi^2 = (a^2 - b^2), (2ab)

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', '**2')
            return
        if not self.standardise_stack():
            return
        a = self.stack_values[0][0]
        b = self.stack_values[0][1]
        self.save_stack()
        self.stack_values[0][0] = a * a - b * b
        self.stack_values[0][1] = 2 * a * b
        for key, value in self.stack_values[0][3].items(): #  Update units of measure
            self.stack_values[0][3][key] = 2 * value
        self.display_stack()

    def my_cubed(self) -> None:
        '''Calculate the Cube.

        Calculates the cube of the item in R0.

        (a + bi)^3 = a^3 + 3a^2b + 3b^2a+ b^3 = (a^3 + 3ab^2), (3ba^2 + b^3)

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', '**3')
            return
        if not self.standardise_stack():
            return
        a = self.stack_values[0][0]
        b = self.stack_values[0][1]
        self.save_stack()
        self.stack_values[0][0] = a * a * a - 3 * a * b * b
        self.stack_values[0][1] = 3 * a * a * b - b ** 3
        for key, value in self.stack_values[0][3].items(): #  Update units of measure
            self.stack_values[0][3][key] = 3 * value
        self.display_stack()

    def my_sqrt(self) -> None:
        '''Calculate the Square root.

        Calculates the square root of the item in R0.
        R0/R1 must be >= 0.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', 'sqrt()')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0: #  not Complex
            if self.stack_values[0][0] < 0.0:
                popup_message.show(title='my_sqrt', message='Value < 0')
                return
            else:
                self.save_stack()
                self.stack_values[0][0] = sqrt(self.stack_values[0][0])
        else:  #  Complex number
            a = self.stack_values[0][0]
            b = self.stack_values[0][1]
            mod = (a * a + b * b) ** 0.5
            self.save_stack()
            self.stack_values[0][0] = ((mod + a) / 2) ** 0.5
            self.stack_values[0][1] = copysign(1, b) * (((mod - a) / 2) ** 0.5)
        for key, value in self.stack_values[0][3].items(): #  Update units of measure
            v = value / 2
            if v == int(v):
                v = int(v)
            self.stack_values[0][3][key] = v
        self.display_stack()

    def my_inverse(self) -> None:
        '''Calculate the Inverse

        Calculates the inverse of the item in R0.
        R0/R1 must be != 0.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', '1/')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][0] == 0 and self.stack_values[0][1] == 0:
            popup_message.show(title='my_inverse', message='Divide by zero')
            return
        else:
            x = self.stack_values[0][0]
            y = self.stack_values[0][1]
            self.save_stack()
            self.stack_values[0][0] = x / (x * x + y * y)
            self.stack_values[0][1] = (y * -1) / (x * x + y * y)
            for key, value in self.stack_values[0][3].items():
                self.stack_values[0][3][key] = value * -1
        self.display_stack()

    def my_power_e(self) -> None:
        '''Calculate power of e

        Calculates e to the power of the item in R0.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', 'e**')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:
            if -709 <= self.stack_values[0][0] <= 709:
                self.save_stack()
                self.stack_values[0][0] = e ** self.stack_values[0][0]
            else:
                popup_message.show(title='exp', message='value must be from -709 to 709')
                return
        else:
            z = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_exp(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.display_stack()

    def my_power_10(self) -> None:
        '''Calculate power of 10

        Calculates the power of 10 of the item in R0.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', '10**')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:
            if self.stack_values[0][0] > 308:
                popup_message.show(title='power10', message='value must be <= 308')
                return
            else:
                self.save_stack()
                self.stack_values[0][0] = 10 ** self.stack_values[0][0]
        else:
            z = c_log(10) * (complex(self.stack_values[0][0], self.stack_values[0][1]))
            z = c_exp(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.display_stack()

    def my_power_2(self) -> None:
        '''Calculate power of 2

        Calculates the power of 2 of the item in R0.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', '2**')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:
            if self.stack_values[0][0] > 308:
                popup_message.show(title='power2', message='value must be <= 308')
                return
            else:
                self.save_stack()
                self.stack_values[0][0] = 2 ** self.stack_values[0][0]
        else:
            z = c_log(2) * (complex(self.stack_values[0][0], self.stack_values[0][1]))
            z = c_exp(z)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.display_stack()

    def my_log_e(self) -> None:
        '''Calculate base e log

        Calculates the base e log of the item in R0.
        R0/R1 must be greater than 0

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', 'log()')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:
            if self.stack_values[0][0] > 0:
                self.save_stack()
                self.stack_values[0][0] = log(self.stack_values[0][0])
            else:
                popup_message.show(title='my_log_e', message='Value must be > 0')
                return
        else:
            z = c_log(complex(self.stack_values[0][0], self.stack_values[0][1]))
            self.save_stack()
            self.stack_values[0][0] = z.real
            self.stack_values[0][1] = z.imag
        self.display_stack()

    def my_log_10(self) -> None:
        '''Calculate base 10 log

        Calculates the base 10 log of the item in R0.
        R0/R1 must be greater than 0

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', 'log10()')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:
            if self.stack_values[0][0] > 0:
                self.save_stack()
                self.stack_values[0] = [log10(self.stack_values[0][0]), 0.0, '', {}]
            else:
                popup_message.show(title='my_log_10', message='Value must be > 0')
                return
        else:
            z = c_log(complex(self.stack_values[0][0], self.stack_values[0][1]), 10)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.display_stack()

    def my_log_2(self) -> None:
        '''Calculate base 2 log

        Calculates the base 2 log of the item in R0.
        R0/R1 must be greater than 0

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', 'log2()')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0:
            if self.stack_values[0][0] > 0:
                self.save_stack()
                self.stack_values[0] = [log(self.stack_values[0][0]) / log(2), 0.0, '', {}]
            else:
                popup_message.show(title='my_log_2', message='Value must be > 0')
                return
        else:
            z = c_log(complex(self.stack_values[0][0], self.stack_values[0][1]), 2)
            self.save_stack()
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.display_stack()

    def my_multi_factorial(self) -> None:
        ''' Calculate the multifactorial of R0/R1 or R1/R2.

        Uses either R0 and R1 or R1 and R2 to calculate multifactorial.

        Formula or multifactorial(n, x) is n(n-x)(n-2x)...

        The first value entered is the number, the second is the number of ! marks. 10!!
        would be entered as 10 and then 2.

        10! = 10x9x8x7x6x5x4x3x2x1 = 3628800.
        10!! = 10x8x6x4x2 = 3840.
        10!!! = 10x7x4x1 = 280.
        10!!!! = 10x6x2 = 120.

        Parameters:

        Returns:
            Nothing
        '''

        def values_ok() -> bool:
            all_ok: bool = True
            msg: str = ''
            if self.stack_values[0][0] <= 0:
                msg +='R0 must be > 0.\n'
                all_ok = False
            if self.stack_values[1][0] < 0:
                msg += 'R1 must be >= 0.\n'
                all_ok = False
            if self.stack_values[0][0] != int(self.stack_values[0][0]):
                msg += 'R0 must be an integer.\n'
                all_ok = False
            if self.stack_values[1][0] != int(self.stack_values[1][0]):
                msg += 'R1 must be an integer.\n'
                all_ok = False
            if self.stack_values[1][0] > 170 or self.stack_values[0][0] > 170:
                msg += 'Value out of range, range is 1 to 170.\n'
                all_ok = False
            if not all_ok:
                popup_message.show(title='multi_factorial', message=msg[:-2])
            return all_ok

        def do_calculation(start: int, decrement: int) -> int:
            new_val = start
            answer = 1
            while new_val > 0:
                answer *= new_val
                new_val -= decrement
            return answer

        if not self.standardise_stack():
            return
        if values_ok():
            self.save_stack()
            self.stack_values[0] = [do_calculation(self.stack_values[1][0], self.stack_values[0][0]), 0.0, '', {}]
            self.stack_values.pop(1)
            self.display_stack()

    def my_factorial(self) -> None:
        '''Calculates the factorial.

        Uses the Gamma function to calculate the factorial of the item
        in R0.

        All numbers are supported, except negative integers.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', 'fact()')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] != 0:
            popup_message.show(title='Factorial', message='Cannot calculate factorial of a Complex number.')
            return
        if -170 <= self.stack_values[0][0] <= 170:
            try:
                temp_value = [gamma(self.stack_values[0][0] + 1), 0.0, '', {}]
            except ValueError:
                popup_message.show(title='Factorial', message='Cannot calculate factorial for negative integers.')
                return
            self.save_stack()
            self.stack_values[0] = temp_value
            self.display_stack()
        else:
            popup_message.show(title='Factorial', message='Value out of range, range is -170 to 170.')

    def my_subfactorial(self) -> None:
        '''Calculates the subfactorial.

        subfactorial n (!n) is the number of permutations of a set where no
        element appears in its original position.

        !n = floor(n!/e + 0.5)

        Integers from 1 to 170 are supported.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', 'subfactorial()')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] != 0:
            popup_message.show(title='subfactorial', message='Cannot calculate subfactorial of a Complex number.')
            return
        if self.stack_values[0][0] != int(self.stack_values[0][0]):
            popup_message.show(title='subfactorial', message='R0 must be an integer.')
        elif self.stack_values[0][0] < 1:
            popup_message.show(title='subfactorial', message='R0 must be >= 1.')
        elif self.stack_values[0][0] > 170:
            popup_message.show(title='subfactorial', message='R0 must be <= 170.')
        else:
            self.save_stack()
            self.stack_values[0] = [floor((gamma(self.stack_values[0][0] + 1) / e) + 0.5), 0.0, '', {}]
            self.display_stack()

    def my_power(self) -> None:
        '''Calculates R1 ** R0 or R2 ** R1.

        Calculates R1 ** R0 or R2 ** R1.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', '**')
            return
        if not self.standardise_stack():
            return
        self.save_stack()
        if self.stack_values[1][1] == 0 and self.stack_values[0][1] == 0:
            power = self.stack_values[0][0]
            self.stack_values[0][0] = self.stack_values[1][0] ** power
            self.stack_values[0][3] = self.stack_values[1][3].copy()
            for key, value in self.stack_values[0][3].items():
                self.stack_values[0][3][key] = int(value * power)
        else:
            z1 = complex(self.stack_values[0][0], self.stack_values[0][1])
            z2 = complex(self.stack_values[1][0], self.stack_values[1][1])
            z = c_exp(z1 * c_log(z2))
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.stack_values.pop(1)
        self.display_stack()

    def my_inv_power(self) -> None:
        '''Calculates R1 ** 1/R0 or R2 ** 1/R1.

        Calculates R1 ** 1 / R0 or R2 ** 1 / R1.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', '**(1/)')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][0] == 0.0:
            popup_message.show(title='my_inv_power', message='Divide by 0')
            return
        self.save_stack()
        if self.stack_values[1][1] == 0 and self.stack_values[0][1] == 0:
            power = 1 / self.stack_values[0][0]
            self.stack_values[0][0] = self.stack_values[1][0] ** power
            self.stack_values[0][3] = self.stack_values[1][3].copy()
            for key, value in self.stack_values[0][3].items():
                self.stack_values[0][3][key] = int(value * power)
        else:
            z1 = 1 / complex(self.stack_values[1][0], self.stack_values[1][1])
            z2 = complex(self.stack_values[0][0], self.stack_values[0][1])
            z = c_exp(z1 * c_log(z2))
            self.stack_values[0] = [z.real, z.imag, '', {}]
        self.stack_values.pop(1)
        self.display_stack()

    def my_add(self) -> None:
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', '+')
            return
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[-1] in 'Ee':
            self.my_entry.insert('end', '+')
            return
        if not self.standardise_stack():
            return
        self.save_stack()
        if self.stack_values[0][3] != self.stack_values[1][3]:
            popup_message.show(title='my_add', message='Mis-matched units, Cannot add.')
            return
        self.stack_values[0] = [self.stack_values[1][0] + self.stack_values[0][0],
                                self.stack_values[1][1] + self.stack_values[0][1],
                                '',
                                self.stack_values[0][3]]
        self.stack_values.pop(1)
        self.display_stack()

    def my_subtract(self) -> None:
        if len(self.my_entry.get()) > 0:
            if (self.my_entry.get()[0] == '=' or  #  Equation
                self.my_entry.get()[-1] in 'Ee' or #  Exp
                '@' in self.my_entry.get()): #  Units)
                self.my_entry.insert('end', '-')
                return
        if not self.standardise_stack():
            return
        self.save_stack()
        if self.stack_values[0][3] != self.stack_values[1][3]:
            popup_message.show(title='my_subtract', message='Mis-matched units, Cannot subtract.')
            return
        self.stack_values[0] = [self.stack_values[1][0] - self.stack_values[0][0],
                                self.stack_values[1][1] - self.stack_values[0][1],
                                '',
                                self.stack_values[0][3]]
        self.stack_values.pop(1)
        self.display_stack()

    def my_multiply(self) -> None:
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', '*')
            return
        if not self.standardise_stack():
            return
        a = self.stack_values[1][0]
        b = self.stack_values[1][1]
        c = self.stack_values[0][0]
        d = self.stack_values[0][1]
        self.save_stack()
        self.stack_values[0] = [a * c - b * d,
                                a * d + b * c,
                                '',
                                combine_uom(self.stack_values[0][3], self.stack_values[1][3], '+')]
        self.stack_values.pop(1)
        self.display_stack()

    def my_divide(self) -> None:
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', '/')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] == 0.0 and self.stack_values[1][1] == 0:  #  No complex numbers
            if self.stack_values[0][0] == 0.0:
                popup_message.show(title='my_divide', message='Divide by 0')
                return
            self.save_stack()
            self.stack_values[0][0] = self.stack_values[1][0] / self.stack_values[0][0]
            self.stack_values[0][2] = ''
            self.stack_values[0][3] = combine_uom(self.stack_values[0][3], self.stack_values[1][3], '-')
            self.stack_values.pop(1)
        else:
            a = self.stack_values[1][0]
            b = self.stack_values[1][1]
            c = self.stack_values[0][0]
            d = self.stack_values[0][1]
            l = c * c + d * d
            if l == 0:
                popup_message.show(title='my_divide', message='Complex divide by 0')
                return
            self.save_stack()
            self.stack_values[0] = [(a * c + b * d) / (c * c + d * d),
                                    (b * c - a * d) / (c * c + d * d),
                                    '',
                                    combine_uom(self.stack_values[0][3], self.stack_values[1][3], '-')]
            self.stack_values.pop(1)
        self.display_stack()

    def my_permutation(self) -> None:
        ''' Calculate nPr, permutations of n objects, r at a time.

        Uses either R0 and R1 or R1 and R2 to calculate permutations.

        Formula is n!/(n-x)!.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', 'perm(,)')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] != 0 or self.stack_values[1][1] != 0:
            popup_message.show(title='Permutation', message='Neither value can be complex.')
            return
        if self.stack_values[1][0] < self.stack_values[0][0]:
            popup_message.show(title='Permutation', message='Population must be >= Sample')
            return
        self.save_stack()
        self.stack_values[0] = [perm(int(self.stack_values[1][0]), int(self.stack_values[0][0])), 0.0, '', {}]
        self.stack_values.pop(1)
        self.display_stack()

    def my_combination(self) -> None:
        ''' Calculate nCr, combinations of n objects, r at a time.

        Uses either R0 and R1 or R1 and R2 to calculate combinations.

        Formula is n!/(n-x)!x!.

        Parameters:

        Returns:
            Nothing
        '''
        if len(self.my_entry.get()) > 0 and self.my_entry.get()[0] == '=':
            self.my_entry.insert('end', 'comb(,)')
            return
        if not self.standardise_stack():
            return
        if self.stack_values[0][1] != 0 or self.stack_values[1][1] != 0:
            popup_message.show(title='Combination', message='Neither value can be complex.')
            return
        if self.stack_values[1][0] < self.stack_values[0][0]:
            popup_message.show(title='Combination', message='Population must be >= Sample')
            return
        self.save_stack()
        self.stack_values[0] = [comb(int(self.stack_values[1][0]), int(self.stack_values[0][0])), 0.0, '', {}]
        self.stack_values.pop(1)
        self.display_stack()

    def my_radians(self) -> None:
        '''Toggles between Degrees, Radians and Grads.

        Toggles between Deg, Rad and Grads for the trig functions, sin,
        cos, tan, cas, RtoP and PtoR.

        Parameters:

        Returns:
            Nothing
        '''
        if self.radians_conv == 1:
            self.radians_button.configure(text='deg')
            self.radians_conv = 180 / pi
        elif self.radians_conv == 180 / pi:
            self.radians_button.configure(text='grad')
            self.radians_conv = 200 / pi
        else:
            self.radians_button.configure(text='rad')
            self.radians_conv = 1

    def insert_constant(self, the_constant: float, the_name: str = '', the_units: dict = {}) -> None:
        '''Places the_constant into the entry box.

        Parameters
        ----------
        the_constant float.

        Returns
        -------
            Nothing
        '''
        if len(self.stack_values) == 10:
            self.stack_values.pop()
        self.stack_values.insert(0, [the_constant, 0.0, the_name, the_units])
        self.display_stack()

    def clicked_it(self, the_button: str) -> None:
        self.my_entry.insert('end', the_button)
        self.my_entry.focus_set()

    def file_path_info(self) -> None:
        '''Print filepath info'''
        path_info = (f'my_cwd={getcwd()}\nmy_path={dirname(realpath(argv[0]))}\n'
                     f'argv[0]={argv[0].replace('\\\\','\\')}\n'
                     f'__file__={__file__}\n'
                     f'my_file_path={first_bit.my_file_path}\n'
                     f'my_file_type={first_bit.what_i_am}')
        popup_message.show(title='File and Path info', message=path_info, multi_line=True, alignment=LEFT)


class Finance:
    '''Financial functions'''

    def __init__(self, my_frame):
        self.my_frame = my_frame
        self.calculation_type = IntVar()
        self.rb1 = CTkRadioButton(self.my_frame,
                                  text='Mortgage Repayments',
                                  variable=self.calculation_type,
                                  value=1)
        self.rb1.grid(row=0, column=0, columnspan=2, sticky='w')
        self.rb2 = CTkRadioButton(self.my_frame,
                                  text='Compound Interest',
                                  variable=self.calculation_type,
                                  value=2)
        self.rb2.grid(row=1, column=0, columnspan=2, sticky='w')
        self.rb3 = CTkRadioButton(self.my_frame,
                                  text='Simple Interest',
                                  variable=self.calculation_type,
                                  value=3)
        self.rb3.grid(row=2, column=0, columnspan=2, sticky='w')
        self.calculation_type.set(1)
        CTkLabel(self.my_frame, text='Principal').grid(row=4, column=0, sticky='e')
        self.e_principal = CTkEntry(self.my_frame)
        self.e_principal.grid(row=4, column=1)
        CTkLabel(self.my_frame, text='Rate (p.a)').grid(row=5, column=0, sticky='e')
        self.e_rate = CTkEntry(self.my_frame)
        self.e_rate.grid(row=5, column=1)
        CTkLabel(self.my_frame, text='Years').grid(row=6, column=0, sticky='e')
        self.e_years = CTkEntry(self.my_frame)
        self.e_years.grid(row=6, column=1)
        CTkLabel(self.my_frame, text='Interest').grid(row=7, column=0, sticky='e')
        self.e_interest = CTkEntry(self.my_frame)
        self.e_interest.grid(row=7, column=1)
        CTkLabel(self.my_frame, text='Monthly Payment').grid(row=8, column=0, sticky='e')
        self.e_monthly = CTkEntry(self.my_frame)
        self.e_monthly.grid(row=8, column=1)
        CTkLabel(self.my_frame, text='Weekly Payment').grid(row=9, column=0, sticky='e')
        self.e_weekly = CTkEntry(self.my_frame)
        self.e_weekly.grid(row=9, column=1)
        CTkLabel(self.my_frame, text='Total').grid(row=10, column=0, sticky='e')
        self.e_total = CTkEntry(self.my_frame)
        self.e_total.grid(row=10, column=1)
        self.interest_button = CTkButton(self.my_frame,
                                         text='Calculate',
                                         command=lambda: self.financial_calculation())
        self.interest_button.grid(row=11, column=1, sticky='w')
        self.intclear_button = CTkButton(self.my_frame,
                                         text='Clear Form',
                                         command=lambda: self.clear_int_form('all'))
        self.intclear_button.grid(row=12, column=1, sticky='w')
        self.my_frame.grid()

    def simple_interest(self, principal: float, rate: float, time: float) -> tuple[float, float]:
        interest_earned: float = principal * rate / 100 * time
        final_value: float = principal + interest_earned
        return interest_earned, final_value

    def compound_interest(self, principal: float, rate: float, time: float) -> tuple[float, float]:
        final_value: float = principal * ((1 + rate / 100) ** time)
        interest_earned: float = final_value - principal
        return interest_earned, final_value

    def mortgage(self, loan: float, rate: float, years: float) -> tuple[float, float, float]:
        mrate: float = rate / 100 / 12
        months = years * 12
        payment: float = loan * mrate * ((1 + mrate) ** months) / (((1 + mrate) ** months) - 1)
        return payment, payment * months - loan, payment * months

    def clear_int_form(self, fields: str = 'outputonly') -> None:
        if fields != 'outputonly':
            self.e_principal.delete(0, 'end')
            self.e_rate.delete(0, 'end')
            self.e_years.delete(0, 'end')
        self.e_interest.delete(0, 'end')
        self.e_monthly.delete(0, 'end')
        self.e_weekly.delete(0, 'end')
        self.e_total.delete(0, 'end')

    def financial_calculation(self) -> None:
        self.e_principal.configure(text_color='black', fg_color='white')
        self.e_rate.configure(text_color='black', fg_color='white')
        self.e_years.configure(text_color='black', fg_color='white')
        if self.e_principal.get() == '' or self.e_rate.get() == '' or self.e_years.get() == '':
            popup_message.show(title='Entry error', message='Not all fields have been entered',)
            return
        principal_err = rate_err = year_err = False
        try:
            float(self.e_principal.get())
        except ValueError:
            principal_err = True
            self.e_principal.configure(text_color='red', fg_color='pink')
        try:
            float(self.e_rate.get())
        except ValueError:
            rate_err = True
            self.e_rate.configure(text_color='red', fg_color='pink')
        try:
            float(self.e_years.get())
        except ValueError:
            year_err = True
            self.e_years.configure(text_color='red', fg_color='pink')
        if principal_err or rate_err or year_err:
            popup_message.show(title='Entry error', message='Values MUST be numeric', x_pos=0.5, y_pos=0.2)
            if principal_err:
                self.e_principal.delete(0, 'end')
                self.e_principal.configure(text_color='blue', fg_color='lightyellow')
            if rate_err:
                self.e_rate.delete(0, 'end')
                self.e_rate.configure(text_color='blue', fg_color='lightyellow')
            if year_err:
                self.e_years.delete(0, 'end')
                self.e_years.configure(text_color='blue', fg_color='lightyellow')
            if year_err:
                self.e_years.focus()
            if rate_err:
                self.e_rate.focus()
            if principal_err:
                self.e_principal.focus()
            return
        self.clear_int_form()
        match self.calculation_type.get():
            case 1:
                m, i, t = self.mortgage(float(self.e_principal.get()),
                                        float(self.e_rate.get()),
                                        float(self.e_years.get()))
                self.e_interest.insert('end', str(round(i, 2)))
                self.e_monthly.insert('end', str(round(m, 2)))
                self.e_weekly.insert('end', str(round(m * 12 / 52, 2)))
                self.e_total.insert('end', str(round(t, 2)))
            case 2:
                i, t = self.compound_interest(float(self.e_principal.get()),
                                              float(self.e_rate.get()),
                                              float(self.e_years.get()))
                self.e_interest.insert('end', str(round(i, 2)))
                self.e_monthly.insert('end', '')
                self.e_total.insert('end', str(round(t, 2)))
            case 3:
                i, t = self.simple_interest(float(self.e_principal.get()),
                                            float(self.e_rate.get()),
                                            float(self.e_years.get()))
                self.e_interest.insert('end', str(round(i, 2)))
                self.e_monthly.insert('end', '')
                self.e_total.insert('end', str(round(t, 2)))
            case _:
                print('self.calculation_type:' + str(self.calculation_type.get()))
        equation_string = (''.join(['I_Principal=', self.e_principal.get(), ';I_Rate=', self.e_rate.get(),
                                    ';I_Years=', self.e_years.get(), ';I_Interest=', self.e_interest.get(),
                                    ';I_Total=', self.e_total.get()]))

        equation_string_1 = self.e_monthly.get()
        if equation_string_1 == '':
            equation_string_1 = '\'\''
        equation_string += ';I_Monthly=' + equation_string_1
        app.scientific.other_equals(equation_string)
        self.e_principal.focus()


class Statistics:
    '''Statistics functions'''

    def __init__(self, my_frame):
        self.my_frame = my_frame
        self.previous_modes: str = ''
        self.data_entry = CTkEntry(self.my_frame)
        self.data_entry.bind('<Return>', (lambda event: self.statistics_calculation()))
        self.data_entry.MyID = 'DataEntry'
        data_label = CTkLabel(self.my_frame, text='Data')
        data_label.MyID = 'DataEntry'
        num_label = CTkLabel(self.my_frame, text='Number of Items (n)')
        self.num_items = CTkEntry(self.my_frame)
        sum_label = CTkLabel(self.my_frame, text='Sum (\u03A3x)')
        self.sum_items = CTkEntry(self.my_frame)
        mean_label = CTkLabel(self.my_frame, text='Mean (\u03BCx)')
        self.mean_items = CTkEntry(self.my_frame)
        mode_label = CTkLabel(self.my_frame, text='Mode (Mo)')
        self.mode_items = CTkEntry(self.my_frame)
        median_label = CTkLabel(self.my_frame, text='Median (x\u0303)')
        self.median_items = CTkEntry(self.my_frame)
        rms_label = CTkLabel(self.my_frame, text='RMS')
        self.rms_items = CTkEntry(self.my_frame)
        pstddev_label = CTkLabel(self.my_frame,
                                 text='Population Standard Deviation (\u03C3)',
                                 justify=RIGHT)
        self.pstddev_entry = CTkEntry(self.my_frame)
        sstddev_label = CTkLabel(my_frame, text='Sample Standard Deviation (s)',
                                 justify=RIGHT)
        self.sstddev_entry = CTkEntry(self.my_frame)
        sumsq_label = CTkLabel(self.my_frame,
                               text='Sum of Squares (\u03A3x\N{SUPERSCRIPT TWO})',
                               justify=RIGHT)
        self.sumsq_entry = CTkEntry(self.my_frame)
        geomean_label = CTkLabel(self.my_frame, text='Geometric Mean (GM)')
        geomean_label.MyID = 'GM'
        self.geom_entry = CTkEntry(self.my_frame)
        harmmean_label = CTkLabel(self.my_frame, text='Harmonic Mean (HM)')
        harmmean_label.MyID = 'HM'
        self.harm_entry = CTkEntry(self.my_frame)
        self.calc_button = CTkButton(self.my_frame,
                                     text='Calculate',
                                     command=lambda: self.statistics_calculation())
        self.stat_clear_button = CTkButton(self.my_frame,
                                           text='Clear Form',
                                           command=lambda: self.clear_stat_form('all'))
        data_label.grid(row=0, column=0, sticky='e')
        self.data_entry.grid(row=0, column=1, columnspan=3)
        num_label.grid(row=1, column=0, sticky='e')
        self.num_items.grid(row=1, column=1)
        sum_label.grid(row=2, column=0, sticky='e')
        self.sum_items.grid(row=2, column=1)
        mean_label.grid(row=3, column=0, sticky='e')
        self.mean_items.grid(row=3, column=1)
        mode_label.grid(row=4, column=0, sticky='e')
        self.mode_items.grid(row=4, column=1)
        median_label.grid(row=5, column=0, sticky='e')
        self.median_items.grid(row=5, column=1)
        rms_label.grid(row=6, column=0, sticky='e')
        self.rms_items.grid(row=6, column=1)
        pstddev_label.grid(row=7, column=0, sticky='e')
        self.pstddev_entry.grid(row=7, column=1)
        sstddev_label.grid(row=8, column=0, sticky='e')
        self.sstddev_entry.grid(row=8, column=1)
        sumsq_label.grid(row=9, column=0, sticky='e')
        self.sumsq_entry.grid(row=9, column=1)
        geomean_label.grid(row=10, column=0, sticky='e')
        self.geom_entry.grid(row=10, column=1)
        harmmean_label.grid(row=11, column=0, sticky='e')
        self.harm_entry.grid(row=11, column=1)
        self.calc_button.grid(row=12, column=1)
        self.stat_clear_button.grid(row=13, column=1)
        my_frame.grid()

    def statistics_calculation(self) -> None:
        string = self.data_entry.get().replace(',', ' ').replace(';', ' ').strip()
        if string == '':
            popup_message.show(title='Stats', message='No data entered')
            # app.my_message.popup_msg('Stats', 'No data entered')
            return
        self.clear_stat_form()
        ss = split(r'\s+', string)
        ssn = ''
        for s in ss:
            ssn += s + ' '
        self.data_entry.replace_text(ssn)
        err_str = ''
        floats = []
        for _1 in ss:
            try:
                floats.append(float(_1))
            except ValueError:
                err_str += str(_1) + ' '
        if err_str != '':
            popup_message.show(title='Stats', message='Invalid number(s) entered: ' + err_str)
            return
        if len(floats) == 1:
            popup_message.show(title='Stats', message='Need more than 1 value.')
            return
        product = 1
        pcount = 0
        tot = 0
        tcount = 0
        sqtot = 0
        hm = 0
        list_of_values: list[float] = []
        for _1 in floats:
            list_of_values.append(_1)
            if _1 > 0:  #  Exclude negative numbers and zero for Geometric Mean
                product *= _1
                hm += 1 / _1
                pcount += 1
            tot += _1
            sqtot += _1 ** 2
            tcount += 1
        modes = multimode(list_of_values)
        self.mode_items.insert('end', modes)
        self.median_items.insert('end', median(list_of_values))
        sumdev = 0
        for _1 in floats:
            sumdev += (_1 - (tot / tcount)) ** 2
        self.num_items.insert('end', tcount)
        self.sum_items.insert('end', round(tot, 2))
        self.mean_items.insert('end', round(tot / tcount, 2))
        self.pstddev_entry.insert('end', round((sumdev / tcount) ** 0.5, 2))
        self.sstddev_entry.insert('end', round((sumdev / (tcount - 1)) ** 0.5, 2))
        self.sumsq_entry.insert('end', sqtot)
        self.geom_entry.insert('end', round(product ** (1 / pcount), 2))
        self.harm_entry.insert('end', round(pcount / hm, 2))
        self.rms_items.insert('end', round((sqtot / tcount) ** 0.5, 2))
        if len(self.previous_modes) > 0:
            app.scientific.other_equals(self.previous_modes)
            self.previous_modes = ''
        equation_string = ('S_Num=' + self.num_items.get() + ';S_Sum=' + self.sum_items.get() +
                           ';S_Mean=' + self.mean_items.get())
        self.previous_modes = 'S_Num=\'\';S_Sum=\'\';S_Mean=\'\''
        if len(modes) == 1:
            equation_string += ';S_Mode=' + self.mode_items.get()
            self.previous_modes += ';S_Mode=\'\''
        else:
            #  We define a variable for each mode found.
            i = 1
            for _1 in modes:
                equation_string += ';S_Mode' + str(i) + '=' + str(_1)
                self.previous_modes += ';S_Mode' + str(i) + '=' + '\'\''
                i += 1
        equation_string += (''.join([';S_Median=', self.median_items.get(),
                                     ';S_Popstddev=', self.pstddev_entry.get(),
                                     ';S_Samstddev=', self.sstddev_entry.get(),
                                     ';S_Sumsq=', self.sumsq_entry.get(),
                                     ';S_GM=', self.geom_entry.get(),
                                     ';S_HM=', self.harm_entry.get(),
                                     ';S_RMS=', self.rms_items.get()]))
        self.previous_modes += ';S_Median=\'\';S_Popstddev=\'\';S_Samstddev=\'\';S_Sumsq=\'\';S_GM=\'\';S_HM=\'\';S_RMS=\'\''
        app.scientific.other_equals(equation_string)

    def clear_stat_form(self, fields: str = 'outputonly') -> None:
        '''

        :param fields: <The fields to be cleared>
        :type fields: string
        :return: nothing
        '''
        if fields != 'outputonly':
            self.data_entry.delete(0, 'end')
        self.num_items.delete(0, 'end')
        self.sum_items.delete(0, 'end')
        self.mean_items.delete(0, 'end')
        self.mode_items.delete(0, 'end')
        self.median_items.delete(0, 'end')
        self.rms_items.delete(0, 'end')
        self.pstddev_entry.delete(0, 'end')
        self.sstddev_entry.delete(0, 'end')
        self.sumsq_entry.delete(0, 'end')
        self.geom_entry.delete(0, 'end')
        self.harm_entry.delete(0, 'end')


class Converter:
    '''Conversion functions'''

    def __init__(self, my_frame):
        self.my_frame = my_frame
        self.units_dictionary: dict = None
        self.input_field = CTkEntry(master=self.my_frame)
        self.input_field.grid(row=2, column=3)
        self.output_field = CTkEntry(master=self.my_frame)
        self.output_field.grid(row=3, column=3)
        button_config = {'corner_radius': 0,
                         'width': BUTTON_WIDTH,
                         'height': BUTTON_HEIGHT,
                         'border_width': 1,
                         'border_spacing': 0,
                         'hover_color': 'aquamarine',
                         'fg_color': 'peachpuff',
                         'text_color': 'blue',
                         'border_color': 'red',
                         'background_corner_colors': ('mint cream',
                                                      'mint cream',
                                                      'mint cream',
                                                      'mint cream'),
                         'font': ('Roboto Mono Medium', -13)}
        self.convert_from_button = CTkButton(master=self.my_frame,
                                             text='From',
                                             command=self.popup_from_menu,
                                             **button_config)
        self.convert_from_button.grid(row=2, column=4, sticky='news')
        self.convert_to_button = CTkButton(master=self.my_frame,
                                           text='To',
                                           command=self.popup_to_menu,
                                           **button_config)
        self.convert_to_button.grid(row=3, column=4, sticky='news')
        label_config = {'corner_radius': 0,
                        'width': BUTTON_WIDTH / 2,
                        'height': BUTTON_HEIGHT,
                        'fg_color': 'firebrick1',
                        'text_color': 'yellow2',
                        'font': ('Roboto Mono Medium', -13)}
        self.current_unit = CTkLabel(master=self.my_frame,
                                     text='current_unit',
                                     **label_config)
        self.current_unit.grid(row=1, column=3)
        label_config = {'corner_radius': 0,
                        'width': BUTTON_WIDTH / 2,
                        'height': BUTTON_HEIGHT,
                        'fg_color': 'khaki',
                        'text_color': 'blue',
                        'font': ('Roboto Mono Medium', -13)}
        self.from_label = CTkLabel(master=self.my_frame,
                                   text='From',
                                   **label_config)
        self.from_label.grid(row=2, column=2)
        self.to_label = CTkLabel(master=self.my_frame,
                                 text='To',
                                 **label_config)
        self.to_label.grid(row=3, column=2)
        row_num = 2
        length_button = CTkButton(master=self.my_frame,
                                  text='Length',
                                  command=self.length_conversion,
                                  **button_config)
        length_button.grid(row=row_num, column=1, sticky='news')
        row_num += 1
        quantity_button = CTkButton(master=self.my_frame,
                                    text='Quantity',
                                    command=self.quantity_conversion,
                                    **button_config)
        quantity_button.grid(row=row_num, column=1, sticky='news')
        row_num += 1
        mass_button = CTkButton(master=self.my_frame,
                                text='Mass',
                                command=self.mass_conversion,
                                **button_config)
        mass_button.grid(row=row_num, column=1, sticky='news')
        row_num += 1
        time_button = CTkButton(master=self.my_frame,
                                text='Time',
                                command=self.time_conversion,
                                **button_config)
        time_button.grid(row=row_num, column=1, sticky='news')
        row_num += 1
        temperature_button = CTkButton(master=self.my_frame,
                                       text='Temperature',
                                       command=self.temperature_conversion,
                                       **button_config)
        temperature_button.grid(row=row_num, column=1, sticky='news')
        row_num += 1
        area_button = CTkButton(master=self.my_frame,
                                text='Area',
                                command=self.area_conversion,
                                **button_config)
        area_button.grid(row=row_num, column=1, sticky='news')
        row_num += 1
        speed_button = CTkButton(master=self.my_frame,
                                 text='Speed',
                                 command=self.speed_conversion,
                                 **button_config)
        speed_button.grid(row=row_num, column=1, sticky='news')
        row_num += 1
        volume_button = CTkButton(master=self.my_frame,
                                  text='Volume',
                                  command=self.volume_conversion,
                                  **button_config)
        volume_button.grid(row=row_num, column=1, sticky='news')
        row_num += 1
        energy_button = CTkButton(master=self.my_frame,
                                  text='Energy',
                                  command=self.energy_conversion,
                                  **button_config)
        energy_button.grid(row=row_num, column=1, sticky='news')
        row_num += 1
        force_button = CTkButton(master=self.my_frame,
                                 text='Force',
                                 command=self.force_conversion,
                                 **button_config)
        force_button.grid(row=row_num, column=1, sticky='news')
        row_num += 1
        digital_storage_button = CTkButton(master=self.my_frame,
                                           text='Digital\nStorage',
                                           command=self.digital_storage_conversion,
                                           **button_config)
        digital_storage_button.grid(row=row_num, column=1, sticky='news')
        convcalc_button = CTkButton(master=self.my_frame,
                                    text='Calculate',
                                    command=self.conversion_calculation,
                                    **button_config)
        convcalc_button.grid(row=4, column=3, sticky='news')
        swap_units_button = CTkButton(master=self.my_frame,
                                      text='Swap Units',
                                      command=self.swap_units,
                                      **button_config)
        swap_units_button.grid(row=5, column=3, sticky='news')
        show_units_button = CTkButton(master=self.my_frame,
                                      text='Show Units',
                                      command=self.show_units,
                                      **button_config)
        show_units_button.grid(row=6, column=3, sticky='news')

        my_frame.grid()
        self.length_conversion()
        self.conversion_calculation()

    def popup_from_menu(self) -> None:
        x = self.convert_from_button.winfo_rootx()
        y = self.convert_from_button.winfo_rooty()
        self.popup_from.tk_popup(x, y, 0)

    def popup_to_menu(self) -> None:
        x = self.convert_to_button.winfo_rootx()
        y = self.convert_to_button.winfo_rooty()
        self.popup_to.tk_popup(x, y, 0)

    def conversion_calculation(self) -> None:
        '''Does the actual conversion between units.'''
        if self.input_field.get() == '':
            self.input_field.insert('end', 1)
        try:
            self.from_value = float(self.input_field.get())
        except ValueError as v:
            popup_message.show(title='Converter', message='Invalid From value supplied, ' + str(v))
            return
        self.from_factor = self.convert_from_button.cget('text')
        self.to_factor = self.convert_to_button.cget('text')
        #  Temperature is not a 1 for 1 conversion. Rather than converting between all possible
        #  temperature units, convert the From unit to Celsius and then convert that to the To unit.
        if self.current_unit.cget('text') == 'Temperature':
            match self.from_factor:
                case '\u00B0Celsius':
                    temp_value = self.from_value
                case '\u00B0Kelvin':
                    temp_value = self.from_value - 273.15
                case '\u00B0Fahrenheit':
                    temp_value = (self.from_value - 32) * 5 / 9
                case '\u00B0Rankine':
                    temp_value = (self.from_value - 491.67) * 5 / 9
                case '\u00B0Reamur':
                    temp_value = self.from_value * 5 / 4
                case _:
                    temp_value = 0
            if temp_value < -273.15:
                popup_message.show(title='Temperature value',
                              message='Cannot be less than absolute zero. \u00B0Kelvin')
                return
            #  Convert the degrees C value to the to_factor
            match self.to_factor:
                case '\u00B0Celsius':
                    self.to_value = temp_value
                case '\u00B0Kelvin':
                    self.to_value = temp_value + 273.15
                case '\u00B0Fahrenheit':
                    self.to_value = temp_value * 9 / 5 + 32
                case '\u00B0Rankine':
                    self.to_value = (temp_value * 9 / 5) + 491.67
                case '\u00B0Reamur':
                    self.to_value = temp_value * 4 / 5
                case _:
                    self.to_value = 0
        else:
            self.to_value = float(
                self.from_value * self.units_dictionary[self.from_factor] / self.units_dictionary[self.to_factor])
        format_str = '{:.' + str(app.scientific.settings_dict['significant_digits']) + 'g}'
        self.output_field.replace_text(format_str.format(self.to_value))

    def set_button_text(self, bt, txt) -> None:
        '''Sets button text for bt to the values of txt variable.'''
        if bt == 'from':
            self.convert_from_button.configure(text=txt)
        else:
            self.convert_to_button.configure(text=txt)
        self.conversion_calculation()

    def setup_conversion_menu(self, name: str = None) -> None:
        if name is None:
            calling_def = currentframe().f_back.f_code.co_name
            calling_def = list(calling_def.rsplit('_'))[0].title()
            self.current_unit.configure(text=calling_def)
        else:
            self.current_unit.configure(text=name)
        self.popup_from = Menu(self.my_frame, tearoff=0)
        self.popup_to = Menu(self.my_frame, tearoff=0)
        sub_menu = False
        cascade_1 = ''
        cascade_2 = ''
        for keys, values in self.units_dictionary.items():
            if keys[0] == '>':  #  Create submenu
                sub_menu = True
                cascade_1 = Menu(self.my_frame, tearoff=0)
                cascade_2 = Menu(self.my_frame, tearoff=0)
                if values == '':
                    label_value = 'Submenu'
                else:
                    label_value = values
                self.popup_from.add_cascade(label=label_value, menu=cascade_1, foreground='blue',
                                            background='cornsilk')
                self.popup_to.add_cascade(label=label_value, menu=cascade_2, foreground='blue',
                                          background='cornsilk')
            elif keys[0] == '<':  #  End submenu
                sub_menu = False
            else:
                if sub_menu:
                    if keys[0] == '-':
                        cascade_1.add_separator()
                        cascade_2.add_separator()
                    else:
                        cascade_1.add_command(label=keys,
                                              command=lambda ssk=keys: self.set_button_text('from', ssk))
                        cascade_2.add_command(label=keys,
                                              command=lambda ssk=keys: self.set_button_text('to', ssk))
                else:
                    if keys[0] == '-':
                        self.popup_from.add_separator()
                        self.popup_to.add_separator()
                    else:
                        self.popup_from.add_command(label=keys,
                                                    command=lambda ssk=keys: self.set_button_text('from', ssk))
                        self.popup_to.add_command(label=keys,
                                                  command=lambda ssk=keys: self.set_button_text('to', ssk))
        if list(self.units_dictionary.keys())[0][0] == '>':  #  First dict item is a menu
            first_unit = 1
            second_unit = 2
        else:
            first_unit = 0
            second_unit = 1
        self.convert_from_button.configure(text=list(self.units_dictionary.keys())[first_unit])
        self.convert_to_button.configure(text=list(self.units_dictionary.keys())[second_unit])
        if self.input_field.get() == '':
            self.input_field.insert('end', 1)
        self.conversion_calculation()

    def swap_units(self) -> None:
        '''Swaps the from and to buttons.

        Swaps the units on the from and to buttons, so that the calculation
        can be performed in reverse.

        Parameters:

        Returns:
            Nothing
        '''
        btext = self.convert_from_button.cget('text')
        self.convert_from_button.configure(text=self.convert_to_button.cget('text'))
        self.convert_to_button.configure(text=btext)
        Converter.conversion_calculation(self)

    def show_units(self) -> None:
        '''Shows the units available.

        Lists the current available unit names and the conversion factor.

        Parameters:

        Returns:
            Nothing
        '''
        unit_counter: int = 0
        base_unit: str = ''
        output_string: str = ''
        for keys, values in self.units_dictionary.items():
            if keys[0] not in '<>-':
                if unit_counter == 0:
                    output_string += f'Base unit = {keys}\n'
                    base_unit = keys
                else:
                    if self.current_unit.cget('text') == 'Temperature':
                        output_string += f'\n{keys}'
                    else:
                        output_string += f'\n1 {keys} = {values} {base_unit}'
                unit_counter += 1
        popup_message.show(title=self.current_unit.cget('text'), message=output_string)

    def quantity_conversion(self) -> None:
        '''Sets up length conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'Unit': 1,
                                 'Dozen': 12,
                                 'Pair': 2,
                                 '\u00BD-Dozen': 6,
                                 'Brace': 2,
                                 'Baker''s Dozen': 13,
                                 'Score': 20,
                                 'Gross': 144}
        self.setup_conversion_menu()

    def length_conversion(self) -> None:
        '''Sets up length conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'m': 1,
                                 'cm': 0.01,
                                 'mm': 0.001,
                                 'km': 1000,
                                 'au': 149597870700,
                                 'ly': 9.4607304725808E15,
                                 'parsec': 3.0856778570831E16,
                                 'inch': 0.0254,
                                 'ft': 0.3048,
                                 'yd': 0.9144,
                                 'mile': 1609.344,
                                 '>1': 'Other Metric Units',
                                 'micron': 1e-6,
                                 '<1': '',
                                 'fathom': 1.8288,
                                 '>2': 'Other Imperial Units',
                                 'twip': 0.0000176389,
                                 'thou': 0.0000254,
                                 'barleycorn': 0.0084667,
                                 'hand': 0.1016,
                                 'foot': 0.3048,
                                 'yard': 0.9144,
                                 'chain': 20.1168,
                                 'furlong': 201.168,
                                 '<2': '',
                                 'metre': 1,
                                 'kilometre': 1000}
        self.setup_conversion_menu()

    def mass_conversion(self) -> None:
        '''Sets up mass conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'kg': 1,
                                 'g': .001,
                                 'oz': 0.02834952,
                                 'lb': 0.45359237,
                                 'stone': 6.35029318,
                                 'tonne': 1000,
                                 'ton (US)': 907,
                                 'ton (UK)': 1016,
                                 'quintal': 100,
                                 'dalton': 1.66e-27}
        self.setup_conversion_menu()

    def time_conversion(self) -> None:
        '''Sets up time conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'s': 1,
                                 'ms': .001,
                                 'm': 60,
                                 'h': 3600,
                                 'd': 86400,
                                 'w': 604800,
                                 'y': 31556952,
                                 'fortnight': 1209600,
                                 '\u03BCfortnight': 1.2096}
        self.setup_conversion_menu()

    def temperature_conversion(self) -> None:
        '''Sets up temperature conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'\u00B0Celsius': '',
                                 '\u00B0Kelvin': '',
                                 '\u00B0Fahrenheit': '',
                                 '\u00B0Rankine': '',
                                 '\u00B0Reamur': ''}
        self.setup_conversion_menu()

    def area_conversion(self) -> None:
        '''Sets up area conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'m\N{SUPERSCRIPT TWO}': 1,
                                 'km\N{SUPERSCRIPT TWO}': 1000000,
                                 'Hectare': 10000,
                                 'Acre': 4046.8564224,
                                 '>1': 'Imperial Units',
                                 'barn': 1E-28,
                                 '<1': ''}
        self.setup_conversion_menu()

    def speed_conversion(self) -> None:
        '''Sets up speed conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'m/s': 1,
                                 'km/h': 27 / 99,
                                 'mph': 0.44704,
                                 'cm/s': .01,
                                 'fps': .3048,
                                 'knot': 1852 / 3600}
        self.setup_conversion_menu()

    def volume_conversion(self) -> None:
        '''Sets up volume conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'m\N{SUPERSCRIPT THREE}': 1,
                                 'l': 0.001,
                                 'cubic yard': 0.9144 ** 3,
                                 'ukgal': 0.00454609,
                                 'usgal': 0.00378541}
        self.setup_conversion_menu()

    def energy_conversion(self) -> None:
        '''Sets up energy conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'j': 1,
                                 'kCal': 4184,
                                 'FoodCal': 4.184}
        self.setup_conversion_menu()

    def force_conversion(self) -> None:
        '''Sets up force conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'N': 1,
                                 'Dyne': 0.00001}
        self.setup_conversion_menu()

    def digital_storage_conversion(self) -> None:
        '''Sets up digital stoage conversion.

        Parameters:

        Returns:
            Nothing
        '''
        self.units_dictionary = {'byte': 1,
                                 'bit': .125,
                                 'crumb': .25,
                                 'nibble': .5,
                                 '-1': '',
                                 'KB': 1000,
                                 'MB': 1000000,
                                 'GB': 10 ** 9,
                                 'TB': 10 ** 12,
                                 'PB': 10 ** 15,
                                 'EB': 10 ** 18,
                                 'ZB': 10 ** 21,
                                 'YB': 10 ** 24,
                                 'RB': 10 ** 27,
                                 'QB': 10 ** 30,
                                 '-2': '',
                                 'KiB': 1024,
                                 'MiB': 1024 * 1024,
                                 'GiB': 1024 ** 3,
                                 'TiB': 1024 ** 4,
                                 'PiB': 1024 ** 5,
                                 'EiB': 1024 ** 6,
                                 'ZiB': 1024 ** 7,
                                 'YiB': 1024 ** 8,
                                 'RiB': 1024 ** 9,
                                 'QiB': 1024 ** 10}
        self.setup_conversion_menu('Digital Storage')


class Testing:
    '''Testing functions'''

    def __init__(self, my_frame):
        self.my_frame = my_frame
        self.month_number: IntVar = IntVar()
        self.month_name_1: StringVar = StringVar()
        self.month_name_2: StringVar = StringVar()
        button_row: int = 0

        Spinbox(self.my_frame,
                textvariable=self.month_number,
                from_=1,
                to=12,
                wrap=True,
                width=1,
                foreground='blue',
                background='azure',
                font=('Roboto Mono Medium', '10')).grid(row=button_row, column=0, columnspan=2, sticky='news')
        Spinbox(self.my_frame,
                values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'),
                textvariable=self.month_name_2,
                wrap=True,
                width=1,
                foreground='blue',
                background='azure',
                font=('Roboto Mono Medium', '10')).grid(row=button_row, column=2, columnspan=2, sticky='news')
        Spinbox(self.my_frame,
                values=('Dec', 'Nov', 'Oct', 'Sep', 'Aug', 'Jul', 'Jun', 'May', 'Apr', 'Mar', 'Feb', 'Jan'),
                textvariable=self.month_name_1,
                wrap=True,
                width=1,
                foreground='blue',
                background='azure',
                font=('Roboto Mono Medium', '10')).grid(row=button_row, column=4, columnspan=2, sticky='news')
        self.month_number.set(3)
        self.month_name_1.set('Jan')
        self.month_name_2.set('Jan')
        button_row += 1
        CTkButton(master=self.my_frame,
                  text='111111',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -1)).grid(row=button_row, column=0)
        CTkButton(master=self.my_frame,
                  text='222222',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -2)).grid(row=button_row, column=1)
        CTkButton(master=self.my_frame,
                  text='333333',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -3)).grid(row=button_row, column=2)
        CTkButton(master=self.my_frame,
                  text='444444',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -4)).grid(row=button_row, column=3)
        CTkButton(master=self.my_frame,
                  text='555555',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -5)).grid(row=button_row, column=4)
        CTkButton(master=self.my_frame,
                  text='666666',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -6)).grid(row=button_row, column=5)
        button_row += 1
        CTkButton(master=self.my_frame,
                  text='777777',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -7)).grid(row=button_row, column=0)
        CTkButton(master=self.my_frame,
                  text='888888',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -8)).grid(row=button_row, column=1)
        CTkButton(master=self.my_frame,
                  text='999999',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -9)).grid(row=button_row, column=2)
        CTkButton(master=self.my_frame,
                  text='101010',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -10)).grid(row=button_row, column=3)
        CTkButton(master=self.my_frame,
                  text='111111',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -11)).grid(row=button_row, column=4)
        CTkButton(master=self.my_frame,
                  text='121212',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -12)).grid(row=button_row, column=5)
        button_row += 1
        CTkButton(master=self.my_frame,
                  text='131313',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -13)).grid(row=button_row, column=0)
        CTkButton(master=self.my_frame,
                  text='141414',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -14)).grid(row=button_row, column=1)
        CTkButton(master=self.my_frame,
                  text='151515',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -15)).grid(row=button_row, column=2)
        CTkButton(master=self.my_frame,
                  text='161616',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -16)).grid(row=button_row, column=3)
        CTkButton(master=self.my_frame,
                  text='171717',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -17)).grid(row=button_row, column=4)
        CTkButton(master=self.my_frame,
                  text='181818',
                  width=BUTTON_WIDTH,
                  height=BUTTON_HEIGHT,
                  font=('Roboto Mono Medium', -18)).grid(row=button_row, column=5)
        button_row += 1
        self.round_button = CTkButton(master=self.my_frame,
                                      width=45,
                                      height=45,
                                      corner_radius=21,
                                      border_width=0,
                                      border_spacing=0,
                                      text='',
                                      font=('Roboto Mono Medium', -8),
                                      command=lambda: self.round_button_callback())
        self.round_button.grid(row=button_row, column=0, rowspan=2, columnspan=2)
        button_row += 2
        self.my_frame.grid()

    def round_button_callback(self) -> None:
        print('height=', self.round_button.cget('height'))
        print('width =', self.round_button.cget('width'))
        print('corner_radius =', self.round_button.cget('corner_radius'))
        print('geometry=', self.round_button.winfo_geometry())


class NewSlider:
    '''Slider for both # decimals and base'''

    def __init__(self, s_from: int, s_to: int, s_default: int, s_title: str):
        self.s_from = s_from
        self.s_to = s_to
        self.s_default = s_default
        self.s_title = s_title
        my_font = CTkFont(family='Tw Cen MT', size=15, weight='normal')
        self.slider_digits_value: IntVar = IntVar()
        self.slider_digits_value.set(self.s_default)
        self.slider_digits_window = CTkToplevel()
        self.slider_digits_window.title(self.s_title)
        self.slider_digits_window.protocol('WM_DELETE_WINDOW', self.slider_digits_window.withdraw)
        slider_digits_frame = CTkFrame(master=self.slider_digits_window)
        self.slider_digits_label = CTkLabel(slider_digits_frame,
                                            fg_color='pink',
                                            text_color='blue',
                                            text=str(self.s_default))
        self.slider_digits = CTkSlider(master=slider_digits_frame,
                                       from_=self.s_from,
                                       to=self.s_to,
                                       number_of_steps=(self.s_to - self.s_from),
                                       width=120,
                                       orientation='horizontal',
                                       fg_color='blue',
                                       progress_color='LightBlue1',
                                       command=self.slider_digits_changed,
                                       variable=self.slider_digits_value)
        slider_digits_lo = CTkLabel(slider_digits_frame, text=str(self.s_from))
        slider_digits_hi = CTkLabel(slider_digits_frame, text=str(self.s_to))

        self.slider_digits_window.bind('<FocusOut>',
                                       lambda event: self.slider_digits_window.withdraw())
        self.slider_digits_window.bind('<Left>',
                                       lambda event: self.digits_key('left'))
        self.slider_digits_window.bind('<Right>',
                                       lambda event: self.digits_key('right'))
        self.slider_digits_window.bind('<Home>',
                                       lambda event: self.digits_key('home'))
        self.slider_digits_window.bind('<End>',
                                       lambda event: self.digits_key('end'))
        self.slider_digits_window.bind('d',
                                       lambda event: self.digits_key('default'))
        self.slider_digits_window.bind('D',
                                       lambda event: self.digits_key('default'))
        self.slider_digits_window.bind('<Return>',
                                       lambda event: self.slider_digits_window.withdraw())
        self.slider_digits_window.bind('<Escape>',
                                       lambda event: self.slider_digits_window.withdraw())
        digits_separator = CTkFrame(master=slider_digits_frame,
                                    width=250, height=3,
                                    border_width=1, border_color='green',
                                    fg_color='green')
        help_text = CTkTextbox(slider_digits_frame, width=250, height=150, font=my_font)
        msg = ('Left: decrease by 1.\n'
               'Right: increase by 1.\n'
               'Home: set to the minimum of ' + str(self.s_from) + '.\n'
               'End: set to the maximum of ' + str(self.s_to) + '.\n'
               'D/d: set to the to default of ' + str(self.s_default) + '.\n'
               'Return or Esc: exit the slider window.')
        help_text.insert('0.0', msg)
        help_text.configure(state='disabled')
        self.slider_digits_window.withdraw()
        slider_digits_frame.pack()
        slider_digits_lo.grid(row=0, column=0)
        self.slider_digits.grid(row=0, column=1, sticky='news')
        slider_digits_hi.grid(row=0, column=2)
        self.slider_digits_label.grid(row=1, column=0, columnspan=3)
        self.slider_digits.set(self.s_default)
        digits_separator.grid(row=3, column=0, columnspan=3)
        help_text.grid(row=4, column=0, columnspan=3)

    def show_slider(self) -> None:
        match self.s_title:
            case 'Digits':
                self.slider_digits_value.set(app.scientific.settings_dict['significant_digits'])
                t = '# Decimals = ' + str(app.scientific.settings_dict['significant_digits'])
                self.slider_digits_label.configure(text=t)
            case 'Base':
                self.slider_digits_value.set(app.scientific.settings_dict['display_base'])
                t = 'Base = ' + str(app.scientific.settings_dict['display_base'])
                self.slider_digits_label.configure(text=t)
                app.scientific.set_format(app.scientific.DisplayFormat.FORMAT_BASE)
            case _:
                popup_message.show(title='show_slider',
                              message='self.s_title '+ self.s_title + ' should not happen.')
        app.scientific.update_status_box()
        self.slider_digits_window.deiconify()

    def slider_digits_changed(self, new_slider_value: float) -> None:
        match self.s_title:
            case 'Digits':
                app.scientific.settings_dict['significant_digits'] = int(new_slider_value)
                t = '# Decimals = ' + str(app.scientific.settings_dict['significant_digits'])
                self.slider_digits_label.configure(text=t)
            case 'Base':
                app.scientific.settings_dict['display_base'] = int(new_slider_value)
                t = 'Base = ' + str(app.scientific.settings_dict['display_base'])
                self.slider_digits_label.configure(text=t)
        app.scientific.update_status_box()
        app.scientific.display_stack()

    def digits_key(self, key_name: str) -> None:
        match self.s_title:
            case 'Digits':
                num_digits = app.scientific.settings_dict['significant_digits']
            case 'Base':
                num_digits = app.scientific.settings_dict['display_base']
        match key_name:
            case 'home':
                num_digits = self.s_from
            case 'end':
                num_digits = self.s_to
            case 'left':
                num_digits -= 1
            case 'right':
                num_digits += 1
            case 'default':
                num_digits = self.s_default
        num_digits = max(num_digits, self.s_from)
        num_digits = min(num_digits, self.s_to)
        self.slider_digits_value.set(num_digits)
        match self.s_title:
            case 'Digits':
                app.scientific.settings_dict['significant_digits'] = num_digits
                t = '# Decimals = ' + str(app.scientific.settings_dict['significant_digits'])
                self.slider_digits_label.configure(text=t)
            case 'Base':
                app.scientific.settings_dict['display_base'] = num_digits
                t = 'Base = ' + str(app.scientific.settings_dict['display_base'])
                self.slider_digits_label.configure(text=t)
        app.scientific.update_status_box()
        app.scientific.display_stack()

    #  def check_myentry(self) -> None:
    #      if len(app.scientific.my_entry.get()) != 0:
    #          self.hide_tip()
    #      else:
    #          self.tipwindow.after(250, lambda: self.check_myentry())
    # 
    #  def hide_tip(self) -> None:
    #      self.mouse_still_in = False
    #      tw = self.tipwindow
    #      self.tipwindow = None
    #      if tw:
    #          tw.destroy()

    #  def update_timeout(self, timeout: int) -> None:  #  Timeout is in seconds
    #      self.display_timeout = timeout * 1000


class App(CTk):
    '''Main'''

    def __init__(self):
        super().__init__()
        self.scientific: CTkFrame = None
        self.finance: CTkFrame = None
        self.statistics: CTkFrame = None
        self.converter: CTkFrame = None
        self.testing: CTkFrame = None
        self.digits_slider: NewSlider = None
        self.base_slider: NewSlider = None
        self.my_tabview: CTkTabview = ''
        self.widget_dict: dict = {}
        self.format_menu: int = 0
        self.app_title: str = f'KevCalc v{str(CALC_VERSION)}.{str(CALC_SUBVERSION)}: python {version_info[0]}.{version_info[1]}'
        self.config(cursor='arrow')
        self.title(self.app_title)
        self.protocol('WM_DELETE_WINDOW', lambda: self.exit_this())
        self.clipboard_clear()
        self.transparent: bool = False
        self.bind('<Control-q>', lambda event: self.control_pressed('q'))  #  Exit
        self.bind('<Control-Q>', lambda event: self.control_pressed('q'))  #  Exit
        self.bind('<Control-y>', lambda event: self.control_pressed('q'))  #  Exit
        self.bind('<Control-Y>', lambda event: self.control_pressed('q'))  #  Exit
        self.bind('<Control-b>', lambda event: self.control_pressed('b'))  #  Binary format
        self.bind('<Control-B>', lambda event: self.control_pressed('b'))  #  Binary format
        self.bind('<Control-c>', lambda event: self.control_pressed('c'))  #  Cycle screen layout
        self.bind('<Control-C>', lambda event: self.control_pressed('c'))  #  Cycle screen layout
        self.bind('<Control-d>', lambda event: self.control_pressed('d'))  #  DMS format
        self.bind('<Control-D>', lambda event: self.control_pressed('d'))  #  DMS format
        self.bind('<Control-e>', lambda event: self.control_pressed('e'))  #  Eng format
        self.bind('<Control-E>', lambda event: self.control_pressed('e'))  #  Eng format
        self.bind('<Control-f>', lambda event: self.control_pressed('f'))  #  Fraction format
        self.bind('<Control-F>', lambda event: self.control_pressed('f'))  #  Fraction format
        self.bind('<Control-h>', lambda event: self.control_pressed('h'))  #  Hexadecimal format
        self.bind('<Control-H>', lambda event: self.control_pressed('h'))  #  Hexadecimal format
        self.bind('<Control-k>', lambda event: self.control_pressed('k'))  #  Controlkeys help
        self.bind('<Control-K>', lambda event: self.control_pressed('k'))  #  Controlkeys help
        self.bind('<Control-o>', lambda event: self.control_pressed('o'))  #  Octal format
        self.bind('<Control-O>', lambda event: self.control_pressed('o'))  #  Octal format
        self.bind('<Control-r>', lambda event: self.control_pressed('r'))  #  Roman format
        self.bind('<Control-R>', lambda event: self.control_pressed('r'))  #  Roman format
        self.bind('<Control-s>', lambda event: self.control_pressed('s'))  #  Scientific format
        self.bind('<Control-S>', lambda event: self.control_pressed('s'))  #  Scientific format
        self.bind('<Control-t>', lambda event: self.control_pressed('t'))  #  Transparent
        self.bind('<Control-T>', lambda event: self.control_pressed('t'))  #  Transparent
        self.bind('<Control-u>', lambda event: self.control_pressed('u'))  #  Suffix format
        self.bind('<Control-U>', lambda event: self.control_pressed('u'))  #  Suffix format
        self.bind('<Control-w>', lambda event: self.control_pressed('w'))  #  Word format
        self.bind('<Control-W>', lambda event: self.control_pressed('w'))  #  Word format
        self.bind('<Control-x>', lambda event: self.control_pressed('x'))  #  Sexagesimal format
        self.bind('<Control-X>', lambda event: self.control_pressed('x'))  #  Sexagesimal format
        self.bind('<Control-z>', lambda event: self.control_pressed('z'))  #  Undo
        self.bind('<Control-Z>', lambda event: self.control_pressed('z'))  #  Undo
        self.bind('<Control-Home>', lambda event: self.control_pressed('0'))  #  Bring window back on-screen)
        self.bind('<Control-Key-1>', lambda event: self.control_pressed('1'))  #  Tab 0
        self.bind('<Control-Key-2>', lambda event: self.control_pressed('2'))  #  Tab 1
        self.bind('<Control-Key-3>', lambda event: self.control_pressed('3'))  #  Tab 2
        self.bind('<Control-Key-4>', lambda event: self.control_pressed('4'))  #  Tab 3
        self.bind('<Control-Key-5>', lambda event: self.control_pressed('5'))  #  Tab 4
        self.bind('<Control-Key-6>', lambda event: self.control_pressed('6'))  #  Tab 5
        self.bind('<F1>', lambda event: app.helping.show_help('General'))
        seed()
        self.iconbitmap(r'calculator' + str(randint(0, 3)) + r'.ico')
        self.helping: Helping = Helping()

    def set_transparent(self):
        if self.transparent:
            app.attributes('-alpha', 1.0)
            self.transparent = False
            app.after_cancel(self.t)
        else:
            app.attributes('-alpha', 0.1)
            self.transparent = True
            self.t = app.after(10000, lambda: self.set_transparent())

    def control_pressed(self, which_one) -> None:
        '''User has pressed Ctrl ?'''
        match which_one:
            case 'b':
                self.scientific.set_base(2)
            case 'c':
                self.scientific.cycle_orientation()
            case 'd':
                self.scientific.set_format(app.scientific.DisplayFormat.FORMAT_DMS)
            case 'e':
                self.scientific.set_format(app.scientific.DisplayFormat.FORMAT_ENG)
            case 'f':
                self.scientific.fraction_format()
            case 'h':
                self.scientific.set_base(16)
            case 'k':
                self.helping.controlkeys_help()
            case 'l':
                self.scientific.cycle_orientation()
            case 'o':
                self.scientific.set_base(8)
            case 'q':
                self.exit_this(False)
            case 'r':
                self.scientific.set_format(app.scientific.DisplayFormat.FORMAT_ROMAN)
            case 's':
                self.scientific.set_format(app.scientific.DisplayFormat.FORMAT_SCI)
            case 't':
                self.set_transparent()
            case 'u':
                self.scientific.set_format(app.scientific.DisplayFormat.FORMAT_SUFFIX)
            case 'w':
                self.scientific.set_format(app.scientific.DisplayFormat.FORMAT_WORD)
            case 'x':
                self.scientific.set_format(app.scientific.DisplayFormat.FORMAT_SEXAGESIMAL)
            case 'z':
                self.scientific.restore_stack()
            case '/':
                print('/')
                pass
            case '0':
                app.geometry('+100+100')
            case '1':
                self.scientific.my_entry.focus_set()
                self.my_tabview.set('Scientific')
            case '2':
                self.finance.e_principal.focus_set()
                self.my_tabview.set('Finance')
            case '3':
                self.statistics.data_entry.focus_set()
                self.my_tabview.set('Statistics')
            case '4':
                self.converter.input_field.focus_set()
                self.my_tabview.set('Converter')
            case '5':
                self.my_tabview.set('Test')

    def ctrl_left_click(self, event, textstr: str = ''):
        if textstr != '':
            app.helping.show_help(textstr)
            return 'break'
        widget = event.widget
        if widget.winfo_class() == 'Label':
            app.helping.show_help(widget.cget('text'))
            return 'break'
        grid_info = widget.grid_info()
        for key in grid_info:
            if key == 'in':  #  This widget is contained within another widget.
                widget = grid_info[key]
                child_info = widget.winfo_children()
                for child in child_info:
                    if child.winfo_class() == 'Label':
                        app.helping.show_help(child.cget('text'))
                        return 'break'
        app.helping.show_help('app')

    def create_objects(self) -> None:
        self.my_tabview: CTkTabview = CTkTabview(master=self,
                                                 fg_color='mint cream',
                                                 text_color='blue',
                                                 segmented_button_fg_color='light blue',
                                                 segmented_button_selected_color='lightyellow',
                                                 segmented_button_unselected_hover_color='limegreen',
                                                 segmented_button_selected_hover_color='orange',
                                                 segmented_button_unselected_color='violet')
        self.my_tabview.configure(command=self.process_tab_select)
        self.my_tabview._segmented_button.configure(font=CTkFont(family='Code New Roman', size=16))
        self.my_tabview.pack(expand=1, fill='both')

        self.scientific: Scientific = Scientific(CTkFrame(master=self.my_tabview.insert(0, 'Scientific'),
                                              fg_color='lightyellow'))
        self.finance: Finance = Finance(CTkFrame(master=self.my_tabview.insert(1, 'Finance'),
                                        fg_color='mint cream'))
        self.statistics: Statistics = Statistics(CTkFrame(master=self.my_tabview.insert(2, 'Statistics'),
                                              fg_color='mint cream'))
        self.converter: Converter = Converter(CTkFrame(master=self.my_tabview.insert(3, 'Converter'),
                                            fg_color='mint cream'))
        self.testing: Testing = Testing(CTkFrame(master=self.my_tabview.insert(4, 'Test'),
                                        fg_color='mint cream'))
        self.digits_slider: NewSlider = NewSlider(1, 15, 8, 'Digits')
        self.base_slider: NewSlider = NewSlider(2, 62, 10, 'Base')

        self.show_time()
        self.my_tabview.set('Scientific')
        app.scientific.update_status_box()

    def clip_board(self, what: str) -> None:
        '''
        Manages the Clipboard.
        Parameters:
            what
                from=Copy from self.my_entry to Clipboard.
                to=Paste from Clipboard to self.my_entry.
        '''

        def inner():
            match what:
                case 'from':
                    self.clipboard_clear()
                    self.clipboard_append(app.scientific.my_entry.get())
                case 'to':
                    try:
                        s = self.clipboard_get()
                        app.scientific.my_entry.insert('end', s)
                    except:  #  Don't actually care if the clipboard is empty
                        pass

        return inner

    def create_cascade_menu(self, menulabel: str, parent: Menu, underline: int = 0) -> Menu:
        child = Menu(parent, tearoff=0, font=MENU_FONT)
        parent.add_cascade(label=menulabel,
                           underline=underline,
                           menu=child,
                           font=MENU_FONT)
        return child

    def add_menu_const(self, this_menu: Menu, description: str, value: float, units: dict = {}) -> None:
        '''
        Add a menu item called description with value to menu
        '''
        this_menu.add_command(label=description,
                              underline=0,
                              command=lambda: self.scientific.insert_constant(value, description, units),
                              font=MENU_FONT)


    def setup_menu_items(self) -> None:
        '''
        Setup all the menus we need.
        '''
        self.my_menu = Menu(self, font=('Courier', 20))# MENU_FONT)
        # self.my_menu = CTkTitleMenu(self)
        self.config(menu=self.my_menu)

        filemenu = self.create_cascade_menu('File', self.my_menu)
        filemenu.add_command(label='Cycle Orientation',
                             underline=0,
                             command=self.scientific.cycle_orientation,
                             font=MENU_FONT)

        filemenu.add_separator()
        filemenu.add_command(accelerator='Ctrl+Q',
                             label='Exit',
                             underline=1,
                             command=lambda: self.exit_this(),
                             font=MENU_FONT)

        cnstmenu = self.create_cascade_menu('Constants', self.my_menu, 1)
        othemenu = self.create_cascade_menu('Others', cnstmenu)
        self.add_menu_const(othemenu, 'Bohr Radius', 5.29177210544e-11, {'m': 1})
        self.add_menu_const(othemenu, 'Celsius Absolute Zero', -273.15, {'\u00b0C': 1})
        self.add_menu_const(othemenu, 'Conductance Quantum', 7.7480917346e-5, {'S': 1})
        self.add_menu_const(othemenu, 'Euler-Mascheroni Constant', 0.577215664901533, {'\u03b3': 1})
        self.add_menu_const(othemenu, 'Magnetic Flux Quantum', 2.067833636e-15, {'w': 1})
        self.add_menu_const(othemenu, 'Rydberg Constant', 10973731.568157, {'m': -1})
        self.add_menu_const(othemenu, 'Rydberg Frequency', 3.28984196025e15, {'Hz': 1})
        self.add_menu_const(othemenu, 'Rydberg Wavelength', 9.112670505826e-8, {'m': 1})
        self.add_menu_const(othemenu, 'Speed of Sound', 331.622, {'m': 1, 's': -1})
        self.add_menu_const(othemenu, 'Stefan-Boltzmann Constant', 5.670374419e-8, {'w': 1, 'm': -2, '\u00b0K': -4})

        univmenu = self.create_cascade_menu('Universal', cnstmenu)
        self.add_menu_const(univmenu, 'Avogadro Constant', 6.0221419e23, {'mol': -1})
        self.add_menu_const(univmenu, 'Boltzmann Constant', 1.3806503e-23, {'J': 1, 'K': -1})
        self.add_menu_const(univmenu, 'Electron Volt', 1.602176634e-19, {'J': 1})
        self.add_menu_const(univmenu, 'Faraday', 96485.33212, {'C': 1, 'mol': -1})
        self.add_menu_const(univmenu, 'Molar Gas', 8.31446261815324, {'J': 1, 'K': -1, 'mol': -1})
        self.add_menu_const(univmenu, 'Molar Vol Ideal Gas', 0.022413996, {'m': 3, 'mol': -1})
        self.add_menu_const(univmenu, 'Neutron Mass', 1.67492749804e-27, {'kg': 1})
        self.add_menu_const(univmenu, 'Gravitational constant', 6.6743e-11, {'m': 3, 'kg': -1, 's': -2})
        self.add_menu_const(univmenu, 'Permeability of Vacuum', 1.25663706127e-6, {'N': 1, 'A': -2})
        self.add_menu_const(univmenu, 'Permittivity of Vacuum', 8.8541878188e-12, {'F': 1, 'm': -1})

        astrmenu = self.create_cascade_menu('Astronomical', cnstmenu)
        self.add_menu_const(astrmenu, 'Astronomical Unit', 1.495978707e11, {'m': 1})
        self.add_menu_const(astrmenu, 'Earth g', 9.80665, {'m': 1, 's': -2})
        self.add_menu_const(astrmenu, 'Earth Mass', 5.97370e24, {'kg': 1})
        self.add_menu_const(astrmenu, 'Earth Radius', 6.378140e6, {'m': 1})
        self.add_menu_const(astrmenu, 'Light Year', 9460730472580800, {'m': 1})
        self.add_menu_const(astrmenu, 'Moon g', 1.619, {'m': 1, 's': -2})
        self.add_menu_const(astrmenu, 'Parsec', 3.0856775807e16, {'m': 1})
        self.add_menu_const(astrmenu, 'Sidereal Year 1994', 31558149.8, {'s': 1})
        self.add_menu_const(astrmenu, 'Sun Mass', 1.98892e30, {'kg': 1})
        self.add_menu_const(astrmenu, 'Sun Radius', 6.957e8, {'m': 1})
        self.add_menu_const(astrmenu, 'Sun Schwarzschild Radius', 2.953250e3, {'m': 1})
        self.add_menu_const(astrmenu, 'Tropical Year 1994', 31556925.445, {'s': 1})

        physmenu = self.create_cascade_menu('Physics', cnstmenu)
        self.add_menu_const(physmenu, 'Atomic Mass Unit', 1.66053904020e-27, {'kg': 1})
        self.add_menu_const(physmenu, 'Electron Mass', 9.1093837139e-31, {'kg': 1})
        self.add_menu_const(physmenu, 'Elementary Charge', 1.602176634e-19, {'C': 1})
        self.add_menu_const(physmenu, 'Fine Structure Constant [\u03b1]', 0.0072973525643, {})
        self.add_menu_const(physmenu, 'Planck Constant [\u210e]', 6.62607015e-34, {'J': 1, 's': 1})
        self.add_menu_const(physmenu, 'Planck Length', 1.606255e-35, {'m': 1})
        self.add_menu_const(physmenu, 'Planck Mass', 2.176434e-9, {'kg': 1})
        self.add_menu_const(physmenu, 'Planck Temperature', 1.416784e32, {'\u00b0K': 1})
        self.add_menu_const(physmenu, 'Planck Time', 5.391247e-44, {'s': 1})
        self.add_menu_const(physmenu, 'Proton Mass', 1.67262158e-27, {'kg': 1})
        self.add_menu_const(physmenu, 'Speed of Light in Vacuum', 2.99792458e8, {'m': 1, 's': -1})

        mathmenu = self.create_cascade_menu('Mathematics', cnstmenu)
        self.add_menu_const(mathmenu, 'e', e, {})
        self.add_menu_const(mathmenu, '\u03c0', pi, {})
        self.add_menu_const(mathmenu, 'Tau (2\u03c0)', tau, {})

        self.format_menu = self.create_cascade_menu('Format', self.my_menu, 2)
        self.format_menu.add_command(label='Scientific',
                                     command=lambda: app.scientific.set_format(app.scientific.DisplayFormat.FORMAT_SCI),
                                     font=MENU_FONT)
        self.format_menu.add_command(label='Engineering',
                                     command=lambda: app.scientific.set_format(app.scientific.DisplayFormat.FORMAT_ENG),
                                     font=MENU_FONT)
        self.format_menu.add_command(label="Suffix",
                                     command=lambda: app.scientific.set_format(
                                         app.scientific.DisplayFormat.FORMAT_SUFFIX),
                                     font=MENU_FONT)
        self.format_menu.add_command(label='Hexadecimal',
                                     command=lambda: app.scientific.set_base(16),
                                     font=MENU_FONT)
        self.format_menu.add_command(label="Octal",
                                     command=lambda: app.scientific.set_base(8),
                                     font=MENU_FONT)
        self.format_menu.add_command(label="Binary",
                                     command=lambda: app.scientific.set_base(2),
                                     font=MENU_FONT)
        self.format_menu.add_command(label='Base',
                                     command=lambda: self.base_slider.show_slider(),
                                     font=MENU_FONT)
        self.format_menu.add_command(label='Fraction',
                                     command=lambda: app.scientific.set_format(
                                         app.scientific.DisplayFormat.FORMAT_FRACTION),
                                     font=MENU_FONT)
        self.format_menu.add_command(label='# Decimals',
                                     command=lambda: self.digits_slider.show_slider(),
                                     font=MENU_FONT)
        self.format_menu.add_command(label='Words',
                                     command=lambda: app.scientific.set_format(
                                         app.scientific.DisplayFormat.FORMAT_WORD),
                                     font=MENU_FONT)
        self.format_menu.add_command(label='Sexagesimal',
                                     command=lambda: app.scientific.set_format(
                                         app.scientific.DisplayFormat.FORMAT_SEXAGESIMAL),
                                     font=MENU_FONT)
        self.format_menu.add_command(label="Roman",
                                     command=lambda: app.scientific.set_format(
                                         app.scientific.DisplayFormat.FORMAT_ROMAN),
                                     font=MENU_FONT)
        self.format_menu.add_command(label='\u00b0 \' "',
                                     command=lambda: app.scientific.set_format(app.scientific.DisplayFormat.FORMAT_DMS),
                                     font=MENU_FONT)

        self.editmenu = self.create_cascade_menu('Edit', self.my_menu)
        self.editmenu.add_command(label='Undo',
                                  command=lambda: app.scientific.restore_stack,
                                  font=MENU_FONT)
        self.editmenu.add_command(label='Copy from Entrybox',
                                  command=lambda: self.clip_board('from'),
                                  font=MENU_FONT)
        self.editmenu.add_command(label='Paste to Entrybox',
                                  command=lambda: self.clip_board('to'),
                                  font=MENU_FONT)

        self.hlpmenu = self.create_cascade_menu('Help', self.my_menu)
        self.hlpmenu.add_command(label='Help - F1',
                                 underline=0,
                                 command=lambda: app.helping.show_help('General'),
                                 font=MENU_FONT)
        self.hlpmenu.add_command(label='Formul\u00e6',
                                 underline=0,
                                 command=lambda: app.helping.clicked_help('formulae'),
                                 font=MENU_FONT)
        self.hlpmenu.add_command(label='Control Keys',
                                 underline=0,
                                 command=lambda: app.helping.clicked_help('controlkeys'),
                                 font=MENU_FONT)
        self.hlpmenu.add_command(label='SI Suffixes',
                                 underline=0,
                                 command=lambda: app.helping.clicked_help('suffix'),
                                 font=MENU_FONT)
        self.hlpmenu.add_command(label='SI',
                                 underline=1,
                                 command=lambda: app.helping.clicked_help('SI'),
                                 font=MENU_FONT)
        self.hlpmenu.add_command(label='Some Stuff',
                                 underline=1,
                                 command=app.helping.some_stuff,
                                 font=MENU_FONT)
        self.hlpmenu.add_command(label='File info',
                                 underline=0,
                                 command=app.scientific.file_path_info,
                                 font=MENU_FONT)
        self.hlpmenu.add_command(label="About", underline=0,
                                 command=app.helping.help_about,
                                 font=MENU_FONT)

    def process_tab_select(self) -> None:
        '''Display the selected tab'''
        self.selected_tab = self.my_tabview.get()
        match self.selected_tab:
            case 'Scientific':
                self.scientific.my_entry.focus_set()
            case 'Finance':
                app.finance.e_principal.focus_set()
            case 'Statistics':
                app.statistics.data_entry.focus_set()
            case 'Converter':
                app.converter.input_field.focus_set()

    def show_time(self) -> None:
        '''Updates time every 5 seconds on multiples of 5 seconds.

        Parameters
        ----------

        Returns
        -------

        '''
        self.title(self.app_title + datetime.now().strftime(' %d.%m.%Y %H:%M:%S'))
        delay = datetime.now().second
        delay = 5 - (delay % 5)
        self.self_after = self.after(delay * 1000, self.show_time)


    def exit_this(self, force_exit: bool=True) -> None | Never:
        '''Exit from the app'''
        self.update_registry()
        self.after_cancel(self.self_after)  # stop the time update
        self.config(cursor='arrow')
        try:
            self.digits_slider.slider_digits_window.destroy()
            self.base_slider.slider_digits_window.destroy()
            self.my_message.message_window.destroy()
        except:
            pass
        ''' Why use app.after? Calling exit_this from the Menu was failing to get past the mainloop and end the program.
            exit_this called from an exit button, as a result of the protocol call and via the Esc key all ended OK.
            Changing self.destroy() to app.after(1, lambda: self.destroy()) has resolved the issue.
            No idea why this works.
        '''
        if force_exit is True:
            self.after(1, lambda: self.destroy())
        else:
            popup_message.show(title=None, message='Do you want to exit?', x_pos=0.6, y_pos=0.1, yesno = True)
            if popup_message.get() == 'y':
                app.after(1, lambda: self.destroy())


    def update_registry(self) -> None:
        '''Update registry entries with stack, redo, variables etc.'''
        try:
            my_key = OpenKey(HKEY_CURRENT_USER, r'Software\KevCalc\Scientific', 0, KEY_WRITE)
        except:
            CreateKeyEx(HKEY_CURRENT_USER, r'Software\KevCalc\Scientific')
            my_key = OpenKey(HKEY_CURRENT_USER, r'Software\KevCalc\Scientific', 0, KEY_WRITE)
        pickled_out = pickle.dumps(app.scientific.stack_values)
        SetValueEx(my_key, 'stack_values', 0, REG_BINARY, pickled_out)

        pickled_out = pickle.dumps(app.scientific.redo_stack)
        SetValueEx(my_key, 'redo_stack', 0, REG_BINARY, pickled_out)

        geo = app.winfo_geometry().replace('+', 'x').split('x')
        left = int(geo[2])
        top = int(geo[3])
        app.scientific.settings_dict['left'] = left
        app.scientific.settings_dict['top'] = top
        pickled_out = pickle.dumps(app.scientific.settings_dict)
        SetValueEx(my_key, 'settings_dict', 0, REG_BINARY, pickled_out)

        key_val = app.scientific.my_entry.get()
        SetValueEx(my_key, 'entry_box', 0, REG_SZ, key_val)

        pickled_out = pickle.dumps(app.scientific.equations)
        SetValueEx(my_key, 'equations', 0, REG_BINARY, pickled_out)

        pickled_out = pickle.dumps(app.scientific.created_vars)
        SetValueEx(my_key, 'created_vars', 0, REG_BINARY, pickled_out)

        CloseKey(my_key)


class FirstBit:
    ''' Check the platform, version and if we are .exe or .py'''

    def __init__(self):
        if platform.startswith('win') is False:
            exit('This app is only supported on Windows.')
        if version_info < (PYTHON_MAJOR_VERSION, PYTHON_MINOR_VERSION):
            exit('You MUST be using Python v' + str(PYTHON_MAJOR_VERSION) +
                 '.' + str(PYTHON_MINOR_VERSION) + ' or greater.')

        try:
            if hasattr(sys, 'frozen') and hasattr(sys, '_MEIPASS'):
                self.what_i_am = 'bundled app'
                self.my_file_path = sys._MEIPASS.rsplit('\\', 1)[0]
        except:
            self.my_file_path, self.my_file_name = path.split(argv[0].replace('\\\\', '\\'))
            self.what_i_am = 'Python script'
        '''
        When running the Calculator, keyboard focus stays with IDLE even though the Calculator window
        has focus. So, until the Mouse is clicked in the Calculator window, keyboard strokes go to
        IDLE. This bit presses and releases the Shift key, which forces focus to the Calculator.
        '''
        Shiftkey = 0x10  #  VirtualKey Code for Shift
        win32api.keybd_event(Shiftkey, 0, 0, 0)  #  press the key
        sleep(0.1)
        win32api.keybd_event(Shiftkey, 0, 0x2, 0)  #  release the key

    def check_state(self):
        if app.state() == 'withdrawn':
            # print('withdrawn, deiconifying')
            app.deiconify()

if __name__ == '__main__':
    app: App = App()
    popup_message = PopupMessage(app)
    text_widget_link = TextWidgetLink()
    text_widget_highlight = TextWidgetHighlight()
    first_bit: FirstBit = FirstBit()
    app.create_objects()
    app.setup_menu_items()
    app.bind('<Escape>', lambda e: app.exit_this(False))
    app.bind('<Control-Z>', lambda e: app.scientific.restore_stack())
    app.after(100, lambda: app.scientific.my_entry.focus_force())
    #  Sometimes after pressing Shift-F10, the app window fails to appear.
    #  This to try and fix it.
    app.after(250, lambda: first_bit.check_state())
    app.mainloop()
