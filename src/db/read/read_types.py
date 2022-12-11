from src.db.connection.get_collection_bicycles import get_collection_bicycles


def get_type(type):
    #  Cogemos la conexion a las bicis
    bicycles_collection = get_collection_bicycles()
    # Creamos la query para sacar el tipo aero
    query_result = bicycles_collection.find({"bicycle type": type})

    data = []
    for document in query_result:
        #  Creamos el tipo de archivo que queremos que nos saque para el link a la página de detalles
        file_name = document['model'].replace(' ', '-') + str(document['_id'])
        #  Añadimos los datos que vamos a queres sacar de la coleccion bicicletas
        data.append(
            {
                "id": str(document['_id']),
                "model": document['model'],
                "brand": document['bicycle brand'],
                "image": "/assets/images/bicicleta.webp",
                "details_link": "details/" + file_name + ".html",
                "description": document["description"],
                "specifications": document["specifications"],
                "bicycle type": document["bicycle type"]
            }
        )

    return data
