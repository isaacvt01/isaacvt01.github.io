from src.db.read.read_bicycles import get_bicycles_data


def test_read_bicycles():
    bicycles = get_bicycles_data()

    assert isinstance(bicycles, list)
    assert len(bicycles) > 0
    assert isinstance(bicycles[0], dict)
    assert "id" in bicycles[0].keys()
