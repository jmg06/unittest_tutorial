from src.model.album import Album, Format
from src.model.declarative_base import Base, engine, session
from src.model.performer import Performer
from src.model.song import Song


class Colection:
    def __init__(self):
        Base.metadata.create_all(engine)

    def add_album(self, title, year, description, format):
        album_exist = session.query(Album).filter(Album.title == title).all()
        if len(album_exist) == 0:
            album = Album(
                title=title, year=year, description=description, format=format
            )
            session.add(album)
            session.commit()
            return True
        else:
            return False

    def get_formats(self):
        return [format.name for format in Format]

    def edit_album(self, album_id, title, year, description, format):
        album_exist = (
            session.query(Album)
            .filter(Album.title == title, Album.id != album_id)
            .all()
        )
        if len(album_exist) == 0:
            album = session.query(Album).filter(Album.id == album_id).first()
            album.title = title
            album.year = year
            album.description = description
            album.format = format
            session.commit()
            return True
        else:
            return False

    def delete_album(self, album_id):
        try:
            album = session.query(Album).filter(Album.id == album_id).first()
            session.delete(album)
            session.commit()
            return True
        except Exception:
            return False

    def get_album_by_id(self, album_id):
        return session.query(Album).get(album_id).__dict__
