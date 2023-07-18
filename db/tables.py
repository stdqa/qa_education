from sqlalchemy import Column, Integer, String

from db.db import Model


class Movie(Model):
    """
    here we describe the base table and column we will be working with

    """
    __tablename__ = 'movie'

    movie_id = Column(Integer, primary_key=True)
    status = Column(String, index=True)
    title = Column(String)
    rating = Column(Integer)


class Genre(Model):
    __tablename__ = 'genre'

    genre_id = Column(Integer, primary_key=True)
    genre_name = Column(String)
