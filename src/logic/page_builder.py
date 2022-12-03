from src.layout.bicycles_layout import create_all_bicycles_layout, create_bicycles_layout
from src.layout.details_bicycles_layout import create_bicycle_details_layout
from src.layout.main_bicycles_layout import create_main_page_layout

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

def create_type_entry(type):
    file_name = trim_brand_name(type)
    file_name = "details_type/" + file_name + ".html"
    return f"""
                <div class = "details">
                    <a href="{file_name}">{type}</a>
                </div>
            """

def create_main_type_page_layout(html_content):
    return f"""<!DOCTYPE html>
          <html lang="en">
              <head>
                  <meta charset="UTF-8"/>
                  <link rel="stylesheet" type="text/css" href="../assets/css/styles_all_bicycles.css">
                  <title> Main Page </title>
              </head>
              <body>
              <header>
              <div class="overlay">
                    <h1>Rental Bike Baleares</h1>
                    <h3>Reasons for Choosing US</h3>
                    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vero nostrum quis, odio veniam itaque ullam debitis qui magnam consequatur ab. Vero nostrum quis, odio veniam itaque ullam debitis qui magnam consequatur ab.</p>
              </div>
              <header>
              <section>
                  {html_content}
              </section>
              </body>
          </html>"""

def trim_brand_name(brand):
    return brand.replace(' ', '-')

def create_type_detail_page(type, type_bics):
    entries = ''
    for bic in type_bics:
        entries += create_type_bic_entry(bic)

    html = create_detail_type_page_layout(entries)

    with open("../presentation/details_type/" + trim_brand_name(type) + ".html", "w") as external_file:
        print(html, file=external_file)
        external_file.close()

def create_detail_type_page_layout(html_content):
    return f"""<!DOCTYPE html>
          <html lang="en">
              <head>
                  <meta charset="UTF-8"/>
                  <link rel="stylesheet" type="text/css" href="../assets/css/styles_all_bicycles.css">
                  <title> Main Page </title>
              </head>
              <body>
              <header>
              <div class="overlay">
                    <h1>Rental Bike Baleares</h1>
                    <h3>Reasons for Choosing US</h3>
                    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vero nostrum quis, odio veniam itaque ullam debitis qui magnam consequatur ab. Vero nostrum quis, odio veniam itaque ullam debitis qui magnam consequatur ab.</p>
              </div>
              <header>
              <section>
                  {html_content}
              </section>
              </body>
          </html>"""

def create_type_bic_entry(bic):
    return f"""
                    <div class = "details">
                        <a href="../{bic['details_link']}">{bic['model']}</a>
                    </div>
                """