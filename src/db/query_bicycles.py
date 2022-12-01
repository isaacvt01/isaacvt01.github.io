from src.db.get_bicycles import get_bicycles
# En esta función sacamos los datos de la colección y los metemos en una lista
def get_bicycles_data():
    # Llamamos a la función que conecta y saca los datos de la colección bicicletas
    collection_bicycles = get_bicycles()
    # Creamos una lista para ir metiendo los diccionarios
    bicycles_data = []
    # Hacemos un bucle en el que creamos la página de detalles y un diccionario con los diferentes campos
    for document in collection_bicycles.find():
        file_name = document['model'].replace(' ', '-') + str(document['_id'])

        bicycles_data.append(
            {
                "id": str(document['_id']),
                "model": document['model'],
                "bicycle brand": document['bicycle brand'],
                "image": "/assets/images/bicicleta.webp",
                "details_link": "details/" + file_name + ".html",
                "description": document["description"],
                "specifications": document["specifications"]
            }
        )

    return bicycles_data