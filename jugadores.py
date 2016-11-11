#!../python35/python.exe
print ("Content-type: text/html\n")
from contructor import * 

import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

id = form.getfirst("id");

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer')
cur = conn.cursor()

cur.execute("SELECT * FROM equipos where id = '"+str(id)+"'")
for row2 in cur:
	row2 = row2
								
								
pagina.inicio()
print('''
	<script src="js/vendor/jquery-library.js"></script>
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
							<h1>'''+row2[1]+" - "+row2[3]+ '''</h1>
						</div>
						<ol class="tg-breadcrumb">
							<li class="active">Escalaf&oacute;n mundial : #'''+str(row2[4])+ '''</li>
						</ol>

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
			<!--************************************
					Top Rated Player Start
			*************************************-->
			<section class="tg-main-section tg-haslayout">
				<div class="container">
					<div class="tg-section-name">
						<h2>Jugadores</h2>
					</div>
					<div class="col-sm-11 col-xs-11 pull-right">
						<div class="row">
							<div class="tg-player-grid2 tg-haslayout">
								<div id="tg-player-slider" class="tg-player-slider tg-haslayout">
									<div class="swiper-wrapper">
									'''+datos.jugadores(id)+'''
										
									</div>
									<div class="tg-themebtnnext"><span class="fa fa-angle-down"></span></div>
									<div class="tg-themebtnprev"><span class="fa fa-angle-up"></span></div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</section>
			<!--************************************
					Top Rated Player End
			*************************************-->
			
		</main>
		<!--************************************
				Main End
		*************************************-->
		''')
pagina.fin()