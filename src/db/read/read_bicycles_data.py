import pymongo


def read_bicycles_data(table):
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
        # Create a for loop that puts all the documents into the table
        for bic in bicycles_collection.find():
            table.insert('', 0, text=bic['_id'],
                         values=(bic['model'], bic['usage'], bic['bicycle type'], bic['bicycle brand']))

    except pymongo.errors.ServerSelectionTimeoutError:
        print('Timeout')
    except pymongo.errors.ConnectionFailure:
        print('An error occurred while connecting')
    except pymongo.errors.InvalidURI:
        print('There is an error in the URI entered')
