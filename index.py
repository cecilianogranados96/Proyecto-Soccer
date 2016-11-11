#!../python35/python.exe
print ("Content-type: text/html\n")
from contructor import * 
pagina.inicio()
print('''
		<div class="tg-sliderbox">
			<div class="tg-imglayer">
				<img src="images/bg-pattran.png" alt="image desctription">
			</div>
			<div id="tg-home-slider" class="tg-home-slider tg-haslayout">
				<div class="swiper-wrapper">
					<div class="swiper-slide">
						<div class="container">
							<figure class="floating">
								<img src="images/slider/img-01.png" alt="image description">
							</figure>
							<div class="tg-slider-content">
								<h1>Pro<span>   Soccer</span></h1>
								<div class="tg-btnbox">
									<h2>Sistema inteligente</h2>
									<a class="tg-btn" href="nosotros.py"><span>Nosotros</span></a>
									<a class="tg-btn" href="fechas.py"><span>Fechas</span></a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
''')
