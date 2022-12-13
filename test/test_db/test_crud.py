from src.db.create.create_bicycle import create_data
from src.db.delete.delete_bicycle import delete_data
from src.db.connection.get_collection_bicycles import get_collection_bicycles


def test_delete():
    id = create_data('Usagetest', 'descriptiontest', 'bicycletest', 'modeltest', 'shopname')
    assert delete_data(id) == 'Deleted'


def test_read_noexisting():
    bikes_collections = get_collection_bicycles()
    bad_search = {'bicycle type': 'Fire'}
    find = bikes_collections.find_one(bad_search)
    assert find is None



def test_search():
    bikes_collections = get_collection_bicycles()
    good_search = {'bicycle type': 'Sport'}
    find_bike = bikes_collections.find_one(good_search)
    assert find_bike is not None
