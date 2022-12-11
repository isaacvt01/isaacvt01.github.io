def get_navigation_view():
    return '''
            <nav class="menu">
            <div>
                <img class="logo" src="/bicycles-project/assets/images/logo2.png" alt="imagen-logo">
            </div>
            <div class="nav-container">
                <ul class="nav-menu">
                    <li><a href="../dist/index.html" target="_blank" class="active">Home</a></li>
                    <li><a href="../dist/brands_main.html" target="_blank">Marcas</a></li>
                    <li><a href="../dist/types_main.html" target="_blank">Tipos</a></li>
                    <li><a href="../dist/bicycles.html" target="_blank">Todas las bicicletas</a></li>
                    <li><a href="../dist/form.html">Formulario de registro</a></li>
                </ul>
                 <i class="nav-mobile-icon fa-sharp fa-solid fa-bars"></i>
            </div>
        </nav>
    '''
