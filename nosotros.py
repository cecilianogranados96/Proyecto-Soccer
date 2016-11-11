#!../python35/python.exe
print ("Content-type: text/html\n")
from contructor import * 
pagina.inicio()
print('''
		<!--************************************
				Banner Start
		*************************************-->
		<div class="tg-banner tg-haslayout">
			<div class="tg-imglayer">
				<img src="images/bg-pattran.png" alt="image desctription">
			</div>
			<div class="container">
				<div class="row">
					<div class="tg-banner-content tg-haslayout">
						<div class="tg-pagetitle">
							<h1>Nosotros</h1>
							</div>
					</div>
				</div>
			</div>
		</div>
		<!--************************************
				Banner End
		*************************************-->
		<main id="tg-main" class="tg-main tg-haslayout">
			<!--************************************
					About Us Start
			*************************************-->
			<section class="tg-main-section tg-haslayout">
				<div class="container">
					<div class="tg-section-name">
						<h2>Nosotros</h2>
					</div>
					<div class="col-sm-11 col-xs-11 pull-right">
						<div class="row">
							<div class="tg-aboutussection">
								<div class="row">
									<div class="col-md-6 col-sm-12 col-xs-12">
										<figure>
											<img src="images/img-01.jpg" alt="image description">
										</figure>
									</div>
									<div class="col-md-6 col-sm-12 col-xs-12">
										<div class="tg-contentbox">
											<div class="tg-section-heading"><h2><b><center>IV Proyecto de programacion  Tecnologico de Costa Rica</h2></div>
											<div class="tg-description">
												<p><h4><b>Version:</b> 1.0<br>
												<b>Programador: </b>Jose Andres Ceciliano<br>
												<b>Tipo: </b>Python Web - MySQL<br>
												<b>Encargado:</b> Wiliam Mata<br>
												<b>Curso:</b> Taller de Programacion</p>
											</div>
										
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</section>

			<section class="tg-main-section tg-haslayout tg-bgdark">
				<div class="container">
					<div class="row">
						<div class="col-sm-12 col-xs-12">
							<div class="tg-statistics">
								<div class="tg-statistic tg-goals">
									<span class="tg-icon icon-Icon1"></span>
									<h2><span class="tg-statistic-count" data-from="0" data-to="900" data-speed="8000" data-refresh-interval="50">2700</span></h2>
									<h3>Goles</h3>
								</div>
								<div class="tg-statistic tg-activeplayers">
									<span class="tg-icon icon-Icon2"></span>
									<h2><span class="tg-statistic-count" data-from="0" data-to="200" data-speed="8000" data-refresh-interval="50">1673</span></h2>
									<h3>Visitas</h3>
								</div>
								<div class="tg-statistic tg-activeteams">
									<span class="tg-icon icon-Icon3"></span>
									<h2><span class="tg-statistic-count" data-from="0" data-to="100" data-speed="8000" data-refresh-interval="50">236</span></h2>
									<h3>Equipos</h3>
								</div>
								<div class="tg-statistic tg-earnedawards">
									<span class="tg-icon icon-Icon4"></span>
									<h2><span class="tg-statistic-count" data-from="0" data-to="500" data-speed="8000" data-refresh-interval="50">197</span></h2>
									<h3>Datos</h3>
								</div>
							</div>
						</div>
					</div>
				</div>
			</section>
			
''')
pagina.fin()
	