from __future__ import print_function
import sqlite3
import os.path

data_folder = "data"
db_file = "test.db"
path = os.path.join(data_folder, db_file)

db = sqlite3.connect(path)

### DB SHOULD ONLY BE SET UP ONCE, THEN ALLOW HIM TO ADD THINGS AS HE WANTS
### MAKE SURE TO COMMIT AFTER EVERY SINGLE ADDITION
### TWO TABLES, ONE FOR CDS AND ONE FOR DVDS?

db.execute(""" CREATE TABLE IF NOT EXISTS MUSIC 
            (TRACK INT NOT NULL,
            TITLE VARCHAR(90) NOT NULL,
            ARTIST VARCHAR(45) NOT NULL,
            CDNAME VARCHAR(90) NOT NULL,
            MEDIA VARCHAR(12) NOT NULL,
            YEAR INT NOT NULL)""") # REMOVE NOT NULLS FOR THESE


"""
tracknum = int(raw_input("Enter the track number: "))
title = raw_input("Enter the song title: ")
artist = raw_input("Enter the artist: ")
cdname = raw_input("Enter the CD name: ")
year = int(raw_input("Enter the year the album was released: "))

#db.execute(''' INSERT INTO MUSIC(track, title, artist, cdname, year)
#                VALUES(:track, :title, :artist, :cd, :year)''',
#                {'track':tracknum, 
#                'title':title, 
#                'artist':artist,
#                'cd':cdname,
#                'year':year}
#                )

# once connected, do things like this:
# db.execute('''CREATE TABLE ... \
#               (ID INT PRIMARY KEY NOT NULL, 
#               NAME VARCHAR(20) NOT NULL)''')

db.commit()
"""
cursor = db.cursor()
cursor.execute("""SELECT * from MUSIC""")
for row in cursor:
    print(row[0], row[1], row[2], row[3], row[4], row[5])

cursor2 = db.cursor()
cursor2.execute('SELECT * FROM MUSIC WHERE TITLE = "{0}"'.format("poopy"))
print("\n\n")
print("cursor contains: ")
for row in cursor2:
    print(row)
db.commit()



#print("connected successfully")
db.close()

