from tkinter import *
import sqlite3
from global_vars import *

class QueryFrame(Frame):
    def __init__(self, root, database):
        Frame.__init__(self, root)
        self.query_frame = Frame(self, root)

        self.db = database
        self.cursor = self.db.cursor()

        self.query_header = Label(self.query_frame, text = "Search for items:", font = LABEL_FONT_STYLE)
        self.query_header.pack()

        # search by field select
        data_fields = ["Song Title", "Artist/Performer", "Album/Video Title", "Media Type"]
        self.search_type_default = StringVar()
        self.search_type_default.set(data_fields[0])
        self.search_type_default.trace("w", self.query_type_change)
        self.search_type_dropdown = OptionMenu(self.query_frame, self.search_type_default, *data_fields)
        self.search_type_dropdown.config(font = ("Arial", 12))
        type_menu = self.search_type_dropdown.nametowidget(self.search_type_dropdown['menu'])
        type_menu.config(font = ENTRY_FONT_STYLE)
        self.search_type_dropdown.pack()

        # entry label
        self.query_field_label_text = StringVar()
        self.query_field_label_text.set("Enter a Song Title to search for:") # default to first option in list
        self.query_field_label = Label(self.query_frame, textvariable = self.query_field_label_text, font = LABEL_FONT_STYLE)
        self.query_field_label.pack()

        # search box
        self.query_item = StringVar()
        self.query_item.trace("w", self.submit_query) # live update as search box is modified
        self.query_box = Entry(self.query_frame, textvariable = self.query_item, font = ENTRY_FONT_STYLE)
        self.query_box.pack(pady = 5)

        # result field and scrollbars
        self.y_scroll = Scrollbar(self.query_frame, orient = VERTICAL)
        self.x_scroll = Scrollbar(self.query_frame, orient = HORIZONTAL)
        self.result_field = Listbox(self.query_frame, width = 60, height = 15,
                                        yscrollcommand = self.y_scroll.set, xscrollcommand = self.x_scroll.set, font = ("Courier New", 14), borderwidth = 5, relief = GROOVE)
        self.y_scroll.pack(side = RIGHT, fill = Y, anchor = N)
        self.y_scroll.config(command = self.result_field.yview)
        self.x_scroll.config(command = self.result_field.xview)
        self.result_field.pack()
        self.x_scroll.pack(fill = X, pady = 5)

        # delete and view all buttons
        self.delete_button = Button(self.query_frame, text = "Delete Selected", command = self.delete, font = LABEL_FONT_STYLE)
        self.delete_button.pack(side = RIGHT, padx = 10)
        self.view_all_button = Button(self.query_frame, text = "View All", command = self.view, font = LABEL_FONT_STYLE)
        self.view_all_button.pack(side = LEFT)

        self.query_frame.pack()

    def submit_query(self, *args):
        """ pull query item and search type, submit to db """
        query_string = self.query_item.get().upper()
        query_type = self.get_query_type(self.search_type_default.get()) # change dropdown text to match db fields

        select_statement = """ SELECT * FROM MUSIC WHERE {0} LIKE '%{1}%' ORDER BY 'cdname' """.format(query_type, query_string)
        # Using the LIKE statement allows searching for substrings
        # allows input of "mer" to match "summer, mermaid, hammering"
        self.cursor.execute(select_statement)

        results = []
        for row in self.cursor:
            result_str = ""
            for i in row:
                result_str += str(i) + " "
            results.append(result_str)

        self.result_field.delete(0, END)
        for i in range(len(results)):
            self.result_field.insert(END, results[i])


    def delete(self, *args):
        """ pull selected items and delete them from the results field
        and from the database """

        selected_items = self.result_field.curselection() # tuple of indices
        rows_to_delete = []

        for i in range(len(selected_items)):
            # split each item into its separate fields
            rows_to_delete.append(self.result_field.get(selected_items[i]).split("\t"))

        for row in rows_to_delete: # can have multiple selected for deletion
            for field in range(len(row)): # each part of an entry
                row[field] = row[field].strip()  # pull off extra whitespace for db query

        #del_cursor = self.db.cursor()
        for row in rows_to_delete:
            self.cursor.execute("DELETE FROM MUSIC WHERE title LIKE ? AND artist LIKE ? AND cdname LIKE ?", (row[1] + '%', row[2] + '%', row[3] + '%'))
            self.db.commit()


        for index in selected_items: # update listbox to show deletion
            self.result_field.delete(index)


    def get_query_type(self, query_type_str):
        if query_type_str == "Song Title":
            query_type_str = "title"
        elif query_type_str == "Artist/Performer":
            query_type_str = "artist"
        elif query_type_str == "Album/Video Title":
            query_type_str = "cdname"
        else:
            query_type_str = "media"
        return query_type_str


    def view(self):
        self.query_item.set("")
        self.cursor.execute("""select * from MUSIC""")
        results = []
        for row in self.cursor:
            result_str = ""
            for i in row:
                result_str += str(i) + " "
            results.append(result_str)
        self.result_field.delete(0, END)
        for i in range(len(results)):
            self.result_field.insert(END, results[i])



    def query_type_change(self, *args):
        query_label = "Enter a {0} to search for:".format(self.search_type_default.get())
        self.query_field_label_text.set(query_label)

