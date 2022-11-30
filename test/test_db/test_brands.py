from src.db.get_by_brand.get_cannondale_brand import get_brand_cannondale
from src.db.get_by_brand.get_orbea_brand import get_brand_orbea
from src.db.get_by_brand.get_scott_foil_brand import get_brand_scott_foil
from src.db.get_by_brand.get_trek_domane_brand import get_brand_trek_domane
from src.db.get_by_brand.get_willier_gtr_brand import get_brand_willier_gtr
from src.db.get_by_brand.get_mbc_timemachine_brand import get_brand_mbc_timemachine

def test_cannondale():
    for document in get_brand_cannondale():
        assert document['bicycle brand'] == 'CANNONDALE'

def test_orbea():
    for document in get_brand_orbea():
        assert document['bicycle brand'] == 'ORBEA'

def test_scott_foil():
    for document in get_brand_scott_foil():
        assert document['bicycle brand'] == 'SCOTT FOIL'

def test_trek_domane():
    for document in get_brand_trek_domane():
        assert document['bicycle brand'] == 'TREK DOMANE'

def test_willier():
    for document in get_brand_willier_gtr():
        assert document['bicycle brand'] == 'WILIER GTR'

def test_mbc():
    for document in get_brand_mbc_timemachine():
        assert document ['bicycle brand'] == 'BMC TIMEMACHINE'