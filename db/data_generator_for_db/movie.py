from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.db import Model

"""
    Describe  table movie for test database
"""

class Movie(Model):
    __tablename__  = 'movie'

    movie_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    rating = Column(Integer)
    genre_id = Column(Integer, ForeignKey('genre.genre_id'))
    genre = relationship("Genre", backref="movie")
    status = Column(String)

