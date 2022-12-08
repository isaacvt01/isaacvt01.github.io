from src.db.brand_handler.get_brand import get_brand


def test_cannondale():
    for document in get_brand('CANNONDALE'):
        assert document['brand'] == 'CANNONDALE'


def test_orbea():
    for document in get_brand('ORBEA'):
        assert document['brand'] == 'ORBEA'


def test_scott_foil():
    for document in get_brand('SCOTT FOIL'):
        assert document['brand'] == 'SCOTT FOIL'


def test_trek_domane():
    for document in get_brand('TREK DOMANE'):
        assert document['brand'] == 'TREK DOMANE'


def test_willier():
    for document in get_brand('WILIER GTR'):
        assert document['brand'] == 'WILIER GTR'


def test_mbc():
    for document in get_brand('BMC TIMEMACHINE'):
        assert document['brand'] == 'BMC TIMEMACHINE'
