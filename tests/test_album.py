import random
import unittest

from faker import Faker

from src.logic.colection import Colection
from src.model.album import Album, Format
from src.model.declarative_base import Session


class AlbumTestCase(unittest.TestCase):
    def setUp(self):
        # Create a colection to work work with
        self.colection = Colection()

        # Start a session
        self.session = Session()

        # Create a faker instance
        self.faker = Faker()

        # The
        Faker.seed(1000)

        # Generate random data and use it to create albums
        self.data = []
        self.albums = []
        self.formats = [Format.CASSETTE, Format.CD, Format.DISC]

        for _ in range(0, 10):
            self.data.append(
                (
                    self.faker.unique.name(),
                    self.faker.random_int(1800, 2025),
                    self.faker.text(),
                    random.choice(self.formats),
                )
            )
            self.albums.append(
                Album(
                    title=self.data[-1][0],
                    year=self.data[-1][1],
                    description=self.data[-1][2],
                    format=self.data[-1][3],
                    songs=[],
                )
            )
            self.session.add(self.albums[-1])

        # Commit changes and close session
        self.session.commit()
        # ? Do not close the session, so the albums can be used in all tests
        # self.session.close()

    def tearDown(self):
        self.session = Session()

        albums = self.session.query(Album).all()

        for album in albums:
            self.session.delete(album)

        self.session.commit()
        self.session.close()

    def test_constructor(self):
        for album, data in zip(self.albums, self.data):
            self.assertEqual(album.title, data[0])
            self.assertEqual(album.year, str(data[1]))
            self.assertEqual(album.description, data[2])
            self.assertEqual(album.format, data[3])

    def test_add_album(self):
        """Should return True if the album is created successfully"""
        self.data.append(
            (
                self.faker.unique.name(),
                self.faker.random_int(1800, 2025),
                self.faker.text(),
                random.choice(self.formats),
            )
        )

        result = self.colection.add_album(
            title=self.data[-1][0],
            year=self.data[-1][1],
            description=self.data[-1][2],
            format=self.data[-1][3],
        )
        self.assertEqual(result, True)

    def test_add_album_exist(self):
        """Should return False if the album already exists"""
        result = self.colection.add_album(
            title=self.data[-1][0],
            year=self.data[-1][1],
            description=self.data[-1][2],
            format=self.data[-1][3],
        )
        self.assertNotEqual(result, True)

    def test_edit_album(self):
        """Should return True or False depending if the album name already exists"""
        self.data.append(
            (
                self.faker.unique.name(),
                self.faker.random_int(1800, 2025),
                self.faker.text(),
                random.choice(self.formats),
            )
        )

        # Change the name of the album with id 1 to another that does not exist
        result1 = self.colection.edit_album(
            album_id=1,
            title=self.data[-1][0],
            year=self.data[-1][1],
            description=self.data[-1][2],
            format=self.data[-1][3],
        )

        # Change the nane of the album with id 2 to another that already exist
        result2 = self.colection.edit_album(
            album_id=2,
            title=self.data[-3][0],
            year=self.data[-3][1],
            description=self.data[-3][2],
            format=self.data[-3][3],
        )

        self.assertTrue(result1)
        self.assertFalse(result2)

    def test_equal_albums(self):
        """Tests if two albums are the same reference to an object"""
        x_album = self.albums[0]
        db_album = self.colection.get_album_by_id(1)

        self.assertIs(x_album, self.albums[0])
        self.assertIsNot(db_album, self.albums[0])

    def test_album_in(self):
        """Tests if an element is in a list"""
        new_album = Album(
            title=self.faker.unique.name(),
            year=self.faker.random_int(1800, 2025),
            description=self.faker.text(),
            format=random.choice(self.formats),
            songs=[],
        )
        album_in_list = self.albums[2]

        self.assertIn(album_in_list, self.albums)
        self.assertNotIn(new_album, self.albums)

    def test_is_instance_of(self):
        """Tests if an object is an instance of given class"""
        self.assertIsInstance(self.albums[0], Album)
        self.assertNotIsInstance(self.colection, Album)

    def test_(self):
        """Tests that created data is actually saved in the database"""
        self.data.append(
            (
                self.faker.unique.name(),
                self.faker.random_int(1800, 2025),
                self.faker.text(),
                random.choice(self.formats),
            )
        )

        self.colection.add_album(
            title=self.data[-1][0],
            year=self.data[-1][1],
            description=self.data[-1][2],
            format=self.data[-1][3],
        )

        album = (
            self.session.query(Album)
            .filter(
                Album.title == self.data[-1][0] and Album.format == self.data[-1][3]
            )
            .first()
        )

        self.assertEqual(album.title, self.data[-1][0])
        self.assertEqual(album.year, str(self.data[-1][1]))
        self.assertEqual(album.description, self.data[-1][2])
        self.assertIn(album.format, self.formats)
