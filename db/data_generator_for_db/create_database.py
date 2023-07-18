from faker import Faker
import random

from db.db import create_db, Session
from movie import Movie
from genre import Genre
from src.enums.user_enums import Statuses


"""
 Create database with test data , table movie and genre

"""

def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session: Session):
    fake = Faker()
    genres = ['Action', 'Comedy', 'Drama', 'Thriller', 'Horror']
    status_choices = [status.value for status in Statuses]

    genre_ids = {}

    for genre_name in genres:
        genre = Genre(genre_name=genre_name)
        session.add(genre)
        session.commit()
        genre_ids[genre_name] = genre.genre_id

    for _ in range(50):
        genre_name = random.choice(genres)
        genre_id = genre_ids[genre_name]

        movie = Movie(
            title=fake.text(max_nb_chars=30),
            description=fake.text(),
            rating=random.randint(1, 10),
            genre_id=genre_id,
            status=random.choice(status_choices)
        )
        session.add(movie)

    session.commit()

    session.close()

