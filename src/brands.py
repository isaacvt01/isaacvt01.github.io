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

def create_detail_brand_page_layout(html_content):
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

def create_main_brand_page_layout(html_content):
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

def create_bic_entry(bic):
    return f"""
                    <div class = "details">
                        <a href="../{bic['details_link']}">{bic['model']}</a>
                    </div>
                """

def create_brands_layout(brand_name):
    file_name = trim_brand_name(brand_name)
    file_name = "details_brand/" + file_name + ".html"
    return f"""
                <div class = "details">
                    <a href="{file_name}">{brand_name}</a>
                </div>
            """


def trim_brand_name(brand):
    return brand.replace(' ', '-')