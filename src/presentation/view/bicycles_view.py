from src.presentation.view.navigation_view import get_navigation_view


def create_bicycles_layout(html_content):
    nav = get_navigation_view()
    return f"""
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8"/>
        <meta name="generator" content="PyCharm">
        <link rel="stylesheet" type="text/css" href="./assets/css/style_nav.css">
        <link rel="stylesheet" type="text/css" href="./assets/css/styles_all_bicycles.css">
        <meta name="author" content="Isaac Vásquez y Manuel Ortega"/>
        <meta name="keywords" content="bicicletas, marcas, orbea, racing, bmc, alquiler, rent, mallorca, bikes, scott foil, cannondale"/>
        <meta name="description" content="Página donde se ven todas las bicicletas disponibles">
        <script src="https://kit.fontawesome.com/ffade7e96a.js" crossorigin="anonymous"></script>
        <title> Todas las bicicletas </title>
    </head>
    <body class="body-main_page">
        
        <header>
            {nav}
        </header>
        <h1>Todas las bicicletas</h1>
        <section>
            {html_content}
        </section>
        <footer>
            <hr>
            <h3>MongoBike</h3>
            <h4>@MONGO-BIKE</h4>
            <p>Diseñador web: Isaac Vásquez / Manuel Ortega</p>
            <p>Aviso legal | Política de privacidad</p>
            <div class="social-networks">
                <i class="fa-brands fa-facebook"></i>
                <i class="fa-brands fa-instagram"></i>
                <i class="fa-brands fa-linkedin"></i>
            </div>
        </footer>
    </body>
</html>"""


def create_all_bicycles_layout(bic):
    return f"""
                <div class = "details">
                    <a href="{bic['details_link']}"><img class="imagen_main" src="./assets/images/{bic['image']}"></a>
                    <div class="brand_bike">{bic["brand"]}</div>
                    <div class="brand_bike">{bic['model']}</div>
                </div>
            """
