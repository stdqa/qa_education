from sqlalchemy import desc

from db import tables
from db.db import session

""" 
Some query example how we can work with sqlachemy, use some filters

"""
#result = session.query(tables.Movie.movie_id, tables.Movie.title, tables.Movie.rating
#                       ).filter(tables.Movie.movie_id >= 36, tables.Movie.movie_id <= 39).all()

#films_ids = session.query(tables.Movie.movie_id).filter(tables.Movie.movie_id > 40).subquery()

#result = session.query(tables.Movie.title).filter(tables.Movie.movie_id.in_(films_ids)).all()

films_ids = session.query(tables.Movie.movie_id).order_by(desc(tables.Movie.movie_id)).all()

print(films_ids)


"""
Example of object for training with pydantic schemas.
"""

player = {
    "account_status": "ACTIVE",
    "balance": 10,
    "localize": {
        "en": {"nickname": "MyNick", "countries": {"UK": 3}},
        "ru": {"nickname": "МойНик"}
    },
    "avatar": "https://google.com/images/cars/520/520"
}

computer = {
    "id": 21,
    "status": "ACTIVE",
    "started_at": "2013-06-01",
    "exparation_at": "2040-06-01",
    "host_v4": "91.192.222.17",
    "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "detailed_info": {
        "physical": {
            "color": "green",
            "photo": "https://images.unsplash.com/photo-1231424344",
            "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
        },
        "owners": [{
            "name": "Stephan Nollan",
            "card_number": "4000000000000002",
            "email": "shtephan.nollan@gmail.com",
        }]
    }
}
