from src.db.create.create_bicycle import create_data
from src.db.delete.delete_bicycle import delete_data

def test_crud():
    id = create_data('Usagetest', 'descriptiontest', 'bicycletest', 'modeltest', 'shopname')
    assert delete_data(id) == 'Deleted'
