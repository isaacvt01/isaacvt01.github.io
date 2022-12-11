def create_bicycles_layout(html_content):
    return f"""
<!DOCTYPE html>
<html lang="en">
     <head>
         <meta charset="UTF-8"/>
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <link rel="stylesheet" type="text/css" href="../assets/css/styles_all_bicycles.css">
         <script src="https://kit.fontawesome.com/ffade7e96a.js" crossorigin="anonymous"></script>
         <title> Main Page </title>
     </head>
<body>
    <header>
        <nav>
            <div>
                <img class="logo" src="/bicycles-project/assets/images/logo2.png" alt="imagen-logo">
            </div>
            <i class="fa-sharp fa-solid fa-bars"></i>
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
                    <a href="{bic['details_link']}"><img class="imagen_main" src="../assets/images/{bic['image']}"></a>
                    <div>{bic["brand"]}</div>
                    <div>{bic['model']}</div>
                </div>
            """