from src.db.query_shops import get_shops_data


def test_tiendas_lista():
    assert isinstance (get_shops_data(), list)

def test_tiendas_dict():
    assert isinstance(get_shops_data()[0], dict)
