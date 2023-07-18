from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.db import Model


"""
    Describe  table genre for test database
"""

class Genre(Model):
    __tablename__  = 'genre'

    genre_id = Column(Integer, primary_key=True)
    genre_name = Column(String)




