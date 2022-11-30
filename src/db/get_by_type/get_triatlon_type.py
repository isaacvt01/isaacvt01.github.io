from src.db.get_bicycles import get_bicycles

def get_triatlon_type():

    #  Cogemos la conexion a las bicis
    bicycles_collection = get_bicycles()
    # Creamos la query para sacar el tipo triatlon
    query_result = bicycles_collection.find({"bicycle type":"Triatlon"})


    triatlon_data = []
    for document in query_result:
        #  Creamos el tipo de archivo que queremos que nos saque para el link a la página de detalles
        file_name = document['model'].replace(' ', '-') + str(document['_id'])
        #  Añadimos los datos que vamos a queres sacar de la coleccion bicicletas
        triatlon_data.append(
            {
                "id": str(document['_id']),
                "model": document['model'],
                "bicycle brand": document['bicycle brand'],
                "image": "/assets/images/bicicleta.webp",
                "details_link": "details/" + file_name + ".html",
                "description": document["description"],
                "specifications": document["specifications"],
                "bicycle type": document["bicycle type"]
            }
        )

    return triatlon_data

