#!../python35/python.exe
print ("Content-type: text/html\n")
from contructor import * 
pagina.inicio()


import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer')
cur = conn.cursor()
cur2 = conn.cursor()

#################FALTA ORDENAMIENTO
	

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
									
										<table class="table" style="background:#f7f7f7;margin-top: 42px;" >
										<tr>
											<td><h3>Imagen</td>
											<td><h3>Jugador</td>
											<td><h3>Equipo</td>
											<td><h3>Goles</td>
										</tr>''')
cur2.execute("SELECT id_jugador FROM jugadores")
for row2 in cur2:
	cur.execute("select jugadores.foto,COALESCE(COUNT(id_gol),0) as gol,jugadores.nombre_jugador,equipos.nombre,equipos.id,jugadores.id_equipo,jugadores.id_jugador,goles.id_jugador from goles,jugadores,equipos where goles.id_jugador = "+str(row2[0])+" and jugadores.id_jugador = "+str(row2[0])+" and equipos.id = jugadores.id_equipo order by gol ")
	for row3 in cur:
		row3 = row3
		#print(list(row3))										
		print('''<tr>
											<td><img src="images/player/'''+str(row3[0])+'''"  style="width: 98px;"alt="image description"></td>
											<td><h3 style="line-height: 6;">'''+str(row3[2])+'''</td>
											<td><h3 style="line-height: 6;">'''+str(row3[3])+'''</td>
											<td><h3 style="line-height: 6;" >'''+str(row3[1])+'''</td>
										</tr>''')
										
print('''</table>
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