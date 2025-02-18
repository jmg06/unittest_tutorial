from sqlalchemy import Column, ForeignKey, Integer, String

from .declarative_base import Base


class Performer(Base):
    __tablename__ = "performer"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    text_curiosities = Column(String)
    song = Column(Integer, ForeignKey("song.id"))
