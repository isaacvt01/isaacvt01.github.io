from src.db.get_by_type.get_aero_type import get_aero_type
from src.db.get_by_type.get_sport_type import get_sport_type
from src.db.get_by_type.get_trail_type import get_trail_type
from src.db.get_by_type.get_triatlon_type import get_triatlon_type
from src.db.get_by_type.get_racing_type import  get_type_racing

def test_racing():
    for document in get_type_racing():
        assert document['bicycle type'] == 'Racing'

def test_triatlon():
    for document in get_triatlon_type():
        assert document['bicycle type'] == 'Triatlon'

def test_sport():
    for document in get_sport_type():
        assert document['bicycle type'] == 'Sport'

def test_trail():
    for document in get_trail_type():
        assert document['bicycle type'] == 'Trail'

def test_aero():
    for document in get_aero_type():
        assert document['bicycle type'] == 'Aero'


