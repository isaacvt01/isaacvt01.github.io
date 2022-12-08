import pprint

import pymongo

import pymongo
from bson import ObjectId


def update_data(_id, usage, model, description, shop_name, bicycle_brand):
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
        bike_to_update = {"_id": ObjectId(_id)}
        fields_update = {
            "$set":{"usage": usage,
                    "model": model,
                    "description": description,
                    "shop name": shop_name,
                    "bicycle brand": bicycle_brand
                    }
        }
        pprint.pprint(bicycles_collection.find_one(bike_to_update))
        result = bicycles_collection.update_one(bike_to_update, fields_update)
        print("Documents updated: " + str(result.modified_count))
        pprint.pprint(bicycles_collection.find_one(bike_to_update))
        client.close()

        return bicycles_collection
    except pymongo.errors.ServerSelectionTimeoutError:
        print('Tiempo de espera agotado')
    except pymongo.errors.ConnectionFailure:
        print('Fallo al conectarse')
    except pymongo.errors.InvalidURI:
        print('Hay un error en la URI')
