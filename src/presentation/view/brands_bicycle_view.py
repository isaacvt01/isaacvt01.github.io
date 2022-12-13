from src.presentation.view.navigation_view import get_navigation_view

def create_detail_brand_page_layout(html_content):
    nav = get_navigation_view()

    return f"""<!DOCTYPE html>
          <html lang="en">
              <head>
                  <meta charset="UTF-8"/>
                  <link rel="stylesheet" type="text/css" href="../assets/css/style_nav.css">
                  <link rel="stylesheet" type="text/css" href="../assets/css/styles_all_bicycles.css">
                  <script src="https://kit.fontawesome.com/ffade7e96a.js" crossorigin="anonymous"></script>
                  <title>Marcas</title>
              </head>
              <body class="body-main_page">
              <header>
              {nav}
              </header>
              <h1>Nuestras bicicletas</h1>
              <section>
                  {html_content}
              </section>
              </body>
          </html>"""


def create_main_brand_page_layout(html_content):
    nav = get_navigation_view()

    return f"""<!DOCTYPE html>
          <html lang="es">
              <head>
                  <meta charset="UTF-8"/>
                  <meta name="generator" content="PyCharm">
                  <link rel="stylesheet" type="text/css" href="./assets/css/style_nav.css">
                  <link rel="stylesheet" type="text/css" href="./assets/css/styles_brands_bicycles.css">
                  <meta name="description" content="Página donde se encuentran las diferentes marcas de bicicletas">
                  <meta name="keywords" content="bicicletas, marcas, orbea, racing, bmc, alquiler, rent, mallorca, bikes, scott foil, cannondale"/>
                  <script src="https://kit.fontawesome.com/ffade7e96a.js" crossorigin="anonymous"></script>
                  <meta name="author" content="Isaac Vásquez y Manuel Ortega"/>
                  <title> Marcas </title>
              </head>
              <body class="body-main_page">
              <header>
                {nav}
              </header>
    <section class="first-photo">
        <div class="banner-text">
            <h1>MONGO-BIKE MALLORCA</h1>
            <h1>Marcas <span>CON LAS QUE CONTAMOS</span></h1>
        </div>
    </section>
    <hgroup>
        <h1 id="title_brands">Marcas de bicicletas</h1>
    </hgroup>
              <section id="brands">
                  {html_content}
              </section>
              </body>
          </html>"""


def create_brands_entry(bic):
    return f"""
                    <div class = "details">
                        
                        <a href="{bic['details_link']}"><img class="imagen_main" src="../assets/images/{bic['image']}"></a>
                        <div>{bic['model']}</div>
                    </div>
                """


def create_brands_layout(brand_name):
    file_name = trim_brand_name(brand_name)
    file_name = "details_brand/" + file_name + ".html"
    return f"""
                <div class = "details">
                    <a href="{file_name}">
                    <img src="./assets/images/brands/{brand_name}.jpg" alt="{brand_name}" class="image">
                    {brand_name}
                </div>
            """


def trim_brand_name(brand):
    return brand.replace(' ', '-')
