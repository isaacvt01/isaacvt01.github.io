from src.db.create.create_bicycle import create_data
from src.db.delete.delete_bicycle import delete_data
from src.db.connection.get_collection_bicycles import get_collection_bicycles


def test_delete():
    id = create_data('Usagetest', 'descriptiontest', 'bicycletest', 'modeltest', 'shopname')
    assert delete_data(id) == 'Deleted'


def test_read_noexisting():
    import pymongo

    import os
    # Declaramos una variable con el tiempo de espera máximo para la respuesta del servidor
    mongo_timeout = 5000
    # Variable de entorno que contiene un string con la URI de conexión al cluster
    mongo_uri = os.environ['MONGO_URI']
    # Esta variable contiene un string con la base de datos que vamos a utilizar
    mongo_db = "proyecto_bicicletas"
    # Esta variable contiene la colección que vamos a utilizar
    mongo_collection = "bicicletas"

    try:
        # Intentamos conectarnos al cluster y meter la colección en una variable, si funciona, devolvemos la variable
        client = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=mongo_timeout)
        database = client[mongo_db]
        bicycles_collection = database[mongo_collection]
        wrong_search = {'bicycle type': 'Fire'}
        bike = bicycles_collection.find_one(wrong_search)
        assert bike is None

    except pymongo.errors.ServerSelectionTimeoutError:
        print('Tiempo de espera agotado')
    except pymongo.errors.ConnectionFailure:
        print('Fallo al conectarse')
    except pymongo.errors.InvalidURI:
        print('Hay un error en la URI')


def test_search():
    bikes_collections = get_collection_bicycles()
    good_search = {'bicycle type': 'Sport'}
    find_bike = bikes_collections.find_one(good_search)
    assert find_bike is not None
