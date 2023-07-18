import pytest
import db.tables as tables
from src.generators.player import Player
from src.generators.item_type_generator import ItemsTypeBuilder

from db.db import Session


@pytest.fixture
def get_player_generator():
    print('here')
    return Player()


@pytest.fixture
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_data_from_db(session, table, filter_data):
    session.query(table).filter(filter_data).delete()
    session.commit()


def add_data_to_db(session, item):
    session.add(item)
    session.commit()


@pytest.fixture
def get_add_data_to_db():
    return add_data_to_db


@pytest.fixture
def get_delete_method():
    return delete_data_from_db


@pytest.fixture
def get_item_type_generator():
    return ItemsTypeBuilder()


@pytest.fixture
def generate_genre_name(get_db_session, get_item_type_generator, get_add_data_to_db, get_delete_method):
    item = tables.Genre(**get_item_type_generator.build())
    get_add_data_to_db(get_db_session, item)
    yield item
    get_delete_method(get_db_session, tables.Genre, (tables.Genre.genre_id == item.genre_id))
