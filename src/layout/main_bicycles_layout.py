def create_main_page_layout():
    return f"""
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../assets/css/styles_main_page.css">
    <script src="https://kit.fontawesome.com/ffade7e96a.js" crossorigin="anonymous"></script>
    <title>Document</title>
</head>

<body class="body-main_page">
    <header>
        <nav class="menu">
            <div>
                <img class="logo" src="/bicycles-project/assets/images/logo2.png" alt="imagen-logo">
            </div>
            <label for="check" class="bar-btn">
                <i class="fa-sharp fa-solid fa-bars"></i>
            </label>
            <ul class="nav-menu">
                <li><a href="http://localhost:63342/bicycles-project/presentation/index.html?_ijt=nusf4d02h388gjoo14lboqlc05" target="_blank" class="active">Home</a></li>
                <li><a href="http://localhost:63342/bicycles-project/presentation/brands_main.html?_ijt=nusf4d02h388gjoo14lboqlc05" target="_blank">Marcas</a></li>
                <li><a href="http://localhost:63342/bicycles-project/presentation/types_main.html?_ijt=nusf4d02h388gjoo14lboqlc05" target="_blank">Tipos</a></li>
                <li><a href="http://localhost:63342/bicycles-project/presentation/bicycles.html?_ijt=nusf4d02h388gjoo14lboqlc05" target="_blank">Todas las bicicletas</a></li>
                <li><a href="">Formulario de registro</a></li>
            </ul>
        </nav>
    </header>

    <section class="first-photo">
        <div class="banner-text">
            <h1>MONGO-BIKE MALLORCA</h1>
            <h1>Reserva tu bicicleta <span>CON NOSOTROS</span></h1>
            <div class="botones">
                <a href="#" class="button1">REGISTRO</a>
                <a href="http://localhost:63342/bicycles-project/presentation/bicycles.html?_ijt=nusf4d02h388gjoo14lboqlc05" target="_blank"" class="button2">BICICLETAS DISPONIBLES</a>
            </div>
        </div>
    </section>

    <section class="about-us">
        <h2 class="first-element-body">A diferencia de la competencia,<br> <span>Mongo-Bikes</span> no cobra tarifas de
            <br> reserva adicionales ni tarifas de <br> conveniencia. ¡Lo que ve es lo que <br> paga!
        </h2>
    </section>

    <section class="icons">
        <div class="logos-description1">
            <img class="icon-img" src="../assets/images/icon-precios.svg" alt="icon1">
            <h4>Los mejores precios</h4>
        </div>
        <div class="logos-description2">
            <img class="icon-img" src="../assets/images/icon-tiempo.svg" alt="icon2">
            <h4>Fácil y conveniente</h4>
        </div>
        <div class="logos-description3">
            <img class="icon-img" src="../assets/images/icon-eco.svg" alt="icon3">
            <h4>Por un mundo mejor</h4>
        </div>
        <div class="logos-description4">
            <img class="icon-img" src="../assets/images/icon-facilidad.svg" alt="icon4">
            <h4>Mejores rincones de Mallorca</h4>
        </div>

    </section>

    <section class="catedral">
        <div class="routes">
            <h5>RUTAS RECOMENDADAS POR NOSOTROS</h5>
            <h2>CONOCE LAS MEJORES RUTAS DE MALLORCA</h2>
            <p>Todas nuestras tiendas, vienen con un mapa indicando algunas de las rutas<br> que se pueden hacer en la
                isla
                Mallorca. <br>Dependiendo de la localización de la tienda, le indicaremos las rutas más cercanas<br> a
                ella.
                Entre
                otras tenemos:</p>
            <ul>
                <li>Paseo Maritimo</li>
                <li>Sa Calobra</li>
                <li>Coll de Femenia</li>
                <li>Cap de Formentor</li>
                <li>Galilea</li>
            </ul>
            <video width="550" height="400" controls>
                <source src="/bicycles-project/assets/images/video_bicycles.mp4" type="video/mp4">
              Your browser does not support the video tag.
              </video>
        </div>

        <div class="img-routes">
            <img class="img-catedral" class="img-catedral-vert"
                src="../assets/images/pelayo-arbues-BB_m1hV5zlY-unsplash (1).jpg" alt="image-catedral">
            <img class="img-catedral, img-catedral-hori"
                src="../assets/images/yves-alarie-O0xdBP5yCqo-unsplash.jpg" alt="image-catedral2">
        </div>
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

</html>

    """
