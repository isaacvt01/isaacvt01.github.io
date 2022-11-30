from src.db.query_bicycles import get_bicycles_data


def test_bicycles_list():
    assert isinstance (get_bicycles_data(), list)

def test_bicycles_dict():
    assert isinstance(get_bicycles_data()[0], dict)