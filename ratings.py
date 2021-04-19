import sqlite3


# START UP WORK
database_filename = "songs.db"
songs_table = "songs"
ratings_table = "ratings"

conn = sqlite3.connect("songs.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS 'songs' ('id', 'title', 'artist')")
cur.execute("CREATE TABLE IF NOT EXISTS 'ratings' ('id', 'rating')")
cur2 = conn.cursor()


def allSongs():
    return cur.execute("SELECT * FROM songs")


def ratingsForSong(id):
    listOfRatings = []
    for row in cur2.execute("SELECT * FROM ratings WHERE id=?", (id,)):
        listOfRatings.append(row[1])
    return listOfRatings


def insertSong(song):
    cur.execute('INSERT INTO songs VALUES (?,?,?)', (song['song_id'], song['title'], song['artist']))


def insertRating(rating):
    cur.execute('INSERT INTO ratings VALUES (?,?)', (rating['song_id'], rating['rating']))


def songIDAlreadyExists(id):
    for row in cur.execute("SELECT * FROM songs WHERE id=?", (id,)):
        return True
    return False


def get_songs():
    songDict = {}
    for row in allSongs():
        id = row[0]
        title = row[1]
        artist = row[2]
        rats = ratingsForSong(id)
        songDict[id] = {"id": id, "title": title, "artist": artist, "ratings": rats}
    return songDict


def songNotValid(song):
    return 'song_id' not in song or 'title' not in song or 'artist' not in song or len(song['song_id']) != 11 or song['title'] == "" or song['artist'] == ""


def ratingNotValid(rating):
    return 'song_id' not in rating or 'rating' not in rating or rating['rating'] not in [1, 2, 3, 4, 5]


def add_song(song):
    if songNotValid(song) or songIDAlreadyExists(song['song_id']):
        return
    insertSong(song)
    conn.commit()


def rate_song(rating):
    if ratingNotValid(rating) or not songIDAlreadyExists(rating['song_id']):
        return
    insertRating(rating)
    conn.commit()
