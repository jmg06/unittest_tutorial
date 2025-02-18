from album import Album, Format
from declarative_base import Base, engine, session
from performer import Performer
from song import Song

Base.metadata.create_all(engine)

# Create performers
performer1 = Performer(
    name="Brenda Rowe", text_curiosities="Cupidatat labore aute sunt anim occaecat."
)
performer2 = Performer(
    name="Alisha Hahn",
    text_curiosities="Eiusmod non minim ullamco magna adipisicing velit et sit.",
)
performer3 = Performer(
    name="Dimitri Tremblay",
    text_curiosities="Eu enim anim reprehenderit laborum incididunt nulla non.",
)
performer4 = Performer(
    name="Justina Hintz",
    text_curiosities="Aliquip culpa laboris elit aute ad nostrud nostrud.",
)

session.add(performer1)
session.add(performer2)
session.add(performer3)
session.add(performer4)

# Create albums
album1 = Album(
    title="deserunt in perferendis",
    year=2021,
    description="Recusandae quas saepe voluptate expedita consequatur consequuntur aut officiis.",
    format=Format.CD,
)
album2 = Album(
    title="et autem ipsam",
    year=2021,
    description="Voluptatem perspiciatis et omnis.",
    format=Format.CASSETTE,
)

session.add(album1)
session.add(album2)

# Create songs
song1 = Song(
    title="enim est optio", minutes=4, seconds=20, songwriter="Berenice Dickinson"
)
song2 = Song(
    title="molestias iste quae",
    minutes=2,
    seconds=36,
    songwriter="Harmony Bashirian",
)
song3 = Song(title="vero dolores eum", minutes=5, seconds=30, songwriter="Unknown")

session.add(song1)
session.add(song2)
session.add(song3)

# Relationship album-song
album1.songs = [song1, song2]
album2.songs = [song1, song3]

# song1.albums = [album1, album2]
# song2.albums = [album1]
# song3.albums = [album2]

# Relationship song-performer
song1.performers = [performer1]
song2.performers = [performer2]
song3.performers = [performer3, performer4]

# Save changes
session.commit()
session.close()
