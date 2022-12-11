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
