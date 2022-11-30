
from src.db.type_handler.get_type import get_type

def test_racing():
    for document in get_type('Racing'):
        assert document['bicycle type'] == 'Racing'

def test_sport():
    for document in get_type('Sport'):
        assert document['bicycle type'] == 'Sport'

def test_aero():
    for document in get_type('Aero'):
        assert document['bicycle type'] == 'Aero'

def test_triatlon():
    for document in get_type('Triatlon'):
        assert document['bicycle type'] == 'Triatlon'

def test_triatlon():
    for document in get_type('Trail'):
        assert document['bicycle type'] == 'Trail'


