from src.db.query_bicycles import get_bicycle_data


def test_bicycles_list():
    assert isinstance (get_bicycle_data(), list)

def test_bicycles_dict():
    assert isinstance(get_bicycle_data()[0], dict)