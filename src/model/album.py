import enum

from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Format(enum.Enum):
    DISC = 1
    CASSETTE = 2
    CD = 3


class Album(Base):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(String)
    description = Column(String)
    format = Column(Enum(Format))
    songs = relationship("Song", secondary="album_song")
