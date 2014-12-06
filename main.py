from __future__ import print_function
import sqlite3
import os.path


data_folder = "data"
db_file = "test.db"
path = os.path.join(data_folder, db_file)


db = sqlite3.connect(path)

def read_input_file(path):
    # | is the newline separator
    # commas separate values
    in_file = open(path)
    lines = in_file.read().splitlines()
    for line in range(len(lines)):
        lines[line] = lines[line].split(",")
        insert_into_db(lines[line])
    
    
def insert_into_db(row):
    cursor = db.cursor()
    cursor.execute("INSERT INTO MUSIC(track, title, artist, cdname, media, year) \
                        VALUES(:track, :title, :artist, :cdname, :media, :year)", 
                    {'track':row[0] + "\t",
                    'title':row[1].upper() + "\t",
                    'artist':row[2].upper() + "\t",
                    'cdname':row[3].upper() + "\t",
                    'media':row[4].upper() + "\t",
                    'year':row[5] }
                    )
    db.commit()


infile_path = os.path.join(data_folder, "testnobar.csv")
#read_input_file(infile_path) # uncomment to add the file again

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

