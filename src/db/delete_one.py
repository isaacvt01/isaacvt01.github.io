import pymongo
from bson import ObjectId


def delete_data(_id):
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
        bike_to_delete = {
            "_id": ObjectId(_id)
        }
        result = bicycles_collection.delete_one(bike_to_delete)

        print('Object deleted ' + str(result.deleted_count))

        return bicycles_collection
    except pymongo.errors.ServerSelectionTimeoutError:
        print('Tiempo de espera agotado')
    except pymongo.errors.ConnectionFailure:
        print('Fallo al conectarse')
    except pymongo.errors.InvalidURI:
        print('Hay un error en la URI')
