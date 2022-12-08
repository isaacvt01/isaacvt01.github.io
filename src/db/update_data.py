import pprint
import pymongo
from bson import ObjectId


def update_data(_id, usage, model, description, shop_name, bicycle_brand):
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

    except pymongo.errors.ServerSelectionTimeoutError:
        print('Timeout')
    except pymongo.errors.ConnectionFailure:
        print('An error occurred while connecting')
    except pymongo.errors.InvalidURI:
        print('There is an error in the URI entered')

