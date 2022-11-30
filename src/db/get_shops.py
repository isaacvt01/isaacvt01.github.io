import pymongo

def get_shops():
    # Declaramos una variable con el tiempo de espera máximo para la respuesta del servidor
    mongo_timeout = 5000
    # Variable que contiene un string con la URI de conexión al cluster
    mongo_uri = 'mongodb+srv://manuortdaw17:fpsuperiordaw2022@cluster0.jmkzwwg.mongodb.net/test'
    # Esta variable contiene un string con la base de datos que vamos a utilizar
    mongo_db = "proyecto_bicicletas"
    # Esta variable contiene la colección que vamos a utilizar
    mongo_collection = "tiendas"

    try:
        # Intentamos conectarnos al cluster y meter la colección en una variable, si funciona, devolvemos la variable
        client = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=mongo_timeout)
        database = client[mongo_db]
        bicycles_collection = database[mongo_collection]

        return bicycles_collection
    except pymongo.errors.ServerSelectionTImeoutError:
        print('Tiempo de espera agotado')
    except pymongo.errors.ConnectionFailure:
        print('Fallo al conectarse')
    except pymongo.errors.InvalidURI:
        print('Hay un error en la URI')
