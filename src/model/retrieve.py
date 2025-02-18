from album import Album, Format
from declarative_base import session
from performer import Performer
from song import Song

songs = session.query(Song).all()

print("Stored songs:")
for song in songs:
    print(f"Song: {song.title}")
    print(f"Duration: 00:{song.minutes}:{song.seconds}")

    print("Performers")
    for performer in song.performers:
        print(f"- {performer.name}")

    print("Albums")
    for album in song.albums:
        print(f"- {album.title}")

    print("======================================")


print("\nAlbums in Cassette format:")
albums = session.query(Album).filter(Album.format == Format.CASSETTE).all()
for album in albums:
    print(f"- {album.title}")

session.close()
