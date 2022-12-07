from src.layout.bicycles_layout import create_all_bicycles_layout, create_bicycles_layout
from src.layout.details_bicycles_layout import create_bicycle_details_layout
from src.layout.main_bicycles_layout import create_main_page_layout
from src.layout.brands_bicycle_layout import create_main_brand_page_layout, create_brands_layout, create_detail_brand_page_layout, create_bic_entry
from src.layout.types_bicycle_layout import create_detail_type_page_layout, create_main_type_page_layout, create_type_entry, create_type_bic_entry, trim_brand_name

def create_all_bicycles_page(bicycles):
    bicycles_html = ''

    for bic in bicycles:
        bicycles_html += create_all_bicycles_layout(bic)

    html = create_bicycles_layout(bicycles_html)

    with open("../presentation/bicycles.html", "w") as external_file:
        print(html, file=external_file)
        external_file.close()


def create_detail_pages(bicycles):
    for bic in bicycles:
        html = create_bicycle_details_layout(bic)

        file_name = bic['model'].replace(' ', '-') + bic["id"]
        with open(f"../presentation/details/{file_name}.html", "w") as external_file:
            print(html, file=external_file)
            external_file.close()


def create_main_page():
    html = create_main_page_layout()

    with open("../presentation/index.html", "w") as external_file:
        print(html, file=external_file)
        external_file.close()


def create_brand_pages(bicycles):
    brands = []
    # Generar lista de todos los brands que existen en la base de datos
    for bic in bicycles:
        brands.append(
            bic['brand']
        )
        # Que no se repitan los brands
    brands = list(dict.fromkeys(brands))
        # Llamamos a la funcion que nos va a crear la página
    create_main_brand_page(brands)

    brand_with_bycicles = {}

    for brand in brands:
        brand_with_bycicles[brand] = []

    for bic in bicycles:
        brand_with_bycicles[bic['brand']].append(bic)

    for brand in brands:
        create_brand_detail_page(brand, brand_with_bycicles[brand])


def create_brand_detail_page(brand, brand_bics):
    entries = ''
    for bic in brand_bics:
        entries += create_bic_entry(bic)

    html = create_detail_brand_page_layout(entries)

    with open("../presentation/details_brand/" + trim_brand_name(brand) + ".html", "w") as external_file:
        print(html, file=external_file)
        external_file.close()


# Creamos la página para los brands
def create_main_brand_page(brands):
    # Creamos un string vacio
    brand_html = ''
    # Metemos cada brand dentro del string y cada uno de ellos dentro de la funcion create_all_brands_layout
    for bic in brands:
        brand_html += create_brands_layout(bic)
    html = create_main_brand_page_layout(brand_html)
    with open("../presentation/brands_main.html", "w") as external_file:
        print(html, file=external_file)
        external_file.close()


def create_type_main_page(bicycles):
    bicycle_types = []
    for bic in bicycles:
        bicycle_types.append(
            bic['type']
        )
    bicycle_types = list(dict.fromkeys(bicycle_types))

    create_types_bicycle_layout(bicycle_types)

    types_with_bycicles = {}

    for type in bicycle_types:
        types_with_bycicles[type] = []

    for bic in bicycles:
        types_with_bycicles[bic['type']].append(bic)

    for type in bicycle_types:
        create_type_detail_page(type, types_with_bycicles[type])


def create_types_bicycle_layout(types):
    types_html = ''
    # Metemos cada brand dentro del string y cada uno de ellos dentro de la funcion create_all_brands_layout
    for type in types:
        types_html += create_type_entry(type)
    html = create_main_type_page_layout(types_html)
    with open("../presentation/types_main.html", "w") as external_file:
        print(html, file=external_file)
        external_file.close()


def create_type_detail_page(type, type_bics):
    entries = ''
    for bic in type_bics:
        entries += create_type_bic_entry(bic)

    html = create_detail_type_page_layout(entries)

    with open("../presentation/details_type/" + trim_brand_name(type) + ".html", "w") as external_file:
        print(html, file=external_file)
        external_file.close()


