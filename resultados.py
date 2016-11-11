#!../python35/python.exe
print ("Content-type: text/html\n")
from contructor import * 
pagina.inicio()
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer',autocommit=True)

cur = conn.cursor()
cur.execute("select * from fechas where estado != 0 ")
         				
print('''
		<div class="tg-banner2 tg-haslayout">
		</div>
		<main id="tg-main" class="tg-main tg-haslayout">
			<section class="tg-main-section tg-haslayout">
				<div class="container">
					<div class="tg-section-name">
						<h2>Resultados</h2>
					</div>
					<div class="col-sm-11 col-xs-11 pull-right">
						<div class="row">
							<div class="tab-content tg-tabscontent">''')
for row in cur:
	if (int(row[7]) < int(row[8]) ) :
		#gano 2
		#Datos Gano
		gano = str(row[4])
		gol_gano = str(row[8])
		goleadores = str(row[10])
		#Datos Perdio
		perdio = str(row[2])
		gol_perdio = str(row[7])
		goleadores_p = str(row[9])
	else:
		#Datos Gano
		gano = str(row[2])
		gol_gano = str(row[7])
		goleadores = str(row[9])
		#Datos Perdio
		perdio = str(row[4])
		gol_perdio = str(row[8])
		goleadores_p = str(row[10])
	print('''
								<div role="tabpanel" class="tab-pane fade in active" id="one">
									<div class="tg-matchresult">
										<div class="tg-box">
											<div class="tg-score"><h3>'''+gol_gano+" - "+gol_perdio+'''</h3></div>
											<div class="tg-teamscore">
												<div class="tg-team-nameplusstatus">
													<h4><a href="#">'''+gano+'''</a></h4>
												</div>
												<ul class="tg-playernameplusgoadtime">
													'''+goleadores+'''
												</ul>
											</div>
											<div class="tg-teamscore">
												<div class="tg-team-nameplusstatus">
													<h4><a href="#">'''+perdio+'''</a></h4>
												</div>
												<ul class="tg-playernameplusgoadtime">
													'''+goleadores_p+'''
												</ul>
											</div>
										</div>
									</div>
								</div>''')
					
								
			
							
print('''</ul>
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