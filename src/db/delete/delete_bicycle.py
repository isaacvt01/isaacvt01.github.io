import pymongo
from bson import ObjectId


def delete_data(_id):
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
        # Create a new variable, which contains a dictionary with key _id and the objecttid we specify in the Tkinter window
        bike_to_delete = {
            "_id": ObjectId(_id)
        }
        # We put in the result variable the action of deleting the document
        # then we print on the screen the number of objects that have been deleted.
        result = bicycles_collection.delete_one(bike_to_delete)

        print('Object deleted ' + str(result.deleted_count))
        return 'Deleted'

    except pymongo.errors.ServerSelectionTimeoutError:
        print('Timeout')
    except pymongo.errors.ConnectionFailure:
        print('An error occurred while connecting')
    except pymongo.errors.InvalidURI:
        print('There is an error in the URI entered')
