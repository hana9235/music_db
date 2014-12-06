from tkinter import *
import tkinter.ttk as ttk
from tkinter.scrolledtext import *
from global_vars import *



class HelpFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.help_frame = Frame(self, root)

        self.text_field = ScrolledText(self.help_frame, width = 100, height = 40)
        self.text_field.pack()
        
        self.text_field.insert(END, readme_text)
        self.text_field.config(font = ENTRY_FONT_STYLE, wrap = WORD)
        self.help_frame.pack()