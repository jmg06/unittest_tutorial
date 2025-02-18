from album import Album
from declarative_base import session
from performer import Performer
from song import Song

song2 = session.query(Song).get(2)
session.delete(song2)
session.commit()
session.close()
