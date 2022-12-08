import pymongo

import pymongo

def create_data(usage, description, bicycle_type, model, shop_name):
    import os
    # We declare a variable with the maximum waiting time for the server's response
    mongo_timeout = 5000
    # Environment variable containing a string with the connection URI to the cluster
    mongo_uri = os.environ['MONGO_URI']
    # This variable contains a string with the database we are going to use
    mongo_db = "proyecto_bicicletas"
    # This variable contains the collection we are going to use
    mongo_collection = "bicicletas"

    try:
        # We try to connect to the cluster and put the collection in a variable, if it works, we return the variable
        client = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=mongo_timeout)
        database = client[mongo_db]
        bicycles_collection = database[mongo_collection]
        # We create a new variable, which is a dictionary
        # where the values previously entered the tkinter fields will be placed.
        new_bicycle = {
            'usage': usage,
            'description': description,
            'bicycle type': bicycle_type,
            'model': model,
            'shop name': shop_name
        }
        # We put in the variable result the insertion of the bicycle
        # We print on the screen the id of the inserted document
        result = bicycles_collection.insert_one(new_bicycle)

        print('Object inserted ' + str(result.inserted_id))

    except pymongo.errors.ServerSelectionTimeoutError:
        print('Timeout')
    except pymongo.errors.ConnectionFailure:
        print('An error occurred while connecting')
    except pymongo.errors.InvalidURI:
        print('There is an error in the URI entered')
