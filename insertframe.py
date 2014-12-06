from tkinter import *
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import sqlite3
from global_vars import *

class InsertFrame(Frame):
    def __init__(self, root, database):
        Frame.__init__(self, root)
        self.insert_frame = Frame(self, root)

        self.db = database
        self.cursor = self.db.cursor()

        ### track number
        self.track_label = Label(self.insert_frame, text = "Track number:", font = LABEL_FONT_STYLE)
        self.track_label.pack()
        self.track_entry_default = StringVar()
        self.track_entry_default.set("1")
        self.track_entry = Entry(self.insert_frame, textvariable  = self.track_entry_default, font = ENTRY_FONT_STYLE)
        self.track_entry.pack()
        ### title
        self.title = Label(self.insert_frame, text = "Song Title:", font = LABEL_FONT_STYLE)
        self.title.pack()
        self.title_entry_default = StringVar()
        self.title_entry_default.set("")
        self.title_combobox = ttk.Combobox(self.insert_frame, textvariable = self.title_entry_default, font = ENTRY_FONT_STYLE, values = TITLES, postcommand = self.adjust_title_dropdown)
        self.title_combobox.pack()
        ### artist
        self.artist = Label(self.insert_frame, text = "Artist:", font = LABEL_FONT_STYLE)
        self.artist.pack()
        self.artist_entry_default = StringVar()
        self.artist_entry_default.set("")
        self.artist_combobox = ttk.Combobox(self.insert_frame, textvariable = self.artist_entry_default, font = ENTRY_FONT_STYLE, values = ARTISTS, postcommand = self.adjust_artist_dropdown)
        self.artist_combobox.pack()

        ### album title
        self.album = Label(self.insert_frame, text = "Album/Video title:", font = LABEL_FONT_STYLE)
        self.album.pack()
        self.album_entry_default = StringVar()
        self.album_entry_default.set("")
        self.album_combobox = ttk.Combobox(self.insert_frame, textvariable = self.album_entry_default, font = ENTRY_FONT_STYLE, values = ALBUMS, postcommand = self.adjust_album_dropdown)
        self.album_combobox.pack()

        ### media type
        self.media = Label(self.insert_frame, text = "Media Type:", font = LABEL_FONT_STYLE)
        self.media.pack()
        self.media_menu_default = StringVar()
        self.media_menu_default.set("CD")
        media_options = ["CD", "Cassette", "DVD", "VHS"]
        self.media_menu_dropdown = OptionMenu(self.insert_frame, self.media_menu_default, *media_options)
        self.media_menu_dropdown.config(font = ENTRY_FONT_STYLE)
        media_menu = self.media_menu_dropdown.nametowidget(self.media_menu_dropdown['menu'])
        media_menu.config(font = ("Arial", 12))
        self.media_menu_dropdown.pack()

        ### year
        self.year = Label(self.insert_frame, text = "Year:", font = LABEL_FONT_STYLE)
        self.year.pack()
        self.year_default = StringVar()
        self.year_default.set("")
        self.year_entry = Entry(self.insert_frame, textvariable = self.year_default, font = ENTRY_FONT_STYLE)
        self.year_entry.pack()

        ### submit
        self.add_button = Button(self.insert_frame, text = "Add to database", command = self.insert_sql, font = LABEL_FONT_STYLE)
        self.add_button.pack(pady = 10)

        self.insert_frame.pack(fill = BOTH)
        
        
    def insert_sql(self, *args):
        """ pull from data entry fields, uppercase relevant data so things are uniform
        then add to database """
        try:
            self.db.execute("""INSERT INTO MUSIC(track, title, artist, cdname, media, year)
                        VALUES(:track, :title, :artist, :cdname, :media, :year)""",
                        {'track':self.track_entry_default.get() + "\t",  #add tabs to split on
                        'title':self.title_entry_default.get().upper() + "\t",
                        'artist':self.artist_entry_default.get().upper() + "\t",
                        'cdname':self.album_entry_default.get().upper() + "\t",
                        'media':self.media_menu_default.get() + "\t",
                        'year':self.year_default.get()}
                        )
            self.db.commit()
        except:
            tkmb.showerror("Duplicate entry", "This entry is probably already in the database.")
            
    def adjust_title_dropdown(self, *args):
        """ adjust the dropdown in the title combobox to suggest only items containing the 
        already entered text """
        curr_entry = self.title_entry_default.get().upper()
        new_values = []
        for title in TITLES:
            if curr_entry in title:
                new_values.append(title)
        self.title_combobox.config(values = new_values)
        
    def adjust_artist_dropdown(self, *args):
        """ adjust the dropdown in the title combobox to suggest only items containing the 
        already entered text """
        curr_entry = self.artist_entry_default.get().upper()
        new_values = []
        for artist in ARTISTS:
            if curr_entry in artist:
                new_values.append(artist)
        self.artist_combobox.config(values = new_values)
        
    def adjust_album_dropdown(self, *args):
        """ adjust the dropdown in the title combobox to suggest only items containing the 
        already entered text """
        curr_entry = self.album_entry_default.get().upper()
        new_values = []
        for album in ALBUMS:
            if curr_entry in album:
                new_values.append(album)
        self.album_combobox.config(values = new_values)