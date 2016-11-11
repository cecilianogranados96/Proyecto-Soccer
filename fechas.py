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
							<h1>Fechas de torneos</h1>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!--************************************
				Banner End
		*************************************-->
		<!--************************************
				Main Start
		*************************************-->
		<main id="tg-main" class="tg-main tg-haslayout">
			<section class="tg-main-section tg-haslayout">
				<div class="container">
					<div class="tg-section-name">
						<h2>Proximos Torneos</h2>
					</div>
					<div class="col-sm-11 col-xs-11 pull-right">
						<div class="row">

							<ul class="tg-tickets tg-tabnav" role="tablist">

								
								
								
								'''+datos.fechas()+'''
								
								
								
								
							</ul>
						</div>
					</div>
				</div>
			</section>
		</main>
		<!--************************************
				Main End
		*************************************-->
''')
pagina.fin()