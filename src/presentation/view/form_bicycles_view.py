from src.presentation.view.navigation_view import get_navigation_view

def create_form_page_layout():
    nav = get_navigation_view()

    return f"""
<!DOCTYPE html>
<html lang="es" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="../assets/css/style_nav.css">
    <link rel="stylesheet" type="text/css" href="/../assets/css/styles_form_bicycles.css">
    <script src="https://kit.fontawesome.com/ffade7e96a.js" crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body class="body-main_page">
    <header>
        {nav}
    </header>

    <section class="first-photo">
        <div class="banner-text">
            <h1>MONGO-BIKE MALLORCA</h1>
            <h1>Reserva tu bicicleta <span>CON NOSOTROS</span></h1>
        </div>
    </section>

    <section>
        <hgroup>
    <h1>Introduce tus datos aquí:</h1>
        </hgroup>
        <form action="http://www.infojobs.com" method="get">
        <div class="group">
            <input type="text" placeholder="Nombre y Apellidos" id="nombre"><span class="highlight" ></span><span class="bar"></span>
            
        </div>
        <div class="group">
            <input type="email" placeholder="Email"><span class="highlight"></span><span class="bar"></span>
            
        </div>
        <div class="group">
            <input type="text" placeholder="Envíanos un mensaje"><span class="highlight"></span><span class="bar"></span>
            
        </div>
        <button type="submit" class="button buttonBlue">Enviar
        </button>
        </form>
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
"""
