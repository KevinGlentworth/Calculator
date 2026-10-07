from tkinter import Tk, Toplevel, Frame, Label, Button, StringVar, font as tkfont, CENTER, LEFT, RIGHT, BOTTOM
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Separator
# from customtkinter import CTkButton

class SimplePopupMessage():
    """
    Author: Kevin Glentworth
    Date: July 2026
    Description: Simple popup message with buttons.
                 Displays the message with pre-defined colours etc.
                 Default button is always the first button.
    Parameters: Title, Message & Buttons
    .get() Returns the value of the clicked button.
    """
    def __init__(self, master):
        self.master = master
        self.answer: str = ''

    def show(self,
             title: str = 'Simple Popup Message',
             message: str = 'The default message.',
             buttons: list = ['OK']):

        '''Shows a message window and waits for user to press a button.
            Window has predefined colours, font sizes and is centred on the screen.
            The calling window will wait until themessage window is clicked.
            On a multi button window, the first button is always the default.

        :param title: str
        :param message: str
        :param buttons: list [If blank, just have OK button, else show these.]
        :method get: [Returns the text of the pressed button.]
        '''

        self.message_window: Toplevel = Toplevel(bg='lemonchiffon')
        self.message_window.title('')
        self.message_window.attributes('-topmost', True)
        l=Label(master=self.message_window, text=title, bg='lemonchiffon', font=('', 14))
        l.pack()
        l=Label(master=self.message_window, text=message, bg='lemonchiffon', fg='navy', font=('', 14))
        l.pack(side='top', pady=10, padx=10)
        if len(buttons) == 0:
            buttons=['OK']
        my_frame = Frame(master=self.message_window, bg='lemonchiffon')
        for index, button in enumerate(buttons):
            if index == 0:
                c = 'green'
            else:
                c = 'red'
            b = Button(master=my_frame, text=button, fg=c, font=('', 14))
            b.configure(command=lambda x=button: self.popup_answer(x))
            b.grid(row=0, column=index, padx=6, pady=2)
        my_frame.pack()
        self.message_window.update_idletasks()
        geo = self.master.winfo_geometry().replace('+', 'x').split('x')
        left = int(geo[2])
        top = int(geo[3])
        geo = self.message_window.winfo_geometry().replace('+', 'x').split('x')
        width = int(geo[0])
        height = int(geo[1])
        left = left + width // 2
        top = top + height // 2
        self.message_window.geometry(f'+{left}+{top}')
        self.message_window.bind('<Return>', lambda event: self.popup_answer(buttons[0]))
        self.message_window.bind('<space>', lambda event: self.popup_answer(buttons[0]))
        self.message_window.bind('<Escape>', lambda event: self.popup_answer(buttons[0]))
        self.message_window.protocol('WM_DELETE_WINDOW', lambda: self.popup_answer(buttons[0]))
        self.message_window.focus_force()
        self.message_window.grab_set()
        self.master.wait_window(self.message_window)
        

    def popup_answer(self, answer: str='') -> None:
        self.answer=answer
        self.message_window.destroy()


    def get(self) -> str:
        '''
        Returns the label off the clicked, or default, button.
        '''
        return self.answer


class PopupMessage():
    """
    Author: Kevin Glentworth
    Date: July 2026
    Description: popup message with buttons.
    .get() Returns the value of the clicked button.
    .get_textbox() If a textbox is used, a reference to it can be retrieved for
        further actions, e.g. using tags to highlight text or assign a URL.
    """
    def __init__(self, master):
        self.master = master
        self.answer: str = ''
        self.textbox: ScrolledText = None


    def show(self,
             title: str = 'Popup Message',
             message: str = 'The default message.',
             alignment: str = 'left',
             x_pos: float = 0.2,
             y_pos: float = 0.4,
             screen_relative: bool = False,
             buttons: list = ['OK'],
             default_button: int = 0,
             default_button_colour: str = 'green',
             other_button_colour: str = 'red',
             window_colour: str = 'lemonchiffon',
             use_text_box: bool = False,
             multi_line: bool = False,
             m_width: int = 50, # characters
             m_height: int = 30, # lines
             max_width: int = 100, # characters
             max_height: int = 30, # lines
             wait: bool = True,
             timeout: int = 0, # seconds, 0 = no timout. Closes window and returns default value after timeout.
             font: list = ('Code New Roman', 14)):
        '''Shows a message window and waits for user to press a button.

        :param title: str
        :param message: str
        :param alignment: str [LEFT, CENTER, RIGHT, WEST, EAST]
        :param x_pos: float [value between 0 and 1]. Value > 1 is pixels
        :param y_pos: float [value bewtween 0 and 1]. Value > 1 is pixels.
        :screen_relative: bool [position relative to current window or screen.]
        :param buttons: list [If blank, just have OK button, else show these.]
        :param default_button: int [When enter is pressed or window is closed.]
        :param use_text_box: bool [Use a textbox rather than a label]
        :param multi_line: bool [Allow multiple lines]
        :param m_width: int [width in characters]
        :param m_height: int [height in lines]
        :param max_width: int [maximum width in characters]
        :param max_height: int [maximum height in characters]
        :param wait: bool [True returns to calling process only after window is closed.
                           False returns immediately, leaving the textbox visible.]
        :param font: list [Family:str, size: int)
        
        :method get: [Returns the text of the pressed button.]
        :method get_textbox: [Returns the textbox, if used.]

        '''

        # def popup_answer(answer:str='') -> None:
        #     if answer == '':
        #         answer=buttons[0]
        #     self.answer = answer.strip(' ')
        #     self.message_window.destroy()


        self.buttons = buttons
        if multi_line:
            num_lines: int = 0
            lines = message.splitlines()
            width: int = 0
            for line in lines:
                width = max(width, len(line))
                num_lines += 1
            m_width = width + 2
            m_height = min(num_lines, m_height) - 1
        m_height = min(m_height, max_height)
        m_width = min(m_width, max_width)
        x_pos = abs(x_pos)
        y_pos = abs(y_pos)
        self.message_window: Toplevel = Toplevel(background=window_colour)
        self.message_window.title('')
        self.message_window.attributes('-topmost', True)
        if alignment == '':
            alignment = LEFT
        # get alignment based upon first character of alignment, default is 'left'. middle, centre, left, right, west, east
        alignment = {'m':CENTER, 'c':CENTER, 'l':LEFT, 'r':RIGHT, 'w':LEFT, 'e':RIGHT}.get(alignment[:1].lower(), LEFT)
        self.s1 = StringVar(self.message_window, title)
        if title != None or title == '':
            Label(master=self.message_window,
                  textvariable=self.s1,
                  background=window_colour,
                  font=font,
                  justify=alignment).pack()
            Separator(self.message_window, orient='horizontal').pack(fill='x')
        self.textbox = None
        if use_text_box:
            self.textbox = ScrolledText(master=self.message_window,
                                        fg='blue',
                                        bg=window_colour,
                                        width=m_width,
                                        height=m_height,
                                        wrap='word',
                                        font=font)
            self.textbox.pack()
            self.textbox.insert('0.0', message)
            self.textbox.configure(state='disabled')
        else:
            self.s2 = StringVar(self.message_window, message)
            Label(master=self.message_window,
                  textvariable=self.s2,
                  fg='navy',
                  bg=window_colour,
                  justify=alignment,
                  font=font).pack(side='top', pady=10, padx=10)
        max_len = 0
        if len(buttons) == 0:
            buttons=['OK']
        for b in buttons:
            max_len = max(max_len, len(b))
        max_len += 2 # Allow for space at each end
        max_len = max(max_len, 8) # Button is at least 8 characters
        new_buttons: list = []
        if default_button < 0:
            default_button = 0
        if default_button >= len(buttons):
            default_button = len(buttons) - 1
        # Centre the button text in the button.
        buttons_bound = set()
        for index, button in enumerate(buttons):
            leading_chars = int((max_len - len(button)) / 2)
            trailing_chars = max_len - len(button) - leading_chars
            new_button: str = ' ' * (leading_chars-1) + button + ' ' * (trailing_chars-1)
            new_buttons.append(new_button)
        # buttons = new_buttons.copy()
        my_frame = Frame(master=self.message_window, bg=window_colour)
        for index, button in enumerate(new_buttons):
            if index == default_button:
                b_colour = default_button_colour
            else:
                b_colour = other_button_colour
            b = Button(master=my_frame, text=button, width=max_len, font=font, fg=b_colour)
            b.configure(command=lambda x=button: self.popup_answer(x))
            b.grid(row=0, column=index, padx=6, pady=2)
        my_frame.pack()
        self.message_window.update_idletasks()
        if screen_relative:
            master_width = self.master.winfo_screenwidth()
            master_height = self.master.winfo_screenheight()
            master_left = 0
            master_top = 0
        else:
            geo = self.master.winfo_geometry().replace('+', 'x').split('x')
            master_width = int(geo[0])
            master_height = int(geo[1])
            master_left = int(geo[2])
            master_top = int(geo[3])
        geo = self.message_window.winfo_geometry().replace('+', 'x').split('x')
        width = int(geo[0])
        height = int(geo[1])
        if 0 < x_pos < 1:
            new_left = int(master_left + master_width * x_pos)
        else:
            new_left = int(x_pos)
        if 0 < y_pos < 1:
            new_top = int(master_top + master_height * y_pos)
        else:
            new_top = int(y_pos)
        if new_left + width > self.master.winfo_screenwidth():
            new_left = self.master.winfo_screenwidth() - width - 10
        if new_top + height > self.master.winfo_screenheight():
            new_top = self.master.winfo_screenheight() - height - 30 # Use 30 for visible taskbar.
        self.message_window.geometry(f'+{new_left}+{new_top}')
        self.message_window.protocol('WM_DELETE_WINDOW', lambda: self.popup_answer(new_buttons[default_button]))
        self.message_window.bind('<Return>', lambda event: self.popup_answer(new_buttons[default_button]))
        self.message_window.bind('<space>', lambda event: self.popup_answer(new_buttons[default_button]))
        self.message_window.bind('<Escape>', lambda event: self.popup_answer(new_buttons[default_button]))
        self.message_window.focus_force()
        if timeout > 0 and timeout <= 60:
            self.message_window.after(timeout * 1000, lambda: self.popup_answer())
        if wait:
            self.message_window.grab_set()
            self.master.wait_window(self.message_window)
        

    def popup_answer(self, answer:str='') -> None:
        if answer == '':
            answer=self.buttons[0]
        self.answer = answer.strip(' ')
        self.message_window.destroy()


    def get_textbox(self) -> any:
        '''
        Returns the textbox created. If no textbox was used, returns None. This allows other operations to be
         performed on the textbox by the calling program.
        '''
        return self.textbox
        
        
    def get(self) -> str:
        '''
        Returns the label off the clicked, or default, button.
        '''
        return self.answer
        
        
if __name__ == '__main__':
    tk = Tk()

    print('** PopupMessage **')
    pm = PopupMessage(tk)
    pm.show()
    print(f'pm.get:{pm.get()}')
    pm.show(title='Testing new PopupMessage',
            message='Multiple Options, default = 2nd button',
            x_pos=0.25, y_pos=0.25,
            use_text_box=True,
            max_height=5,
            buttons=['Accept', 'Cancel', 'Dismiss', 'Ignore', 'Fail'],
            default_button=1)
    print(f'pm.get={pm.get()}')
    pm.show(title='Testing new PopupMessage',
            message='One Button, bottom right',
            x_pos=3400, y_pos=1400,
            use_text_box=True,
            max_height=5,
            buttons=['No way'],
            screen_relative=True)
    print(f'pm.get={pm.get()}')
    pm.show(title='Testing new PopupMessage',
            message='Default Buttons',
            x_pos=350, y_pos=300,
            max_height=5)
    print(f'pm.get={pm.get()}')
    pm.show(title='Testing new PopupMessage',
            message='Good afternoon',
            x_pos=-350, y_pos=-300,
            max_height=5,
            timeout=5,
            buttons=['One', 'Two', 'Three'])
    print(f'pm.get={pm.get()}')

    print('** SimplePopupMessage **')
    spm = SimplePopupMessage(tk)
    spm.show(title='Simple: Title testing',
             message='Default values')
    print(f'spm.get={spm.get()}')
    spm.show(title='Simple: Second title',
             message='3 buttons',
             buttons=['Yes', 'No', 'Maybe'])
    print(f'spm.get={spm.get()}')
    exit()