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
                  <link rel="stylesheet" type="text/css" href="../assets/css/styles_brands_bicycles.css">
                  <title> Main Page </title>
              </head>
              <body class="body_main_page">
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
