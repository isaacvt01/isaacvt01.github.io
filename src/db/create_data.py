import pymongo

import pymongo

def create_data(usage, description, bicycle_type, model, shop_name):
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
        new_bicycle = {
            'usage': usage,
            'description': description,
            'bicycle type': bicycle_type,
            'model': model,
            'shop name': shop_name
        }
        result = bicycles_collection.insert_one(new_bicycle)

        print('Object inserted ' + str(result.inserted_id))

        return bicycles_collection
    except pymongo.errors.ServerSelectionTimeoutError:
        print('Tiempo de espera agotado')
    except pymongo.errors.ConnectionFailure:
        print('Fallo al conectarse')
    except pymongo.errors.InvalidURI:
        print('Hay un error en la URI')
