import requests
import pytest
from src.generators.player_localization import PlayerLocalization


import db.tables as tables


@pytest.mark.parametrize("status", [
    'ACTIVE',
    'BANEED',
    'DELETED',
    'INACTIVE'
])
def test_status(status, get_player_generator):
    print(get_player_generator.build())


@pytest.mark.parametrize("balance_value", [
    '100',
    '0',
    '-10',
    'asdd'
])
def test_balance_value(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


@pytest.mark.parametrize("delete_key", [
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_delete_key(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize("localizations, local", [
    ('fr', 'fr_FR'),
    ('de', 'de_DE')
])
def test_inner_generator(get_player_generator, localizations, local):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(local).set_number(15).build()
    ).build()
    print(object_to_send)


@pytest.mark.db_tests
def test_get_data_movie(get_db_session):
    data = get_db_session.query(tables.Movie).first()
    print(data.movie_id)


@pytest.mark.db_tests
def test_try_to_delete_something(get_delete_method, get_db_session):
    get_delete_method(get_db_session, tables.Genre, (tables.Genre.genre_id == 9))


@pytest.mark.db_tests
def test_try_to_add_something(get_db_session, get_add_data_to_db, get_item_type_generator):
    item = tables.Genre(**get_item_type_generator.build())
    get_add_data_to_db(get_db_session, item)
    print(item.genre_name)


@pytest.mark.db_tests
def test_generate_genre_name(generate_genre_name):
    print(generate_genre_name.genre_name)


class Letter:

    def __init__(self, letter, position):
        self.letter = letter
        self.position = position

    def __str__(self):
        return f"Letter {self.letter}. Position {self.position}"


def get_cases():
    return [
        Letter('a', 1),
        Letter('b', 2)
    ]


@pytest.mark.production
@pytest.mark.parametrize('my_value', get_cases(), ids=str)
def test_my_magic_method(my_value):
    print(my_value)

