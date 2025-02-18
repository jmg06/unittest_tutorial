from album import Album
from declarative_base import session
from performer import Performer
from song import Song

song2 = session.query(Song).get(2)
performer4 = session.query(Performer).get(4)

song2.minutes = 1
song2.seconds = 55
song2.songwriter = "Evert Doyle"
song2.performers.append(performer4)

session.add(song2)

session.commit()
session.close()
