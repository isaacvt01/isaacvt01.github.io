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
