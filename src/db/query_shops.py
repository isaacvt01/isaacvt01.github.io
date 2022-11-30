from src.db.get_shops import get_shops

def get_shops_data():

    #  Cogemos la conexion a las bicis
    bicycles_collection = get_shops()

    shops_data = []
    for document in bicycles_collection.find():

        #  Añadimos los datos que vamos a queres sacar de la colección tiendas
        shops_data.append(
            {
                "id": str(document['_id']),
                "nombre": document['nombre'],
                "ciudad": document['ciudad'],
                "isla": document["isla"]
            }
        )

    return shops_data
