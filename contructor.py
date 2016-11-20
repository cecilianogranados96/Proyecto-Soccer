#!../python35/python.exe
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer',autocommit=True)
cur2 = conn.cursor()
cur3 = conn.cursor()
cur = conn.cursor()
cur1 = conn.cursor()
cur4 = conn.cursor()
class datos():
        def equipos_header():
                        cur.execute("SELECT * FROM equipos where id != 0")
                        x = ""
                        for row in cur:
                                        x += ("<li><a href='jugadores.py?id="+str(row[0])+"'>"+row[1]+" - "+row[3]+"</a></li>")
                        return (x)
        def jugadores(ide):
                        cur.execute("SELECT * FROM equipos where id = '"+str(ide)+"'")
                        for row2 in cur:
                                row2= row2
                      
                        cur.execute("SELECT * FROM jugadores where id_equipo = '"+str(ide)+"'")
                        x = ""
                        for row in cur:
                                        x += ('''                                                                   
									<div class="swiper-slide"><figure class="tg-postimg">
												<img src="images/player/'''+str(row[5])+'''" alt="image description">
												<!--<div class="tg-img-hover">-->
													<figcaption class="tg-img-hover">
												<a href="#" class="tg-theme-tag">'''+str(row2[1])+'''</a>
                                                    <div class="tg-section-heading">
                                                            <h3><a href="#">'''+str(row[1])+'''</a></h3>
                                                            <span class="tg-stars"><span></span></span>
                                                                  </div>
                                                                     <div class="tg-description">
                                                                          <p>'''+str(row2[2])+'''</p>
                                                                     </div>
																	<div class="tg-description">
                                                                          <p>Posicion: '''+str(row[3])+'''</p>
                                                                     </div>											
																	<div class="tg-description">
                                                                          <p>Numero: '''+str(row[4])+'''</p>
                                                                     </div>
								
																	<ul class="tg-socialicons"><li><a href="#"><i class="fa fa-facebook"></i></a></li><li><a href="#"><i class="fa fa-twitter"></i></a></li> <li><a href="#"><i class="fa fa-linkedin"></i></a></li></ul>
									</div>
										''')
                        return (x)
        def fechas():

                        cur.execute("SELECT * FROM fechas ")

                        x = ""
                        for row in cur:
                                        cur1.execute("SELECT * FROM equipos where id = '"+str(row[2])+"'")
                                        for row2 in cur1:
                                                row2= row2
                                        cur2.execute("SELECT * FROM equipos where id = '"+str(row[3])+"'")
                                        for row3 in cur2:
                                                row3= row3
                                        cur3.execute("SELECT * FROM general")
                                        for row4 in cur3:
                                                row4 = row4
                                        x += ('''<li role="presentation" class="active">
													<a href="#" aria-controls="one" role="tab" data-toggle="tab">
													<div class="tg-ticket">
														<time class="tg-matchdate" datetime="2016-05-03">'''+str(row[1])+''' <span>Fecha</span></time>
														<div class="tg-matchdetail">
															<span class="tg-theme-tag">'''+str(row4[0])+'''</span>
															<h4>'''+str(row[2])+''' <span>vs</span> '''+str(row[4])+'''</h4>
														<ul class="tg-matchmetadata">
															<li><address>'''+str(row[6])+'''</address></li>
														</ul>
													</div>
													<div class="tg-btnsbox">
														<span class="tg-btn" onclick=\'window.open("jugadores.py?id='''+str(row[3])+''' ")\' >Ver: '''+str(row[2])+'''</span>
													</div>
													<div class="tg-btnsbox">
														<span class="tg-btn" onclick=\'window.open("jugadores.py?id='''+str(row[5])+''' ")\'>Ver: '''+str(row[4])+'''</span>
													</div>
													</div>
													</a>
												</li>
										''')
                        return (x)
                
class pagina:
    def inicio():
        print ('''
					<html>
					<head>
						<meta charset="utf-8">
						<meta http-equiv="X-UA-Compatible" content="IE=edge">
						<title>ProSoccer</title>
						<meta name="viewport" content="width=device-width, initial-scale=1">
						<link rel="icon" type="image/png" href="images/logo.png" />
						<link rel="stylesheet" href="css/bootstrap.min.css">
						<link rel="stylesheet" href="css/normalize.css">
						<link rel="stylesheet" href="css/font-awesome.min.css">
						<link rel="stylesheet" href="css/transitions.css">
						<link rel="stylesheet" href="css/prettyPhoto.css">
						<link rel="stylesheet" href="css/swiper.min.css">
						<link rel="stylesheet" href="css/jquery-ui.css">
						<link rel="stylesheet" href="css/animate.css">
						<link rel="stylesheet" href="css/owl.theme.css">
						<link rel="stylesheet" href="css/owl.carousel.css">
						<link rel="stylesheet" href="css/customScrollbar.css">
						<link rel="stylesheet" href="css/icomoon.css">
						<link rel="stylesheet" href="css/main.css">
						<link rel="stylesheet" href="css/color.css">
						<link rel="stylesheet" href="css/responsive.css">
						
					</head>
					<body>
						<div id="tg-wrapper" class="tg-wrapper tg-haslayout">
							<header id="tg-header" class="tg-header tg-haslayout">
								<div class="container">
									<div class="col-md-10 col-md-offset-1 col-sm-12 col-xs-12">
										<div class="row">
											<div class="tg-topbar tg-haslayout">
												<nav id="tg-topaddnav" class="tg-topaddnav">
													<div class="navbar-header">
														<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#tg-addnavigationm-mobile">
															<i class="fa fa-arrow-right"></i>
														</button>
													</div>
												</nav>
											</div>
											<nav id="tg-nav" class="tg-nav brand-center">
												<div class="navbar-header">
													<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#tg-navigationm-mobile">
														<i class="fa fa-bars"></i>
													</button>
													<strong class="tg-logo">
														<a href="index.py"><img src="images/logo.png" alt="image description"></a>
													</strong>
												</div>
												<div id="tg-navigation" class="tg-navigation">
														<div class="tg-colhalf">
															<ul>
																<li class="active">
																	<a href="index.py">Inicio</a>
																</li>
																<li>
																	<a href="#">Equipos</a>
																	<ul class="tg-dropdown-menu">
																		'''+datos.equipos_header()+'''
																	</ul>
																</li>
																<li><a href="fechas.py">Fechas</a></li>
															</ul>
														</div>
														<div class="tg-colhalf">
															<ul>
															<li>
																<a href="ayuda.py">Ayuda</a>
																
																<ul class="tg-dropdown-menu">
																	<li><a href="ayuda.py">Ayuda</a></li>
																	<li><a href="nosotros.py">Acerca de</a></li>
																	
																<li>
																	<a href="admin_general.py">Configuracion</a>
																	<ul class="tg-dropdown-menu">
																		<li><a href="admin_general.py">Administracion General</a></li>
		''')
        cur4.execute("SELECT fecha FROM general")
        for row in cur4:
                row = row
        if row[0] == 0:
                print('''<li><a href="admin_equipos.py">Administracion Equipos</a></li>''')
        else:        
                print('''<li><a href="#">Administracion Equipos (Inactiva)</a></li>''')
        print('''								
				<li><a href="admin_jugadores.py">Administracion Jugadores</a></li>
				<li><a href="admin_juegos.py">Marcadores</a></li>
			''')
        cur4.execute("SELECT fecha FROM general")
        for row in cur4:
                row = row
                if row[0] != 1:
                        print('''<li><a href="roudrobin.py">Generar Fechas</a></li>''')
                else:
                        print('''<li><a href="reiniciar.py">Reiniciar Sistema</a></li>''')
                print('''           </ul>
										</li>
										</ul>
											</li>
											<li>
												<a href="resultados.py">Resultados</a>
											</li>
											<li>
												<a href="tabla.py">Pocisiones</a>
												<ul class="tg-dropdown-menu">
													<li><a href="tabla.py">Tabla General</a></li>
													<li><a href="tabla_jugadores.py">Tabla Jugadores</a></li>
												</ul>
											</li>
										</ul>
									</div>
							</div>
						</nav>
					</div>
				</div>
			</div>
		</header>
''')
    def fin ():
        print ('''
				<footer id="tg-footer" class="tg-footer tg-haslayout">
					<div class="tg-footerbar">
						<div class="container">
							<span class="tg-copyright"><center>&copy; 2016  |  Todos los derechos reservados | Dise&ntilde;o y programacion: Jose Andres Ceciliano G. | Tecnologico de Costa Rica</span>
						</div>
					</div>
				</footer>
			</div>
			<script src="js/vendor/bootstrap.min.js"></script>
			<script src="js/customScrollbar.min.js"></script>
			<script src="js/owl.carousel.js"></script>
			<script src="js/isotope.pkgd.js"></script>
			<script src="js/prettyPhoto.js"></script>
			<script src="js/swiper.min.js"></script>
			<script src="js/jquery-ui.js"></script>
			<script src="js/countTo.js"></script>
			<script src="js/appear.js"></script>
			<script src="js/main.js"></script>
		</body>
		</html>			
		''')



