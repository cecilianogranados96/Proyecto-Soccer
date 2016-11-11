#!../python35/python.exe
print ("Content-type: text/html\n")
from contructor import * 
pagina.inicio()
print('''
		<!--************************************
					Points Table Start
			*************************************-->
			<section class=" tg-haslayout tg-bgstyletwo">
				<div class="tg-bgboxone"></div>
				<div class="tg-bgboxtwo"></div>
				<div class="tg-bgpattrant">
					<div class="container">
						<div class="row">
							<div class="tg-pointstablewrapper">
								<div class="col-sm-12 col-xs-12">
									<div class="tg-pointstable">
										<div class="tg-section-heading"><h2>Tabla de resultados</h2></div>
										<div id="tg-pointstable-slider" class="tg-pointstable-slider">
											<div class="swiper-wrapper">
											
												<div class="swiper-slide">
													<div class="tg-pointtable">

														<div class="tg-box">Equipo</div>			
														<div class="tg-box">Juegos Jugados</div>
														<div class="tg-box">Juegos Ganados</div>
														<div class="tg-box">Juegos Empatados</div>
														<div class="tg-box">Juegos Perdidos</div>
														<div class="tg-box">Goles a Favor</div>
														<div class="tg-box">Goles en Contra</div>
														<div class="tg-box">Goles de Direfencia</div>
														<div class="tg-box">Puntos Totales</div>
													</div>''')

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer',autocommit=True)
cur1 = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()
cur4 = conn.cursor()
cur5 = conn.cursor()
cur6 = conn.cursor()
cur7 = conn.cursor()
cur8= conn.cursor()
cur8.execute("SELECT puntos_p_ganado FROM general")
for d in cur8:
	d = d
cur1.execute("SELECT * FROM equipos where id != 0")
for row in cur1:
	cur2.execute("select COUNT(id_fecha) from fechas where estado != 0 and (id_equipo1 = "+str(row[0])+" or id_equipo2 = "+str(row[0])+") ")
	for jj in cur2:
		jj = jj
	cur3.execute("SELECT COUNT(id_fecha) from fechas where gano = "+str(row[0])+"  ")
	jg = [[0]]
	for jg in cur3:
		jg = jg
	cur4.execute("SELECT COUNT(id_fecha) from fechas where (id_equipo1= "+str(row[0])+" or id_equipo2= "+str(row[0])+") and empato = 1 ")
	je = [[0]]
	for je in cur4:
		je = je
	cur5.execute("SELECT COUNT(id_fecha) from fechas where perdio = "+str(row[0])+"  ")
	jp = [[0]]
	for jp in cur5:
		jp = jp
	cur6.execute("SELECT COALESCE(ABS(sum(gol_gano)),0) from fechas where gano = "+str(row[0])+"  ")
	gf = [0]
	for gf in cur6:
		gf = gf
	cur7.execute("SELECT COALESCE(ABS(sum(gol_perdio)),0) from fechas where perdio = "+str(row[0])+"  ")
	gc = [[0]]
	for gc in cur7:
		gc = gc
	print('''<div class="tg-pointtable">
				<div class="tg-box"><a href="jugadores.py?id='''+str(row[0])+'''">'''+str(row[1])+'''</a></div>			
				<div class="tg-box">JJ '''+str(jj[0])+'''</div>
				<div class="tg-box">JG '''+str(jg[0])+'''</div>
				<div class="tg-box">JE '''+str(je[0])+'''</div>
				<div class="tg-box">JP '''+str(jp[0])+'''</div>
				<div class="tg-box">GF '''+str(gf[0])+'''</div>
				<div class="tg-box">GC '''+str(gc[0])+'''</div>
				<div class="tg-box">GD '''+str(int(gf[0])-int(gc[0]))+'''</div>
				<div class="tg-box">PUNTOS '''+str(int(gf[0]) * d[0])+'''</div>
			</div>''')
													
							
print('''												</div>
											
											
											</div>
											<div class="tg-themebtnnext"><span class="fa fa-angle-down"></span></div>
											<div class="tg-themebtnprev"><span class="fa fa-angle-up"></span></div>
										</div>
								
									</div>
								</div>
						
						
						
							</div>
						</div>
					</div>
				</div>
			</section>
			<!--************************************
					Points Table End
			*************************************-->

		''')
pagina.fin()