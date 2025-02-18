from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Song(Base):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    minutes = Column(Integer)
    seconds = Column(Integer)
    songwriter = Column(String)
    albums = relationship("Album", secondary="album_song")
    performers = relationship("Performer", cascade="all, delete, delete-orphan")


class AlbumSong(Base):
    __tablename__ = "album_song"

    album = Column(Integer, ForeignKey("album.id"), primary_key=True)
    song = Column(Integer, ForeignKey("song.id"), primary_key=True)
