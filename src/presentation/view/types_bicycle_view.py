from src.presentation.view.navigation_view import get_navigation_view


def create_type_entry(type):
    file_name = trim_type_name(type)
    file_name = "details_type/" + file_name + ".html"
    return f"""
                <div class = "details">
                    <a href="{file_name}">
                    <img src="./assets/images/types/{type}.jpg" alt="{type}" class="image">
                    {type}
                    </a>
                </div>
            """


def create_main_type_page_layout(html_content):
    nav = get_navigation_view()

    return f"""<!DOCTYPE html>
          <html lang="es">
              <head>
                  <meta charset="UTF-8"/>
                  <link rel="stylesheet" type="text/css" href="./assets/css/style_nav.css">
                  <link rel="stylesheet" type="text/css" href="./assets/css/styles_types_bicycles.css">
                  <meta name="author" content="Isaac Vásquez y Manuel Ortega"/>
                  <meta name="generator" content="PyCharm">
                  <meta name="keywords" content="bicicletas, marcas, orbea, racing, bmc, alquiler, rent, mallorca, bikes, scott foil, cannondale"/>
                  <meta name="description" content="Mostramos las bicicletas separadas por tipo en esta página.">
                  <script src="https://kit.fontawesome.com/ffade7e96a.js" crossorigin="anonymous"></script>
                  <title> Tipos </title>
              </head>
              <body class="body-main_page">
              <header>
              {nav}
              </header>
        <section class="first-photo">
            <div class="banner-text">
                <h1>MONGO-BIKE MALLORCA</h1>
                <h1>Tipos de bicicletas <span>CON LOS QUE CONTAMOS</span></h1>
            </div>
        </section>
        <hgroup>
            <h1 id="title_types">Tipos de bicicletas</h1>
        </hgroup>
              <section id="types">
                  {html_content}
              </section>
              <footer>
        <hr>
        <h3>MongoBike</h3>
        <h4>@MONGO-BIKE</h4>
        <p>Dise�ador web: Isaac V�squez / Manuel Ortega</p>
        <p>Aviso legal | Pol�tica de privacidad</p>
        <div class="social-networks">
            <i class="fa-brands fa-facebook"></i>
            <i class="fa-brands fa-instagram"></i>
            <i class="fa-brands fa-linkedin"></i>
        </div>
    </footer>
              </body>
          </html>"""


def trim_type_name(type):
    return type.replace(' ', '-')


def create_detail_type_page_layout(html_content):
    nav = get_navigation_view()

    return f"""<!DOCTYPE html>
          <html lang="en">
              <head>
                  <meta charset="UTF-8"/>
                  <link rel="stylesheet" type="text/css" href="./assets/css/style_nav.css">
                  <link rel="stylesheet" type="text/css" href="./assets/css/styles_all_bicycles.css">
                  <title> Main Page </title>
              </head>
              <body class="body-main_page">
              <header>
              {nav}
              <header>
              <section>
                  {html_content}
              </section>
              </body>
          </html>"""


def create_type_bic_entry(bic):
    return f"""
                    <div class = "details">
                        <a href="./{bic['details_link']}">{bic['model']}</a>
                    </div>
                """
