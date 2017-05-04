
#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    May 04, 2017 03:16:44 PM
import sys


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import MoM
    MoM.vp_start_gui()

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import MoM_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = main_window (root)
    MoM_support.init(root, top)
    root.mainloop()

w = None
def create_main_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = main_window (w)
    MoM_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_main_window():
    global w
    w.destroy()
    w = None


class main_window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1096x846+453+81")
        top.title("main_window")
        top.configure(background="#d9d9d9")



        self.save_button = Button(top)
        self.save_button.place(relx=0.32, rely=0.02, height=24, width=35)
        self.save_button.configure(activebackground="#d9d9d9")
        self.save_button.configure(activeforeground="#000000")
        self.save_button.configure(background="#d9d9d9")
        self.save_button.configure(disabledforeground="#a3a3a3")
        self.save_button.configure(foreground="#000000")
        self.save_button.configure(highlightbackground="#d9d9d9")
        self.save_button.configure(highlightcolor="black")
        self.save_button.configure(pady="0")
        self.save_button.configure(text='''Save''')

        self.attendees = Entry(top)
        self.attendees.place(relx=0.13, rely=0.02, relheight=0.02, relwidth=0.15)

        self.attendees.configure(background="white")
        self.attendees.configure(disabledforeground="#a3a3a3")
        self.attendees.configure(font="TkFixedFont")
        self.attendees.configure(foreground="#000000")
        self.attendees.configure(insertbackground="black")

        self.attendees_labe = Label(top)
        self.attendees_labe.place(relx=0.02, rely=0.02, height=21, width=62)
        self.attendees_labe.configure(background="#d9d9d9")
        self.attendees_labe.configure(disabledforeground="#a3a3a3")
        self.attendees_labe.configure(foreground="#000000")
        self.attendees_labe.configure(text='''Attendees:''')

        self.location_label = Label(top)
        self.location_label.place(relx=0.02, rely=0.06, height=21, width=68)
        self.location_label.configure(background="#d9d9d9")
        self.location_label.configure(disabledforeground="#a3a3a3")
        self.location_label.configure(foreground="#000000")
        self.location_label.configure(justify=RIGHT)
        self.location_label.configure(text='''Location:''')
        self.location_label.configure(width=68)

        self.location = Entry(top)
        self.location.place(relx=0.13, rely=0.06, relheight=0.02, relwidth=0.15)
        self.location.configure(background="white")
        self.location.configure(cursor="xterm")
        self.location.configure(disabledforeground="#a3a3a3")
        self.location.configure(font="TkFixedFont")
        self.location.configure(foreground="#000000")
        self.location.configure(insertbackground="black")

        self.Label3 = Label(top)
        self.Label3.place(relx=0.02, rely=0.11, height=21, width=108)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Background/Topic:''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.where_to_save_label = Label(top)
        self.where_to_save_label.place(relx=0.61, rely=0.01, height=21, width=83)

        self.where_to_save_label.configure(background="#d9d9d9")
        self.where_to_save_label.configure(disabledforeground="#a3a3a3")
        self.where_to_save_label.configure(foreground="#000000")
        self.where_to_save_label.configure(text='''Where to save:''')

        self.where_to_save = ttk.Combobox(top)
        self.where_to_save.place(relx=0.69, rely=0.01, relheight=0.02
                , relwidth=0.13)
        self.where_to_save.configure(takefocus="")

        self.background = Text(top)
        self.background.place(relx=0.13, rely=0.11, relheight=0.12, relwidth=0.4)

        self.background.configure(background="white")
        self.background.configure(cursor="xterm")
        self.background.configure(font="TkTextFont")
        self.background.configure(foreground="black")
        self.background.configure(highlightbackground="#d9d9d9")
        self.background.configure(highlightcolor="black")
        self.background.configure(insertbackground="black")
        self.background.configure(selectbackground="#c4c4c4")
        self.background.configure(selectforeground="black")
        self.background.configure(width=434)
        self.background.configure(wrap=WORD)

        self.Issue_label = Label(top)
        self.Issue_label.place(relx=0.02, rely=0.3, height=21, width=35)
        self.Issue_label.configure(background="#d9d9d9")
        self.Issue_label.configure(disabledforeground="#a3a3a3")
        self.Issue_label.configure(foreground="#000000")
        self.Issue_label.configure(text='''Issue:''')

        self.Issue_text_1 = Text(top)
        self.Issue_text_1.place(relx=0.03, rely=0.33, relheight=0.08
                , relwidth=0.3)
        self.Issue_text_1.configure(background="white")
        self.Issue_text_1.configure(font="TkTextFont")
        self.Issue_text_1.configure(foreground="black")
        self.Issue_text_1.configure(highlightbackground="#d9d9d9")
        self.Issue_text_1.configure(highlightcolor="black")
        self.Issue_text_1.configure(insertbackground="black")
        self.Issue_text_1.configure(selectbackground="#c4c4c4")
        self.Issue_text_1.configure(selectforeground="black")
        self.Issue_text_1.configure(width=324)
        self.Issue_text_1.configure(wrap=WORD)

        self.decision_label = Label(top)
        self.decision_label.place(relx=0.33, rely=0.3, height=21, width=54)
        self.decision_label.configure(background="#d9d9d9")
        self.decision_label.configure(disabledforeground="#a3a3a3")
        self.decision_label.configure(foreground="#000000")
        self.decision_label.configure(text='''Decision:''')

        self.decision_text_1 = Text(top)
        self.decision_text_1.place(relx=0.35, rely=0.33, relheight=0.08
                , relwidth=0.29)
        self.decision_text_1.configure(background="white")
        self.decision_text_1.configure(font="TkTextFont")
        self.decision_text_1.configure(foreground="black")
        self.decision_text_1.configure(highlightbackground="#d9d9d9")
        self.decision_text_1.configure(highlightcolor="black")
        self.decision_text_1.configure(insertbackground="black")
        self.decision_text_1.configure(selectbackground="#c4c4c4")
        self.decision_text_1.configure(selectforeground="black")
        self.decision_text_1.configure(width=314)
        self.decision_text_1.configure(wrap=WORD)

        self.TSizegrip1 = ttk.Sizegrip(top)
        self.TSizegrip1.place(anchor=SE, relx=1.0, rely=1.0)

        self.Assignee_label = Label(top)
        self.Assignee_label.place(relx=0.64, rely=0.3, height=21, width=56)
        self.Assignee_label.configure(background="#d9d9d9")
        self.Assignee_label.configure(disabledforeground="#a3a3a3")
        self.Assignee_label.configure(foreground="#000000")
        self.Assignee_label.configure(text='''Assignee:''')

        self.Text4 = Text(top)
        self.Text4.place(relx=0.66, rely=0.33, relheight=0.03, relwidth=0.14)
        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(foreground="black")
        self.Text4.configure(highlightbackground="#d9d9d9")
        self.Text4.configure(highlightcolor="black")
        self.Text4.configure(insertbackground="black")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(selectforeground="black")
        self.Text4.configure(width=154)
        self.Text4.configure(wrap=WORD)

        self.due_date_label = Label(top)
        self.due_date_label.place(relx=0.83, rely=0.3, height=21, width=57)
        self.due_date_label.configure(background="#d9d9d9")
        self.due_date_label.configure(disabledforeground="#a3a3a3")
        self.due_date_label.configure(foreground="#000000")
        self.due_date_label.configure(text='''Due Date:''')

        self.Text5 = Text(top)
        self.Text5.place(relx=0.83, rely=0.33, relheight=0.03, relwidth=0.12)
        self.Text5.configure(background="white")
        self.Text5.configure(font="TkTextFont")
        self.Text5.configure(foreground="black")
        self.Text5.configure(highlightbackground="#d9d9d9")
        self.Text5.configure(highlightcolor="black")
        self.Text5.configure(insertbackground="black")
        self.Text5.configure(selectbackground="#c4c4c4")
        self.Text5.configure(selectforeground="black")
        self.Text5.configure(width=134)
        self.Text5.configure(wrap=WORD)

        self.Issue_text_2 = Text(top)
        self.Issue_text_2.place(relx=0.03, rely=0.46, relheight=0.08
                , relwidth=0.3)
        self.Issue_text_2.configure(background="white")
        self.Issue_text_2.configure(font="TkTextFont")
        self.Issue_text_2.configure(foreground="black")
        self.Issue_text_2.configure(highlightbackground="#d9d9d9")
        self.Issue_text_2.configure(highlightcolor="black")
        self.Issue_text_2.configure(insertbackground="black")
        self.Issue_text_2.configure(selectbackground="#c4c4c4")
        self.Issue_text_2.configure(selectforeground="black")
        self.Issue_text_2.configure(width=324)
        self.Issue_text_2.configure(wrap=WORD)

        self.decision_text_2 = Text(top)
        self.decision_text_2.place(relx=0.35, rely=0.46, relheight=0.08
                , relwidth=0.29)
        self.decision_text_2.configure(background="white")
        self.decision_text_2.configure(font="TkTextFont")
        self.decision_text_2.configure(foreground="black")
        self.decision_text_2.configure(highlightbackground="#d9d9d9")
        self.decision_text_2.configure(highlightcolor="black")
        self.decision_text_2.configure(insertbackground="black")
        self.decision_text_2.configure(selectbackground="#c4c4c4")
        self.decision_text_2.configure(selectforeground="black")
        self.decision_text_2.configure(width=314)
        self.decision_text_2.configure(wrap=WORD)

        self.Text6 = Text(top)
        self.Text6.place(relx=0.66, rely=0.46, relheight=0.03, relwidth=0.14)
        self.Text6.configure(background="white")
        self.Text6.configure(font="TkTextFont")
        self.Text6.configure(foreground="black")
        self.Text6.configure(highlightbackground="#d9d9d9")
        self.Text6.configure(highlightcolor="black")
        self.Text6.configure(insertbackground="black")
        self.Text6.configure(selectbackground="#c4c4c4")
        self.Text6.configure(selectforeground="black")
        self.Text6.configure(width=154)
        self.Text6.configure(wrap=WORD)

        self.Text7 = Text(top)
        self.Text7.place(relx=0.83, rely=0.46, relheight=0.03, relwidth=0.12)
        self.Text7.configure(background="white")
        self.Text7.configure(font="TkTextFont")
        self.Text7.configure(foreground="black")
        self.Text7.configure(highlightbackground="#d9d9d9")
        self.Text7.configure(highlightcolor="black")
        self.Text7.configure(insertbackground="black")
        self.Text7.configure(selectbackground="#c4c4c4")
        self.Text7.configure(selectforeground="black")
        self.Text7.configure(width=134)
        self.Text7.configure(wrap=WORD)

        self.Issue_text_3 = Text(top)
        self.Issue_text_3.place(relx=0.03, rely=0.59, relheight=0.08
                , relwidth=0.3)
        self.Issue_text_3.configure(background="white")
        self.Issue_text_3.configure(font="TkTextFont")
        self.Issue_text_3.configure(foreground="black")
        self.Issue_text_3.configure(highlightbackground="#d9d9d9")
        self.Issue_text_3.configure(highlightcolor="black")
        self.Issue_text_3.configure(insertbackground="black")
        self.Issue_text_3.configure(selectbackground="#c4c4c4")
        self.Issue_text_3.configure(selectforeground="black")
        self.Issue_text_3.configure(width=324)
        self.Issue_text_3.configure(wrap=WORD)

        self.decision_text_3 = Text(top)
        self.decision_text_3.place(relx=0.35, rely=0.59, relheight=0.08
                , relwidth=0.29)
        self.decision_text_3.configure(background="white")
        self.decision_text_3.configure(font="TkTextFont")
        self.decision_text_3.configure(foreground="black")
        self.decision_text_3.configure(highlightbackground="#d9d9d9")
        self.decision_text_3.configure(highlightcolor="black")
        self.decision_text_3.configure(insertbackground="black")
        self.decision_text_3.configure(selectbackground="#c4c4c4")
        self.decision_text_3.configure(selectforeground="black")
        self.decision_text_3.configure(width=314)
        self.decision_text_3.configure(wrap=WORD)

        self.Text8 = Text(top)
        self.Text8.place(relx=0.66, rely=0.59, relheight=0.03, relwidth=0.14)
        self.Text8.configure(background="white")
        self.Text8.configure(font="TkTextFont")
        self.Text8.configure(foreground="black")
        self.Text8.configure(highlightbackground="#d9d9d9")
        self.Text8.configure(highlightcolor="black")
        self.Text8.configure(insertbackground="black")
        self.Text8.configure(selectbackground="#c4c4c4")
        self.Text8.configure(selectforeground="black")
        self.Text8.configure(width=154)
        self.Text8.configure(wrap=WORD)

        self.Text9 = Text(top)
        self.Text9.place(relx=0.83, rely=0.59, relheight=0.03, relwidth=0.12)
        self.Text9.configure(background="white")
        self.Text9.configure(font="TkTextFont")
        self.Text9.configure(foreground="black")
        self.Text9.configure(highlightbackground="#d9d9d9")
        self.Text9.configure(highlightcolor="black")
        self.Text9.configure(insertbackground="black")
        self.Text9.configure(selectbackground="#c4c4c4")
        self.Text9.configure(selectforeground="black")
        self.Text9.configure(width=134)
        self.Text9.configure(wrap=WORD)

        self.Issue_text_4 = Text(top)
        self.Issue_text_4.place(relx=0.03, rely=0.71, relheight=0.08
                , relwidth=0.3)
        self.Issue_text_4.configure(background="white")
        self.Issue_text_4.configure(font="TkTextFont")
        self.Issue_text_4.configure(foreground="black")
        self.Issue_text_4.configure(highlightbackground="#d9d9d9")
        self.Issue_text_4.configure(highlightcolor="black")
        self.Issue_text_4.configure(insertbackground="black")
        self.Issue_text_4.configure(selectbackground="#c4c4c4")
        self.Issue_text_4.configure(selectforeground="black")
        self.Issue_text_4.configure(width=324)
        self.Issue_text_4.configure(wrap=WORD)

        self.decision_text_4 = Text(top)
        self.decision_text_4.place(relx=0.35, rely=0.71, relheight=0.08
                , relwidth=0.29)
        self.decision_text_4.configure(background="white")
        self.decision_text_4.configure(font="TkTextFont")
        self.decision_text_4.configure(foreground="black")
        self.decision_text_4.configure(highlightbackground="#d9d9d9")
        self.decision_text_4.configure(highlightcolor="black")
        self.decision_text_4.configure(insertbackground="black")
        self.decision_text_4.configure(selectbackground="#c4c4c4")
        self.decision_text_4.configure(selectforeground="black")
        self.decision_text_4.configure(width=314)
        self.decision_text_4.configure(wrap=WORD)

        self.Text10 = Text(top)
        self.Text10.place(relx=0.66, rely=0.71, relheight=0.03, relwidth=0.14)
        self.Text10.configure(background="white")
        self.Text10.configure(font="TkTextFont")
        self.Text10.configure(foreground="black")
        self.Text10.configure(highlightbackground="#d9d9d9")
        self.Text10.configure(highlightcolor="black")
        self.Text10.configure(insertbackground="black")
        self.Text10.configure(selectbackground="#c4c4c4")
        self.Text10.configure(selectforeground="black")
        self.Text10.configure(width=154)
        self.Text10.configure(wrap=WORD)

        self.Text11 = Text(top)
        self.Text11.place(relx=0.83, rely=0.71, relheight=0.03, relwidth=0.12)
        self.Text11.configure(background="white")
        self.Text11.configure(font="TkTextFont")
        self.Text11.configure(foreground="black")
        self.Text11.configure(highlightbackground="#d9d9d9")
        self.Text11.configure(highlightcolor="black")
        self.Text11.configure(insertbackground="black")
        self.Text11.configure(selectbackground="#c4c4c4")
        self.Text11.configure(selectforeground="black")
        self.Text11.configure(width=134)
        self.Text11.configure(wrap=WORD)

        self.Issue_text_5 = Text(top)
        self.Issue_text_5.place(relx=0.03, rely=0.83, relheight=0.08
                , relwidth=0.3)
        self.Issue_text_5.configure(background="white")
        self.Issue_text_5.configure(font="TkTextFont")
        self.Issue_text_5.configure(foreground="black")
        self.Issue_text_5.configure(highlightbackground="#d9d9d9")
        self.Issue_text_5.configure(highlightcolor="black")
        self.Issue_text_5.configure(insertbackground="black")
        self.Issue_text_5.configure(selectbackground="#c4c4c4")
        self.Issue_text_5.configure(selectforeground="black")
        self.Issue_text_5.configure(width=324)
        self.Issue_text_5.configure(wrap=WORD)

        self.decision_text_5 = Text(top)
        self.decision_text_5.place(relx=0.35, rely=0.83, relheight=0.08
                , relwidth=0.29)
        self.decision_text_5.configure(background="white")
        self.decision_text_5.configure(font="TkTextFont")
        self.decision_text_5.configure(foreground="black")
        self.decision_text_5.configure(highlightbackground="#d9d9d9")
        self.decision_text_5.configure(highlightcolor="black")
        self.decision_text_5.configure(insertbackground="black")
        self.decision_text_5.configure(selectbackground="#c4c4c4")
        self.decision_text_5.configure(selectforeground="black")
        self.decision_text_5.configure(width=314)
        self.decision_text_5.configure(wrap=WORD)

        self.Text12 = Text(top)
        self.Text12.place(relx=0.66, rely=0.83, relheight=0.03, relwidth=0.14)
        self.Text12.configure(background="white")
        self.Text12.configure(font="TkTextFont")
        self.Text12.configure(foreground="black")
        self.Text12.configure(highlightbackground="#d9d9d9")
        self.Text12.configure(highlightcolor="black")
        self.Text12.configure(insertbackground="black")
        self.Text12.configure(selectbackground="#c4c4c4")
        self.Text12.configure(selectforeground="black")
        self.Text12.configure(width=154)
        self.Text12.configure(wrap=WORD)

        self.Text13 = Text(top)
        self.Text13.place(relx=0.83, rely=0.83, relheight=0.03, relwidth=0.12)
        self.Text13.configure(background="white")
        self.Text13.configure(font="TkTextFont")
        self.Text13.configure(foreground="black")
        self.Text13.configure(highlightbackground="#d9d9d9")
        self.Text13.configure(highlightcolor="black")
        self.Text13.configure(insertbackground="black")
        self.Text13.configure(selectbackground="#c4c4c4")
        self.Text13.configure(selectforeground="black")
        self.Text13.configure(width=134)
        self.Text13.configure(wrap=WORD)


