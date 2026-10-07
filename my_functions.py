""" These are functions written by Kev
"""
# from win32 import win32api
def retrieve_object(object: any, where_h: float=0.5, where_v=0.5):
    ''' Retrieve an object that is off screen by at least 50% in any direction. Object is moved to where_h & where_v distance
        across/down the screen.
        If either of where_h or where_v are > 1, they are treated as screen location in pixels.
        This does not check for visible taskbar etc, so the window may have the bottom hidden behind the taskbar.
    '''
    # primary_monitor = win32api.MonitorFromPoint((0,0))
    # monitor_info = win32api.GetMonitorInfo(primary_monitor)
    # monitor_area = monitor_info.get("Monitor")
    # work_area = monitor_info.get("Work")
    # taskbar_height = monitor_area[3] - work_area[3]
    # title_height = object.winfo_rooty() - object.winfo_y()
    sw = object.winfo_screenwidth()
    sh = object.winfo_screenheight() # - taskbar_height - title_height
    geo = object.geometry().replace('x', '+').split('+')
    w = int(geo[0])
    h = int(geo[1])
    l = int(geo[2])
    t = int(geo[3])
    off_screen: bool = False
    if l + w / 2 < 0: # Horizontal object centre off left
        off_screen = True
    if l + w / 2 > sw: # Horizontal object centre off right
        off_screen = True
    if t + h / 2 < 0: # Vertical object centre off top
        off_screen = True
    if t + h / 2 > sh: # Vertical object centre off bottom
        off_screen = True
    if off_screen:
        if w > sw or h > sh: # window larger than screen, put it roughly top left.
            l_pos = 100
            t_pos = 100
        else:
            l_pos = int(where_h) if where_h > 1.0 else int(sw*where_h)
            r_pos = l_pos + w
            t_pos = int(where_v) if where_v > 1.0 else int(sh*where_v)
            b_pos = t_pos + h
            if l_pos < 0:
                l_pos = 0
            if r_pos > sw:
                l_pos = sw - w - 10
            if t_pos < 0:
                t_pos = 0
            if b_pos > sh:
                t_pos = sh - h - 10
        s = f'+{l_pos}+{t_pos}'
        object.geometry(s)
    
def get_tag_config(text_widget_in = None, text_widget_out = None):
    text_detail = text_widget_in.get('1.0', 'end')
    print(text_detail)
    text_info = text_widget_in.dump('1.0', 'end', tag=True, text=True)
    print(text_info)
    out = ''
    for ti in text_info:
        tags=[]
        match ti[0]:
            case 'text':
                out = f"{text_widget_in}.insert('end', '{ti[1]}')"
                #print(out)
            case 'tagon':
                tag_start = ti[2]
            case 'tagoff':
                s = f"{text_widget_in}.tag_add('{ti[1]}','{tag_start}','{ti[2]})'"
                print(s)
            case 'mark':
                print(f'Mark {ti[1]} {ti[2]}')
            case 'image':
                print(f'Image {ti[1]} {ti[2]}')
            case 'window':
                print(f'Window {ti[1]} {ti[2]}')
            case _:
                print(f'Invalid {ti[0]}')
    tag_names = text_widget_in.tag_names()
    for tag_name in reversed(tag_names):
        if tag_name != 'sel':
            tag_details = text_widget_in.tag_config(tag_name)
            tag_config = f'tag_config({tag_name}'
            for key, detail in tag_details.items():
                if detail[4] != '':
                    tag_config += f', {detail[0]}={detail[4]}'
            tag_config += ')'
            print(tag_config)

    
def float_to_dms(number: float) -> str:
    negative: str = ''
    dms: float = number
    neg: str = ''
    if dms < 0:
        neg = '-'
        dms = -dms
    degrees: int = int(dms)
    dms = (dms - degrees) * 60
    minutes: int = int(dms)
    dms = (dms - minutes) * 60
    seconds: int = int(round(dms, 2))
    dms = dms - seconds
    fract: str = ''
    if dms > 0:
        fract = '.' + str(int(round(dms * 1000, -1)))
        if fract[-1] == '0':
            fract = fract[:-1]
            if fract[-1] == '0':
                fract = fract[:-1]
        if fract[-1] == '.':
            fract = fract[:-1]
    retval = ''.join([neg, str(degrees), '\u00b0 ', str(minutes), '\' ', str(seconds), '"', fract])
    return retval

def float_to_word(number: float, sig_digits: int=8) -> str:
    '''Converts the float value into words.

    Number cannot be >= 1_000_000_000_000_000_000

    Parameters
        number

    Returns
        The value of number in words.
    '''
    # hundreds = ['', 'one', 'two', 'three', 'four', 'five',
    #             'six', 'seven', 'eight', 'nine']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
            'seventy', 'eighty', 'ninety']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    def word(number: int) -> str:

        retval = ''
        if number == 0:
            return ''
        if number >= 100:
            hundreds_index = number // 100
            retval = units[hundreds_index] + ' hundred'
            number = number - 100 * hundreds_index
        if number != 0:
            if retval != '':
                retval += ' and '
            if number >= 20:
                tens_index = number // 10
                retval += tens[tens_index]
                number = number - 10 * tens_index
                if number > 0:
                    retval += '-'
                    retval += units[number % 10]
            elif number >= 10:
                teens_index = number - 10
                retval += teens[teens_index]
            elif number > 0:
                retval += units[number % 10]
        return retval

    def to_words(number: str) -> str:
        prefix = ''
        ret_str = ''
        for char in number:
            ret_str += prefix + units[int(char)]
            prefix = ' '
        return ret_str

    # self.save_stack()
    if number == 0:
        return 'zero'
    if abs(number) >= 1_000_000_000_000_000_000 or abs(number) < 0.0001:
        s = '{:.' + str(sig_digits) + 'g}'
        # s = '{:.' + str(self.settings_dict['significant_digits']) + 'g}'
        return s.format(number)
    if number < 0:
        minus = 'minus '
        number = -number
    else:
        minus = ''
    if number == 3.141592653589793:
        return minus + 'pi'
    if number == 2.718281828459045:
        return minus + 'e'
    if number == 6.283185307179586:
        return minus + 'tau'
    fraction = 0.0
    full_fraction = 0.0
    if number != int(number):
        full_fraction = number - int(number)
        number = round(number, sig_digits)
        fraction = round(number - int(number), sig_digits)
    strthousands: str = ''
    strmillions: str = ''
    strbillions: str = ''
    strtrillions: str = ''
    strquadrillions: str = ''
    int_number = int(number)
    iones = int_number % 1000
    int_number = int_number // 1000
    strones = word(iones)
    if 0 < iones < 100:
        strones = 'and ' + strones
    if int_number > 0:
        ithousands = int_number % 1000
        int_number = int_number // 1000
        strthousands = word(ithousands)
        if int_number > 0:
            imillions = int_number % 1000
            int_number = int_number // 1000
            strmillions = word(imillions)
            if int_number > 0:
                ibillions = int_number % 1000
                int_number = int_number // 1000
                strbillions = word(ibillions)
                if int_number > 0:
                    itrillions = int_number % 1000
                    int_number = int_number // 1000
                    strtrillions = word(itrillions)
                    if int_number > 0:
                        iquadrillions = int_number % 1000
                        int_number = int_number // 1000
                        strquadrillions = word(iquadrillions)
    output_string = ''
    if strquadrillions != '':
        output_string += strquadrillions + ' quadrillion '
    if strtrillions != '':
        output_string += strtrillions + ' trillion '
    if strbillions != '':
        output_string += strbillions + ' billion '
    if strmillions != '':
        output_string += strmillions + ' million '
    if strthousands != '':
        output_string += strthousands + ' thousand '
    if strones != '':
        output_string += strones
    if output_string.find('and ') == 0:
        output_string = output_string[3:]
    output_string = minus + output_string.strip()
    if fraction != 0.0:
        if output_string == '':
            if fraction == 1 / 4:
                output_string = 'one-quarter'
            elif f'{full_fraction:.15f}' == f'{1 / 3:.15f}':
                output_string = 'one-third'
            elif fraction == 1 / 2:
                output_string = 'one-half'
            elif f'{full_fraction:.15f}' == f'{2 / 3:.15f}':
                output_string = 'two-thirds'
            elif fraction == 3 / 4:
                output_string = 'three-quarters'
            else:
                format_str = '{:.' + str(sig_digits) + 'f}'
                s = format_str.format(fraction)[2:]
                s = s.rstrip('0')
                output_string = 'zero point ' + to_words(s)
        else:
            if fraction == 1 / 4:
                output_string += ' and a quarter'
            elif f'{full_fraction:.15f}' == f'{1 / 3:.15f}':
                output_string += ' and a third'
            elif fraction == 1 / 2:
                output_string += ' and a half'
            elif f'{full_fraction:.15f}' == f'{2 / 3:.15f}':
                output_string += ' and two-thirds'
            elif fraction == 3 / 4:
                output_string += ' and three-quarters'
            else:
                format_str = '{:.' + str(sig_digits) + 'f}'
                s = format_str.format(fraction)[2:]
                s = s.rstrip('0')
                output_string += ' point ' + to_words(s)
    return output_string.replace('  ', ' ')

# from webbrowser import open_new as open_link
# from tkinter import Tk, Toplevel, Label, font
# class ExtendTextbox():
    # """
    # Extends textbox widget to allow for word highlighting and URLs.
    # __init__ sets the initial values for each configurable item. borderwidth and relief apply to highlight_word only.
    # config allows those values to be changed for any future calls, but not for existing links and words.
    # add_link and highlight_word allow the options to be changed for that item only.
    # """
    # def __init__(self,
                 # underline: bool=True,
                 # underlinefg: str='blue',
                 # hover_ul: str='green',
                 # hover_bg: str='orange',
                 # fg_color: str='blue',
                 # bg_color: str='yellow',
                 # popup_fg: str='blue',
                 # popup_bg: str = 'lightyellow',
                 # popup_border: str = 'red',
                 # borderwidth: str='',
                 # relief: str='',
                 # bold: bool = False):
        # self._underline = underline
        # self._underlinefg = underlinefg
        # self._hover_ul = hover_ul
        # self._hover_bg = hover_bg
        # self._fg_color = fg_color
        # self._bg_color = bg_color
        # self._popup_fg = popup_fg
        # self._popup_bg = popup_bg
        # self._popup_border = popup_border
        # self._borderwidth = borderwidth
        # self._relief = relief
        # self._bold = bold
        
    # def show_url_popup(self, text_widget, message, p_fg: str='blue', p_bg: str='lightyellow', p_bd: str='red'):
        # """
        # Shows the URL of the link under the mouse.

        # If the mouse pointer ends up over the popup object, it is treated as an <Exit>, which closes the popup window.
        # As the mouse is still within the text_widget, it then performs another <Enter> and goes into a loop until the mouse is
        # moved off the popup. Adjust both x and y to keep the popup away from the mouse cursor.
        # The popup_border (p_bd) isn't a Label widget item, it is applied to the Toplevel widget with padding, to make it appear
        # as a border colour.
        # """
        # mouse_x = self._text_widget.winfo_pointerx() + 10
        # mouse_y = self._text_widget.winfo_pointery() - 30

        # self.popup = Toplevel(self._text_widget, bg=p_bd, padx=2, pady=2) # padx & pady allow the colour to show around the label.
        # self.popup.overrideredirect(True)  # Remove window decorations
        # self.popup.geometry(f'+{mouse_x}+{mouse_y}') # Position at mouse cursor
        # self.popup.attributes('-topmost', True) # Ensure the popup is above everything else.

        # Label(self.popup, text=message, fg=p_fg, bg=p_bg, relief='flat', borderwidth=0, padx=2, pady=2, font=('',-15)).pack()
        # self.popup.update_idletasks()
        # self._text_widget.update_idletasks()

        
    # def kill_url_popup(self):
        # self.popup.destroy()


    # def add_link(self,
                 # text_widget,
                 # the_text: str,
                 # tag_name: str,
                 # the_link: str,
                 # new_text: str = None,
                 # underline: bool=None,
                 # underlinefg: str=None,
                 # hover_ul: str=None,
                 # hover_bg: str=None,
                 # fg_color: str=None,
                 # bg_color: str=None,
                 # popup_fg: str=None,
                 # popup_bg: str=None,
                 # popup_border: str=None):
        # """
        # Highlight text and create a link in a text widget that supports tags. The parameters here over-ride those
        # set in __init__, but only for this call.
        # To change the colours for future calls, use config.
        # """
        # try:
            # text_widget.tag_add('????',1.0, 'end')
        # except AttributeError:
            # raise Exception(f'item {text_widget} does not support tags.')
        # text_widget.tag_delete('????')
        # str0: str = text_widget.get('1.0', 'end')
        # if len(str0) == 0:
            # return
        # if (text_length := len(the_text)) == 0:
            # return
        # if (find_location := str0.find(the_text)) == -1:
            # return
        # begin_pos = '1.0 linestart+' + str(find_location) + 'c'
        # if new_text is not None and len(new_text) > 0:
            # end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
            # text_widget.configure(state='normal')
            # text_widget.delete(begin_pos, end_pos)
            # text_widget.insert(begin_pos, new_text)
            # text_widget.configure(state='disabled')
            # text_length = len(new_text)
            # str0: str = text_widget.get('1.0', 'end')
        # end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
        # self._text_widget = text_widget
        # fc = self._fg_color if fg_color is None else fg_color
        # bc = self._bg_color if bg_color is None else bg_color
        # uf = self._underlinefg if underlinefg is None else underlinefg
        # hu = self._hover_ul if hover_ul is None else hover_ul
        # hb = self._hover_bg if hover_bg is None else hover_bg
        # ul = self._underline if underline is None else underline
        # uf = self._underlinefg if underlinefg is None else underlinefg
        # pf = self._popup_fg if popup_fg is None else popup_fg
        # pb = self._popup_bg if popup_bg is None else popup_bg
        # pbd = self._popup_border if popup_border is None else popup_border
        # text_widget.tag_add(tag_name, begin_pos, end_pos)
        # text_widget.tag_config(tag_name, foreground=fc, background=bc)
        # # text_widget.tag_config(tag_name, background=bc)
        # if ul:
            # text_widget.tag_config(tag_name, underline=True)
            # text_widget.tag_config(tag_name, underlinefg=uf)
        # text_widget.tag_bind(tag_name, '<Button-1>', lambda x: open_link(the_link))
        # """
        # Pass a list, tuple or set of commands to the lambda. We cannot use a variable for this.
        # Set the cursor, set the highlight and then the action.
        # """
        # text_widget.tag_bind(tag_name, '<Enter>', lambda x: (text_widget.configure(cursor='hand2'),
            # text_widget.tag_config(tag_name, underlinefg=hu, background=hb), self.show_url_popup(self._text_widget, the_link, pf, pb, pbd)))
        # text_widget.tag_bind(tag_name, '<Leave>', lambda x: (text_widget.configure(cursor='xterm'),
            # text_widget.tag_config(tag_name, underlinefg=uf, background=bc), self.kill_url_popup()))


    # def highlight_text(self,
                       # text_widget,
                       # tag_name: str,
                       # the_text: str='',
                       # new_text: str = None,
                       # qty: int=-1,
                       # underline: bool=None,
                       # underlinefg: str=None,
                       # hover_ul: str=None,
                       # hover_bg: str=None,
                       # fg_color: str=None,
                       # bg_color: str=None,
                       # borderwidth: str=None,
                       # relief: str=None,
                       # bold: bool=None):
        # """
        # Highlight one or more words in a textbox.
        # New text, if specified, replaces the existing text. 
        # """
        # try:
            # str0: str = text_widget.get('1.0', 'end')
        # except AttributeError:
            # return
        # num_found: int = 0
        # if len(the_text) > 0:
            # if str0.find(the_text) == -1:
                # return
            # text_length: int = len(the_text)
            # find_location: int = 0
            # while True:
                # find_location = str0.find(the_text, find_location)
                # text_length = len(the_text)
                # if find_location == -1:
                    # break
                # begin_pos = '1.0 linestart+' + str(find_location) + 'c'
                # if new_text is not None and len(new_text) > 0:
                    # end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
                    # text_widget.configure(state='normal')
                    # text_widget.delete(begin_pos, end_pos)
                    # text_widget.insert(begin_pos, new_text)
                    # text_widget.configure(state='disabled')
                    # text_length = len(new_text)
                    # str0: str = text_widget.get('1.0', 'end')
                # end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
                # text_widget.tag_add(tag_name, begin_pos, end_pos)
                # find_location += text_length
                # num_found += 1
                # if num_found==qty:
                    # break
        # if text_widget.tag_nextrange(tag_name, '1.0') == 0:
            # return
        # fc = self._fg_color if fg_color is None else fg_color
        # bc = self._bg_color if bg_color is None else bg_color
        # ul = self._underline if underline is None else underline
        # uf = self._underlinefg if underlinefg is None else underlinefg
        # bw = self._borderwidth if borderwidth is None else borderwidth
        # r = self._relief if relief is None else relief
        # b = self._bold if bold is None else bold
        # text_widget.tag_config(tag_name, foreground=fc, background=bc)
        # if ul:
            # text_widget.tag_config(tag_name, underline=True, underlinefg=uf)
        # if bw:
            # text_widget.tag_config(tag_name, borderwidth=bw)
        # if r: # Ensure borderwidth is at least 3 to permit relief to be actioned.
            # if bw:
                # i = int(bw)
                # if i < 3:
                    # bw1 = '3'
                # else:
                    # bw1 = str(i)
            # else:
                # bw1 = '3'
            # text_widget.tag_config(tag_name, borderwidth=bw1, relief=r)
        # if b: # If we pass just bold to tag_config, it seems to use a different font that the textbox was created with.
            # font_string = text_widget.cget('font') # returned font is str '{family} size'. Split on the } and then the { to separate family.
            # b1 = font_string.split('}')
            # b2 = b1[0].split('{')
            # f = tuple((b2[1], b1[1])) + ('bold',)
            # text_widget.tag_config(tag_name, font=(f))

        
    # def configure(self, **kwargs):
        # self.config(**kwargs)
        
        
    # def config(self, **args):
        # if 'underline' in args:
            # self._underline = args.pop('underline')
        # if 'underlinefg' in args:
            # self._underlinefg = args.pop('underlinefg')
        # if 'hover_ul' in args:
            # self._hover_ul = args.pop('hover_ul')
        # if 'hover_bg' in args:
            # self._hover_bg = args.pop('hover_bg')
        # if 'fg_color' in args:
            # self._fg_color = args.pop('fg_color')
        # if 'bg_color' in args:
            # self._bg_color = args.pop('bg_color')
        # if 'popup_fg' in args:
            # self._popup_fg = args.pop('popup_fg')
        # if 'popup_bg' in args:
            # self._popup_bg = args.pop('popup_bg')
        # if 'popup_border' in args:
            # self._popup_border = args.pop('popup_border')
        # if 'borderwidth' in args:
            # self._borderwidth = args.pop('borderwidth')
        # if 'relief' in args:
            # self._relief = args.pop('relief')
        # if 'bold' in args:
            # self._bold = args.pop('bold')
        # if args:
            # print(f'There are some items left {args}')
        
        
    # def get_config(self):
        # return {'underline': self._underline,
                # 'underlinefg': self._underlinefg,
                # 'hover_ul': self._hover_ul,
                # 'hover_bg': self._hover_bg,
                # 'fg_color': self._fg_color,
                # 'bg_color': self._bg_color,
                # 'popup_fg': self._popup_fg,
                # 'popup_bg': self._popup_bg,
                # 'popup_border': self._popup_border,
                # 'borderwidth': self._borderwidth,
                # 'relief': self._relief,
                # 'bold': self._bold}
                
    # def clear_all_tags(self, text_widget):
        # self.clear_tag(text_widget, '@')

    # def clear_tag(self, text_widget, tag_name: str|tuple|list|set = None):
        # """
        # pass one tagname to delete that tag, a list, tuple or set of tagnames to delete multiple tags, '@' or 'all' to delete all tags.
        # """
        # if tag_name is None:
            # return
        # if type(tag_name)is str:
            # if tag_name == '@' or tag_name.lower() == 'all' :
                # for tagname in text_widget.tag_names():
                    # if tag_name != 'SEL':
                        # text_widget.tag_delete(tagname)
            # else:
                # if tag_name != 'SEL':
                    # text_widget.tag_delete(tag_name)
        # else:
            # if type(tag_name) in [tuple, list, set]:
                # for tagname in tag_name:
                    # text_widget.tag_delete(tagname)
            # else:
                # raise TypeError(f'{tag_name} is neither a list, tuple nor set. It is {str(type(tag_name))}.')
                     


def integer_to_roman(num: int) -> str:
    '''
        This uses roman digits with overbar, which means digit * 1,000 and 
        double overbar, which means digit * 1,000,000
        M=1,000, 'M̅' = 1,000,000 and 'M̿' = 1,000,000,000
        Even though roman numerals don't have megative values, this will return negative.
        If the num is 0, it simply returns 0 - No Roman value
    '''
    roman_combos = [
        'M\u033F', 'C\u033FM\u033F', 'D\u033F', 'C\u033FD\u033F',
        'C\u033F', 'X\u033FC\u033F', 'L\u033F', 'X\u033FL\u033F',
        'X\u033F', 'I\u033FX\u033F', 'V\u033F', 'I\u033FV\u033F',
        'M\u0305', 'C\u0305M\u0305', 'D\u0305', 'C\u0305D\u0305',
        'C\u0305', 'X\u0305C\u0305', 'L\u0305', 'X\u0305L\u0305',
        'X\u0305', 'I\u0305X\u0305', 'V\u0305', 'I\u0305V\u0305',
        'M', 'CM', 'D', 'CD',
        'C', 'XC', 'L', 'XL',
        'X', 'IX', 'V', 'IV',
        'I'
        ]
    roman_values = [
        1000000000, 900000000, 500000000, 400000000,
        100000000, 90000000, 50000000, 40000000,
        10000000, 9000000, 5000000, 4000000,
        1000000, 900000, 500000, 400000,
        100000, 90000, 50000, 40000,
        10000, 9000, 5000, 4000,
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    if num == 0:
        return '0 - No Roman value'
    if num < 0:
        num *= -1
        neg='-'
    else:
        neg=''
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // roman_values[i]):
            roman_num += roman_combos[i]
            num -= roman_values[i]
        i += 1
    if roman_num != '':
        roman_num = neg + roman_num + '_r'
    return roman_num

def roman_to_integer(s: str) -> int:
    from re import sub as re_sub
    ''' Convert roman to integer.
    This does not verify that the input roman number is valid. M̅IM̅ gives 1,999,999 even though 1,999,999 is actually M̅C̅M̅X̅C̅I̅X̅CMXCIX.
    Assumes overstrike characters are standard characters * 1000. M̅ = 1,000,000, X̅ = 10,000.
    Double-overstrike characters are standard characters * 1,000,000. M̿ = 1,000,000,000, I̿ = 1,000,000.
    While there are no negative numbers in Roman, this does support them.
    Replace the overstrike characters with lowercase and double overstrike with unicode characters in the range \u2160 -> \u216F.
    Makes it far simpler to validate as characters are all single byte.
    '''
    s = s.upper()
    to_replace: dict = {'M̅':'m', 'D̅':'d', 'C̅':'c', 'L̅':'l', 'X̅':'x', 'V̅':'v', 'I̅':'i',
                        'M̿':'\u216F', 'D̿':'\u216E', 'C̿':'\u216D', 'L̿':'\u216C', 'X̿':'\u2169', 'V̿':'\u2164', 'I̿':'\u2160'}
    for c in to_replace.keys():
        s = re_sub(c, to_replace[c], s)
    if s[:1] == '-':
        sign = -1
        s = s[1:]
    else:
        sign = 1
    invalid_roman: str = ''
    for i in range(len(s)):
        if s[i] not in '\u216F\u216E\u216D\u216C\u2169\u2164\u2160mdclxviMDCLXVI':
            invalid_roman += s[i]
    invalid_roman = ''.join(dict.fromkeys(invalid_roman))
    num_invalid: int = 0
    msg: str = ''
    adder: str = ''
    txt: str = ' is not a valid roman character.'
    for i in range(len(invalid_roman)):
        num_invalid += 1
        msg += adder + invalid_roman[i]
        adder = ', '
        if num_invalid > 1:
            txt = ' are not valid roman characters.'
    if num_invalid > 0:
        if num_invalid > 1:
            x = msg.rsplit(', ', 1)
            msg = x[0] + ' and ' + x[1]
        raise Exception(msg + txt)
    int_val: int = 0
    roman_symbols: dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                           'i':1000, 'v':5000, 'x':10000, 'l':50000, 'c':100000, 'd':500000, 'm':1000000,
                           '\u2160':1000000, '\u2164': 5000000, '\u2169': 10000000, '\u216C': 50000000, '\u216D': 100000000, '\u216E': 500000000, '\u216F': 1000000000}
    for i in range(len(s)):
        if i > 0 and roman_symbols[s[i]] > roman_symbols[s[i - 1]]:
            int_val += roman_symbols[s[i]] - 2 * roman_symbols[s[i - 1]]
        else:
            int_val += roman_symbols[s[i]]
    return sign * int_val
    
def combine_uom(uom_1: dict, uom_2: dict, op:str) -> dict:
    ''' Combines units of measure, op is either + or -.

    Combines units of measure. When multiplying values, add the units, when dividing values
    subtract units.
    uom_1 & uom_2 are the units dictionaries from the variables.
    op is the operator, either + or -.
    Aftger the operaton, removes any zero value units.
    '''
    uom_3: dict = uom_1.copy() ## Without copy, uom_3 just points to uom_1.
    uom_3.update(uom_2)
    for i in uom_3:
        match op:
            case '+':
                uom_3[i] = uom_1.get(i, 0) + uom_2.get(i, 0)
            case '-':
                uom_3[i] = uom_2.get(i, 0) - uom_1.get(i, 0)
    # Delete units which have 0 value.
    for k, v in uom_3.copy().items():
        if v == 0:
            del uom_3[k]
    return uom_3

def float_to_sexagesimal(number: float, sig_digits: int = 8) -> str:
    '''Convert decimal to sexagesimal.'''
    if number == 0:
        return '0;'
    if number < 0:
        number *= -1
        neg = '-'
    else:
        neg = ''
    int_part = int(number)
    frac_part = number - int_part
    if int_part != 0:
        retval = ';'
        joiner = ''
        while int_part > 0:
            r = int(int_part % 60)
            retval = str(r) + joiner + retval
            int_part = (int_part - r) / 60
            joiner = ','
    else:
        retval = '0;'
    if frac_part != 0:
        num_ctr = sig_digits
        joiner = ''
        frac_part = round(frac_part, num_ctr)
        while num_ctr != 0:
            frac_part = frac_part * 60
            r = int(frac_part)
            retval = retval + joiner + str(r)
            frac_part = frac_part - r
            joiner = ','
            if frac_part == 0:
                num_ctr = 0
            else:
                num_ctr -= 1
                frac_part = round(frac_part, num_ctr)
    return neg + retval


def sexagesimal_to_float(sexag_text: str, sig_digits: int = 8) -> list[int, float]:
    '''Convert segagesimal to decimal.
       Returns following int values.
        0 - All OK.
        1 - Invalid format, more than 1 semi-colon.
        2 - Non-integer value(s) supplied.
    '''
    if sexag_text.count(';') != 1:
        return 1, 0.0
    x, y = sexag_text.split(';')
    xn = x.split(',')
    yn = y.split(',')
    if xn == ['']:
        xn = ['0']
    if yn == ['']:
        yn = ['0']
    try:
        xn_list = list(reversed(list(map(int, xn))))
        yn_list = list(map(int, yn))
    except:
        return 2, 0.0
    a = 0.0
    m = 1
    s_d = sig_digits
    for x in xn_list:
        a = a + x * m
        m = round(m * 60, s_d)
        s_d -= 1
    m = 1 / 60
    s_d = sig_digits
    for y in yn_list:
        a = a + y * m
        m = round(m / 60, s_d)
        s_d -= 1
    return 0, a


def eng_format(x: float | int, sig_decs: int=3, si: bool=True) -> str:
    '''
    Returns float/int value <x> formatted in a simplified engineering format -
    using an exponent that is a multiple of 3.

    sig_decs: number of significant decimals

    si: if true, use SI suffix for exponent, e.g. k instead of e3, n instead of
    e-9 etc.
    '''
    from math import log10, floor
    x = float(x)
    sign = ''
    if x < 0:
        x = -x
        sign = '-'
    if x == 0:
        exp = 0
        exp3 = 0
        x3 = 0
    else:
        exp = int(floor(log10(x)))
        exp3 = exp - (exp % 3)
        x3 = x / (10 ** exp3)
        x3 = round(x3, sig_decs)
        if x3 == int(x3):  # prevent from displaying .0
            x3 = int(x3)
    if si and exp3 == 0:  # Exponent is either 0, 1 or 2
        if exp == 2:
            x3 = x3 / 100
            exp3_text = 'h'
        elif exp == 1:
            x3 = x3 / 10
            exp3_text = 'da'
        else:
            exp3_text = ''
        if x3 != 0:
            x3 = round(x3, sig_decs)
        if x3 == int(x3):
            x3 = int(x3)
    elif si and -30 <= exp3 <= 30 and exp3 != 0:
        exp3_text = 'qryzafpn\u03BCm kMGTPEZYRQ'[exp3 // 3 + 10]
    elif exp3 == 0:
        exp3_text = ''
    else:
        exp3_text = 'e%s' % exp3
    return '%s%s%s' % (sign, x3, exp3_text)

from customtkinter import CTkFont
def get_width(text_item: str, fontname: CTkFont | str, fontsize: int | str = 12) -> int:
    if type(fontname) is str:
        fontname = CTkFont(fontname, int(fontsize))
    lines = text_item.splitlines()
    width: int = 0
    for line in lines:
        width = max(width, fontname.measure(line))
    return width

# from tkinter import Toplevel, Label, Button, StringVar, font as tkfont, CENTER, LEFT, RIGHT
# from tkinter.scrolledtext import ScrolledText
# from tkinter.ttk import Separator
# class PopupMessage():
    # """
    # Author: Kevin Glentworth
    # Date: August-2025
    # Description: popup message with either yes/no buttons or close button.
    # Returns y or n for Yes/No buttons, nothing for Close button.
    # If a textbox is used, a reference to it can be retrieved for further actions.
    # Used ScrolledText so I don't have to bother with manually adding a vertical scroll bar.
    # """
    # def __init__(self, master):
        # self.master = master
        # self.yes_no: str = 'n'
        # self.textbox = None


    # def colour_button(self, button: Button, Enter: bool, colour:str):
        # """
        # Colours the button depending upon whether the action is <Enter> or <Leave>.
        # """
        # if Enter:
            # button.configure(bg=colour)
        # else:
            # button.configure(bg=colour)
        
            
    # def show(self,
             # title: str = '',
             # message: str = '',
             # alignment: str = 'center',
             # x_pos: float = 0.2,
             # y_pos: float = 0.4,
             # yesno: bool = False,
             # use_text_box: bool = False,
             # multi_line: bool = False,
             # m_width: int = 50, # characters
             # m_height: int = 30, # lines
             # max_width: int = 100, # characters
             # max_height: int = 30, # lines
             # wait: bool = True,
             # font: list = ('Code New Roman', 14)):
        # '''Shows a message window and waits for user to press OK or Yes/No.
           # If wait is True, the message window must be closed before control
           # returns to the calling window.

        # :param title: str
        # :param message: str
        # :param alignment: str [LEFT, CENTER, RIGHT]
        # :param x_pos: float [value between 0 and 1]
        # :param y_pos: float [value bewtween 0 and 1]
        # :param yesno: bool [Use Yes and No buttons or just a Close button]
        # :param use_text_box: bool [Use a textbox rather than a label]
        # :param multi_line: bool [Allow multiple lines]
        # :param m_width: int [width in characters]
        # :param m_height: int [height in lines]
        # :param max_width: int [maximum width in characters]
        # :param wait: bool [wait makes returns to calling process only after window is clsoed]
        # :param font: list(Family:str, size: int)
        # :return:
        # '''

        # def popup_yes() -> None:
            # self.yes_no = 'y'
            # self.message_window.destroy()

        # def popup_no() -> None:
            # self.yes_no = 'n'
            # self.message_window.destroy()
            
        # geo = self.master.winfo_geometry().replace('+', 'x').split('x')
        # width = int(geo[0])
        # height = int(geo[1])
        # left = int(geo[2])
        # top = int(geo[3])
        # new_left = int(left + width * x_pos)
        # new_top = int(top + height * y_pos)
        # if multi_line:
            # num_lines: int = 0
            # lines = message.splitlines()
            # width: int = 0
            # for line in lines:
                # width = max(width, len(line))
                # num_lines += 1
            # m_width = width + 2
            # m_height = min(num_lines, m_height) - 1
        # if m_width > max_width:
            # m_width = max_width
        # self.message_window: Toplevel = Toplevel()
        # self.message_window.title('')
        # if alignment == '':
            # alignment = CENTER
        # self.s1 = StringVar(self.message_window, title)
        # if title != None or title == '':
            # Label(master=self.message_window,
                  # textvariable=self.s1,
                  # font=font,
                  # justify=alignment).pack()
            # Separator(self.message_window, orient='horizontal').pack(fill='x')
        # self.textbox = None
        # if use_text_box:
            # self.textbox = ScrolledText(master=self.message_window,
                                        # fg='blue',
                                        # bg='lightyellow',
                                        # width=m_width,
                                        # height=m_height,
                                        # wrap='word',
                                        # font=font)
            # self.textbox.pack()
            # self.textbox.insert('0.0', message)
            # self.textbox.configure(state='disabled')
        # else:
            # self.s2 = StringVar(self.message_window, message)
            # Label(master=self.message_window,
                  # textvariable=self.s2,
                  # fg='navy',
                  # bg='lightyellow',
                  # justify=alignment,
                  # font=font).pack(side='top', pady=10, padx=10)
        # if yesno:
            # self.yes_no = 'n'
            # self.b_yes = Button(master=self.message_window,
                                # text='Yes',
                                # command=popup_yes,
                                # width=5,
                                # height=1,
                                # bd=2,
                                # fg='blue',
                                # bg='rosybrown1',
                                # font=font)
            # self.b_yes.pack(side=LEFT)
            # self.b_yes.bind('<Enter>', lambda x: self.colour_button(self.b_yes, True, 'lightskyblue2'))
            # self.b_yes.bind('<Leave>', lambda x: self.colour_button(self.b_yes, False, 'rosybrown1'))
            # self.b_no = Button(master=self.message_window,
                               # text='No',
                               # command=popup_no,
                               # width=5,
                               # height=1,
                               # bd=2,
                               # fg='blue',
                               # bg='rosybrown1',
                               # font=font)
            # self.b_no.pack(side=RIGHT)
            # self.b_no.bind('<Enter>', lambda x: self.colour_button(self.b_no, True, 'lightskyblue2'))
            # self.b_no.bind('<Leave>', lambda x: self.colour_button(self.b_no, False, 'rosybrown1'))
            # self.message_window.bind('<Return>', lambda event: popup_no())
            # self.message_window.bind('<space>', lambda event: popup_no())
            # self.message_window.bind('<Escape>', lambda event: popup_no())
            # self.message_window.bind('y', lambda event: popup_yes())
            # self.message_window.bind('n', lambda event: popup_no())
            # self.message_window.bind('Y', lambda event: popup_yes())
            # self.message_window.bind('N', lambda event: popup_no())
        # else:
            # self.b_close = Button(master=self.message_window,
                                  # text='Close',
                                  # command=self.message_window.destroy,
                                  # width=7,
                                  # height=1,
                                  # bd=2,
                                  # fg='yellow',
                                  # bg='steelblue4',
                                  # font=font)
            # self.b_close.pack()
            # self.b_close.bind('<Enter>', lambda x: self.colour_button(self.b_close, True, 'lightskyblue2'))
            # self.b_close.bind('<Leave>', lambda x: self.colour_button(self.b_close, False, 'steelblue4'))
            # self.message_window.bind('<Return>', lambda event: self.message_window.destroy())
            # self.message_window.bind('<space>', lambda event: self.message_window.destroy())
            # self.message_window.bind('<Escape>', lambda event: self.message_window.destroy())
        # self.message_window.geometry(f'+{new_left}+{new_top}')
        # self.message_window.update_idletasks()
        # self.message_window.focus_force()
        # if wait:
            # self.message_window.grab_set()
            # self.master.wait_window(self.message_window)
        
    # def get_textbox(self) -> any:
        # """
        # Returns the textbox created. If no textbox was used, returns None. This allows other operations to be performed
        # on the textbox by the calling program.
        # """
        # return self.textbox
        
    # def get(self) -> str:
        # """
        # Returns the value of self.yes_no
        # """
        # return self.yes_no
        
    # def set(self) -> None:
        # """
        # Sets the value of self.yes_no to 'y'
        # """
        # self.yes_no = 'y'
 
 
 
from tkinter import Toplevel, Label, LEFT, SOLID
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
    
# from webbrowser import open_new as open_link
# from tkinter import Tk, Toplevel, Label, font
# class TextboxLink():
    # """
    # Author: Kevin Glentworth
    # Date: August-2025
    # Extends textbox widget to allow for word highlighting and URLs.
    # __init__ sets the initial values for each configurable item. borderwidth and relief apply to highlight_word only.
    # config allows those values to be changed for any future calls, but not for existing links and words.
    # add_link and highlight_word allow the options to be changed for that item only.
    # """
    # def __init__(self,
                 # underline: bool=True,
                 # underlinefg: str='blue',
                 # hover_ul: str='green',
                 # hover_bg: str='orange',
                 # fg_color: str='blue',
                 # bg_color: str='yellow',
                 # popup_fg: str='blue',
                 # popup_bg: str = 'lightyellow',
                 # popup_border: str = 'red',
                 # popup_font: list = ('Code New Roman', 13),
                 # borderwidth: str='',
                 # show_url: bool = True):
        # self._underline = underline
        # self._underlinefg = underlinefg
        # self._hover_ul = hover_ul
        # self._hover_bg = hover_bg
        # self._fg_color = fg_color
        # self._bg_color = bg_color
        # self._popup_fg = popup_fg
        # self._popup_bg = popup_bg
        # self._popup_border = popup_border
        # self._popup_font = popup_font
        # self._borderwidth = borderwidth
        # self._show_url = show_url

        
    # def show_url_popup(self, text_widget, message, p_fg: str='blue', p_bg: str='lightyellow', p_bd: str='red', p_font: list = None):
        # """
        # Shows the URL of the link under the mouse.

        # If the mouse pointer ends up over the popup object, it is treated as an <Exit>, which closes the popup window.
        # As the mouse is still within the text_widget, it then performs another <Enter> and goes into a loop until the mouse is
        # moved off the popup. Adjust both x and y to keep the popup away from the mouse cursor.
        # The popup_border (p_bd) isn't a Label widget item, it is applied to the Toplevel widget with padding, to make it appear
        # as a border colour.
        # """
        # mouse_x = self._text_widget.winfo_pointerx() + 10
        # mouse_y = self._text_widget.winfo_pointery() - 30

        # self.popup = Toplevel(self._text_widget, bg=p_bd, padx=2, pady=2) # padx & pady allow the colour to show around the label.
        # self.popup.overrideredirect(True)
        # self.popup.geometry(f'+{mouse_x}+{mouse_y}')
        # self.popup.attributes('-topmost', True) # Ensure the popup is above everything else.

        # # Label(self.popup, text=message, fg=p_fg, bg=p_bg, relief='flat', borderwidth=0, padx=2, pady=2, font=('Code New Roman',13)).pack()
        # Label(self.popup, text=message, fg=p_fg, bg=p_bg, relief='flat', borderwidth=0, padx=2, pady=2, font=p_font).pack()
        # #self.popup.update_idletasks()
        # #self._text_widget.update_idletasks()

        
    # def kill_url_popup(self):
        # self.popup.destroy()


    # def add(self,
            # text_widget,
            # the_text: str,
            # tag_name: str,
            # the_link: str,
            # new_text: str = None,
            # underline: bool=None,
            # underlinefg: str=None,
            # hover_ul: str=None,
            # hover_bg: str=None,
            # fg_color: str=None,
            # bg_color: str=None,
            # popup_fg: str=None,
            # popup_bg: str=None,
            # popup_border: str=None,
            # popup_font: list = None,
            # show_url: bool = None):
        # """
        # Highlight text and create a link in a text widget that supports tags. The parameters here over-ride those
        # set in __init__, but only for this call.
        # To change the colours for future calls, use config.
        # """
        # try:
            # text_widget.tag_add('????',1.0, 'end')
        # except AttributeError:
            # raise Exception(f'item {text_widget} does not support tags.')
        # text_widget.tag_delete('????')
        # str0: str = text_widget.get('1.0', 'end')
        # if len(str0) == 0:
            # return
        # if (text_length := len(the_text)) == 0:
            # return
        # if (find_location := str0.find(the_text)) == -1:
            # return
        # begin_pos = '1.0 linestart+' + str(find_location) + 'c'
        # if new_text is not None and len(new_text) > 0:
            # end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
            # text_widget.configure(state='normal')
            # text_widget.delete(begin_pos, end_pos)
            # text_widget.insert(begin_pos, new_text)
            # text_widget.configure(state='disabled')
            # text_length = len(new_text)
            # str0 = text_widget.get('1.0', 'end') # reload text from widget rather than slicing str0
        # end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
        # self._text_widget = text_widget
        # fc = self._fg_color if fg_color is None else fg_color
        # bc = self._bg_color if bg_color is None else bg_color
        # ul = self._underline if underline is None else underline
        # uf = self._underlinefg if underlinefg is None else underlinefg
        # hu = self._hover_ul if hover_ul is None else hover_ul
        # hb = self._hover_bg if hover_bg is None else hover_bg
        # pf = self._popup_fg if popup_fg is None else popup_fg
        # pb = self._popup_bg if popup_bg is None else popup_bg
        # pbd = self._popup_border if popup_border is None else popup_border
        # p_font = self._popup_font if popup_font is None else popup_font
        # su = self._show_url if show_url is None else show_url
        # text_widget.tag_add(tag_name, begin_pos, end_pos)
        # text_widget.tag_config(tag_name, foreground=fc, background=bc)
        # if ul:
            # text_widget.tag_config(tag_name, underline=True, underlinefg=uf)
        # text_widget.tag_bind(tag_name, '<Button-1>', lambda x: open_link(the_link))
        # """
        # Need to define the cursor, the colours and the action for <Enter> and <Leave>. We pass an embedded
        # list or tuple of commands to the lambda for this, we cannot use a list variable or a tuple variable.
        # """
        # if su:
            # text_widget.tag_bind(tag_name, '<Enter>', lambda x: (text_widget.configure(cursor='hand2'),
                                                                # text_widget.tag_config(tag_name, underlinefg=hu, background=hb),
                                                                # self.show_url_popup(self._text_widget, the_link, pf, pb, pbd, p_font)))
            # text_widget.tag_bind(tag_name, '<Leave>', lambda x: (text_widget.configure(cursor='xterm'),
                                                                 # text_widget.tag_config(tag_name, underlinefg=uf, background=bc),
                                                                 # self.kill_url_popup()))
        # else:
            # text_widget.tag_bind(tag_name, '<Enter>', lambda x: (text_widget.configure(cursor='hand2'),
                                                                # text_widget.tag_config(tag_name, underlinefg=hu, background=hb)))
            # text_widget.tag_bind(tag_name, '<Leave>', lambda x: (text_widget.configure(cursor='xterm'),
                                                                 # text_widget.tag_config(tag_name, underlinefg=uf, background=bc)))


    # def configure(self, **kwargs):
        # self.config(**kwargs)
        
        
    # def config(self, **kwargs):
        # if 'underline' in kwargs:
            # self._underline = kwargs.pop('underline')
        # if 'underlinefg' in kwargs:
            # self._underlinefg = kwargs.pop('underlinefg')
        # if 'hover_ul' in kwargs:
            # self._hover_ul = kwargs.pop('hover_ul')
        # if 'hover_bg' in kwargs:
            # self._hover_bg = kwargs.pop('hover_bg')
        # if 'fg_color' in kwargs:
            # self._fg_color = kwargs.pop('fg_color')
        # if 'bg_color' in kwargs:
            # self._bg_color = kwargs.pop('bg_color')
        # if 'popup_fg' in kwargs:
            # self._popup_fg = kwargs.pop('popup_fg')
        # if 'popup_bg' in kwargs:
            # self._popup_bg = kwargs.pop('popup_bg')
        # if 'popup_border' in kwargs:
            # self._popup_border = kwargs.pop('popup_border')
        # if 'popup_font' in kwargs:
            # self._popup_font = kwargs.pop('popup_font')
        # if 'borderwidth' in kwargs:
            # self._borderwidth = kwargs.pop('borderwidth')
        # if 'show_url' in kwargs:
            # self._show_url = kwargs.pop('show_url')
        # if kwargs:
            # raise ValueError(f'{list(kwargs.keys())} not supported.')
        
    # def get_config(self) -> dict:
        # return vars(TextboxLink())


# from webbrowser import open_new as open_link
# from tkinter import Tk, Toplevel, Label, font
# class TextboxHighlight():
    # """
    # Author: Kevin Glentworth
    # Date: August-2025
    # Extends textbox widget to allow for text highlighting.
    # __init__ sets the initial values for each configurable item.
    # add allows the options to be changed for that item only.
    # """
    # def __init__(self,
                 # underline: bool=True,
                 # underlinefg: str='blue',
                 # hover_ul: str='green',
                 # hover_bg: str='orange',
                 # fg_color: str='blue',
                 # bg_color: str='yellow',
                 # borderwidth: str='',
                 # relief: str='',
                 # bold: bool = False):
        # self._underline = underline
        # self._underlinefg = underlinefg
        # self._hover_ul = hover_ul
        # self._hover_bg = hover_bg
        # self._fg_color = fg_color
        # self._bg_color = bg_color
        # self._borderwidth = borderwidth
        # self._relief = relief
        # self._bold = bold
        

    # def add(self,
            # text_widget,
            # tag_name: str,
            # the_text: str='',
            # new_text: str = None,
            # qty: int=-1,
            # underline: bool=None,
            # underlinefg: str=None,
            # hover_ul: str=None,
            # hover_bg: str=None,
            # fg_color: str=None,
            # bg_color: str=None,
            # borderwidth: str=None,
            # relief: str=None,
            # bold: bool=None):
        # """
        # Highlight one or more words in a textbox.
        # New text, if specified, replaces the existing text. 
        # """
        # try:
            # str0: str = text_widget.get('1.0', 'end')
        # except AttributeError:
            # return
        # num_found: int = 0
        # if len(the_text) > 0:
            # if str0.find(the_text) == -1:
                # return
            # text_length: int = len(the_text)
            # find_location: int = 0
            # while True:
                # find_location = str0.find(the_text, find_location)
                # text_length = len(the_text)
                # if find_location == -1:
                    # break
                # begin_pos = '1.0 linestart+' + str(find_location) + 'c'
                # if new_text is not None and len(new_text) > 0:
                    # end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
                    # text_widget.configure(state='normal')
                    # text_widget.delete(begin_pos, end_pos)
                    # text_widget.insert(begin_pos, new_text)
                    # text_widget.configure(state='disabled')
                    # text_length = len(new_text)
                    # str0: str = text_widget.get('1.0', 'end')
                # end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
                # text_widget.tag_add(tag_name, begin_pos, end_pos)
                # find_location += text_length
                # num_found += 1
                # if num_found==qty:
                    # break
        # if text_widget.tag_nextrange(tag_name, '1.0') == 0:
            # return
        # self._text_widget = text_widget
        # fc = self._fg_color if fg_color is None else fg_color
        # bc = self._bg_color if bg_color is None else bg_color
        # ul = self._underline if underline is None else underline
        # uf = self._underlinefg if underlinefg is None else underlinefg
        # bw = self._borderwidth if borderwidth is None else borderwidth
        # r = self._relief if relief is None else relief
        # b = self._bold if bold is None else bold
        # text_widget.tag_config(tag_name, foreground=fc, background=bc)
        # if ul:
            # text_widget.tag_config(tag_name, underline=True, underlinefg=uf)
        # if bw:
            # text_widget.tag_config(tag_name, borderwidth=bw)
        # if r: # Ensure borderwidth is at least 3 to permit relief to be actioned.
            # if bw:
                # i = int(bw)
                # if i < 3:
                    # bw1 = '3'
                # else:
                    # bw1 = str(i)
            # else:
                # bw1 = '3'
            # text_widget.tag_config(tag_name, borderwidth=bw1, relief=r)
        # if b: # If we pass just bold to tag_config, font=('bold',), it seems to use a different font than the textbox was created with.
            # font_string = text_widget.cget('font') # returned font is str '{family} size'. Split on the } and then the { to separate family.
            # b1 = font_string.split('}')
            # b2 = b1[0].split('{')
            # f = tuple((b2[1], b1[1])) + ('bold',)
            # text_widget.tag_config(tag_name, font=(f))

        
    # def configure(self, **kwargs):
        # self.config(**kwargs)
        
        
    # def config(self, **kwargs):
        # if 'underline' in kwargs:
            # self._underline = kwargs.pop('underline')
        # if 'underlinefg' in kwargs:
            # self._underlinefg = kwargs.pop('underlinefg')
        # if 'hover_ul' in kwargs:
            # self._hover_ul = kwargs.pop('hover_ul')
        # if 'hover_bg' in kwargs:
            # self._hover_bg = kwargs.pop('hover_bg')
        # if 'fg_color' in kwargs:
            # self._fg_color = kwargs.pop('fg_color')
        # if 'bg_color' in kwargs:
            # self._bg_color = kwargs.pop('bg_color')
        # if 'borderwidth' in kwargs:
            # self._borderwidth = kwargs.pop('borderwidth')
        # if 'relief' in kwargs:
            # self._relief = kwargs.pop('relief')
        # if 'bold' in kwargs:
            # self._bold = kwargs.pop('bold')
        # if kwargs:
            # raise ValueError(f'{list(kwargs.keys())} not supported.')
        
        
    # def get_config(self) -> dict:
        # return vars(TextboxHighlight())
                
    # def clear_all_tags(self, text_widget):
        # self.clear_tag(text_widget, '@')

    # def clear_tag(self, text_widget, tag_name: str|tuple|list|set = None):
        # """
        # pass one tagname to delete that tag, a list, tuple or set of tagnames to delete multiple tags, '@' or 'all' to delete all tags.
        # """
        # if tag_name is None:
            # return
        # if type(tag_name)is str:
            # if tag_name == '@' or tag_name.lower() == 'all' :
                # for tagname in text_widget.tag_names():
                    # if tag_name != 'SEL':
                        # text_widget.tag_delete(tagname)
            # else:
                # if tag_name != 'SEL':
                    # text_widget.tag_delete(tag_name)
        # else:
            # if type(tag_name) in [tuple, list, set]:
                # for tagname in tag_name:
                    # text_widget.tag_delete(tagname)
            # else:
                # raise TypeError(f'{tag_name} is neither a list, tuple nor set. It is {str(type(tag_name))}.')
                     
