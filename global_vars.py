import sqlite3

BUTTON_FONT_STYLE = ("Arial", 18)
LABEL_FONT_STYLE = ("Arial", 14)
ENTRY_FONT_STYLE = ("Arial", 12)

populating_db = sqlite3.connect("data/test.db")

TITLES = []
ARTISTS = []
ALBUMS = []

cursor = populating_db.cursor()
get_titles = "SELECT title FROM MUSIC"
get_artists = "SELECT artist FROM MUSIC"
get_albums = "SELECT cdname FROM MUSIC"

cursor.execute(get_titles)
for row in cursor:
    if row[0].rstrip() not in TITLES:
        TITLES.append(row[0].rstrip())
TITLES.sort()

cursor.execute(get_artists)
for row in cursor:
    if row[0].rstrip() not in ARTISTS:
        ARTISTS.append(row[0].rstrip())
ARTISTS.sort()

cursor.execute(get_albums)
for row in cursor:
    if row[0].rstrip() not in ALBUMS:
        ALBUMS.append(row[0].rstrip())
ALBUMS.sort()

populating_db.close()

readme_text = """ """
readme_file = open("readme.txt")
readme_text = readme_file.read()
readme_file.close()

