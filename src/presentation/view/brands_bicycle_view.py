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


def create_main_brand_page_layout(html_content):
    nav = get_navigation_view()

    return f"""<!DOCTYPE html>
          <html lang="en">
              <head>
                  <meta charset="UTF-8"/>
                  <link rel="stylesheet" type="text/css" href="../assets/css/style_nav.css">
                  <link rel="stylesheet" type="text/css" href="../assets/css/styles_brands_bicycles.css">
                  <script src="https://kit.fontawesome.com/ffade7e96a.js" crossorigin="anonymous"></script>
                  <title> Main Page </title>
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
                        <a href="../{bic['details_link']}">{bic['model']}</a>
                    </div>
                """


def create_brands_layout(brand_name):
    file_name = trim_brand_name(brand_name)
    file_name = "details_brand/" + file_name + ".html"
    return f"""
                <div class = "details">
                    <a href="{file_name}">
                    <img src="../assets/images/brands/{brand_name}.jpg" alt="{brand_name}" class="image">
                    {brand_name}
                </div>
            """


def trim_brand_name(brand):
    return brand.replace(' ', '-')
