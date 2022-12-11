def create_bicycle_details_layout(bic):
    html = f"""
        <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/bicycles-project/assets/css/styles_details_bicycles.css">
    <script src="https://kit.fontawesome.com/ffade7e96a.js" crossorigin="anonymous"></script>
    <title>Document</title>
</head>

<body>
    <header>
        <nav>
            <div>
                <img class="logo" src="/bicycles-project/assets/images/logo2.png" alt="imagen-logo">
            </div>
            <i class="fa-sharp fa-solid fa-bars"></i>
            </label>
            <ul class="nav-menu">
                <li><a href="http://localhost:63342/bicycles-project/presentation/index.html?_ijt=nusf4d02h388gjoo14lboqlc05"
                        class="active">Home</a></li>
                <li><a
                        href="http://localhost:63342/bicycles-project/presentation/brands_main.html?_ijt=nusf4d02h388gjoo14lboqlc05">Marcas</a>
                </li>
                <li><a
                        href="http://localhost:63342/bicycles-project/presentation/types_main.html?_ijt=nusf4d02h388gjoo14lboqlc05">Tipos</a>
                </li>
                <li><a
                        href="http://localhost:63342/bicycles-project/presentation/bicycles.html?_ijt=nusf4d02h388gjoo14lboqlc05">Todas
                        las bicicletas</a></li>
                <li><a href="">Formulario de registro</a></li>
            </ul>
        </nav>
    </header>
    <div class="content">
        <h1><b>Detalles de <span>{ bic["model"]}</span></b></h1>
        <section>
                <a href="https://www.sanferbike.com/es/" target="_blank"><img src="/assets/images/{bic['image']}" alt="bike-photo"></a>
            
            <div class="descrip_specifications-details">
                <p>{bic["model"]}</p>
            
            
                <p>{bic["description"]}</p>


                <p>{bic["specifications"]}</p>
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

