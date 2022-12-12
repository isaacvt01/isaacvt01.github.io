from src.presentation.view.navigation_view import get_navigation_view

def create_bicycle_details_layout(bic):
    nav = get_navigation_view()

    html = f"""
        <!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="./assets/css/style_nav.css">
    <meta name="description" content="Aquí podrás leer todos los detalles de la bicicleta deseada">
    <meta name="keywords" content="bicicletas, marcas, orbea, racing, bmc, alquiler, rent, mallorca, bikes, scott foil, cannondale"/>
    <link rel="stylesheet" type="text/css" href="./assets/css/styles_details_bicycles.css">
    <meta name="author" content="Isaac Vásquez y Manuel Ortega"/>
    <meta name="generator" content="PyCharm">
    <script src="https://kit.fontawesome.com/ffade7e96a.js" crossorigin="anonymous"></script>
    <title>Detalles</title>
</head>

<body class="body-main_page">
    <header>
        {nav}
    </header>
    <div class="content">
        <h1><b>Detalles de <span>{bic["model"]}</span></b></h1>
        <section>
                <a href="https://www.sanferbike.com/es/" target="_blank"><img src="./assets/images/{bic['image']}" alt="bike-photo"></a>
            
            <div class="descrip_specifications-details">
                <p>{bic["model"]}</p>
            
            
                <p>{bic["description"]}</p>


                <p>{bic["specifications"]['Cassette']}</p>
                <p>{bic["specifications"]['Material']}</p>
                <p>{bic["specifications"]['Chain']}</p>
                <p>{bic["specifications"]['Saddle']}</p>
                <p>{bic["specifications"]['Wheels']}</p>
                <p>{bic["specifications"]['Power']}</p>
                <p>{bic["specifications"]['Fork']}</p>
                <p>{bic["specifications"]['Brakes']}</p>
                <p>{bic["specifications"]['Frame']}</p>
                <p>{bic["specifications"]['Handlebar']}</p>
                <p>{bic["specifications"]['Seat post']}</p>
            </div>
        </section>
    </div>

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

    return html
