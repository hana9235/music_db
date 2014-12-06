from tkinter import *
import sqlite3
from insertframe import *
from queryframe import *
from global_vars import *

db = sqlite3.connect("data/test.db")

class Page(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

    def show(self):
        self.lift()

class Gui_Main(Page):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.main_frame = Frame(root, self)
        self.main_frame.pack(fill = BOTH)
        self.content_frame = Frame(width = 500)

        self.button_frame = Frame(width = 100)

        self.insert_frame_button = Button(self.button_frame,
                                            text = "Add Items",
                                            command = self.show_insert,
                                            width = 10,
                                            height = 3,
                                            font = BUTTON_FONT_STYLE)
        self.insert_frame_button.pack(anchor = NW)
        self.query_frame_button = Button(self.button_frame,
                                            text = "Search",
                                            command = self.show_query,
                                            width = 10,
                                            height = 3,
                                            font = BUTTON_FONT_STYLE)
        self.query_frame_button.pack(anchor = NW, pady = 15)
        self.button_frame.pack(side = LEFT, fill = Y)


        ### insert frame
        self.insert_frame = InsertFrame(self.content_frame, db)
        self.insert_frame.pack() # shown by default
        
        ### query_frame - don't pack it so it won't show up at first
        self.query_frame = QueryFrame(self.content_frame, db)

        self.content_frame.pack()


    def show_insert(self):
        self.query_frame.pack_forget()
        self.insert_frame.pack(fill = BOTH)

    def show_query(self):
        self.insert_frame.pack_forget()
        self.query_frame.pack(fill = BOTH)



def main():
    root = Tk()
    root.title("Database Program")

    root.geometry("850x600")

    gui_content = Gui_Main(root)
    gui_content.pack()
    root.mainloop()


if __name__ == "__main__":
    main()


