from src.presentation.view.navigation_view import get_navigation_view


def create_bicycles_layout(html_content):
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
              </header>
              <section>
                  {html_content}
              </section>
              </body>
          </html>"""


def create_all_bicycles_layout(bic):
    return f"""
                <div class = "details">
                    <a href="{bic['details_link']}"><img class="imagen_main" src="../assets/images/{bic['image']}"></a>
                    <div>{bic["brand"]}</div>
                    <div>{bic['model']}</div>
                </div>
            """
