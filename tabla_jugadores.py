#!../python35/python.exe
print ("Content-type: text/html\n")
from contructor import * 

pagina.inicio()

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer')
cur = conn.cursor()
cur2 = conn.cursor()

################# ORDENAMIENTO
def ordenamiento(matriz):
    '''Retorna la matriz ordenada por el metodo de la burbuja conservando los datos de la posicion 0'''
    for i in range(1, len(matriz)):
        for j in range(len(matriz) - i):
            if matriz[j][1] < matriz[j+1][1]:
                temp = matriz[j][0], matriz[j][1]
                matriz[j][0], matriz[j][1] = matriz[j+1][0], matriz[j+1][1]
                matriz[j+1][0], matriz[j+1][1] = temp
    return(matriz)
################# ORDENAMIENTO

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
matriz = []
for row2 in cur2:
	cur.execute("select jugadores.foto,COALESCE(COUNT(id_gol),0) as gol,jugadores.nombre_jugador,equipos.nombre,equipos.id,jugadores.id_equipo,jugadores.id_jugador,goles.id_jugador from goles,jugadores,equipos where goles.id_jugador = "+str(row2[0])+" and jugadores.id_jugador = "+str(row2[0])+" and equipos.id = jugadores.id_equipo order by gol ")
	for row3 in cur:
		matriz.append([[row3[2],row3[3],row3[0]],row3[1]]) #Llenamos la matriz con los campos la posicion 1 lleva los goles y la 0 los datos del jugador
m = ordenamiento(matriz) #ordenamos y luego simplemente mostramos 
for x in m:
	print('''<tr>
				<td><img src="images/player/'''+str(x[0][2])+'''"  style="width: 98px;"alt="image description"></td>
				<td><h3 style="line-height: 6;">'''+str(x[0][0])+'''</td>
				<td><h3 style="line-height: 6;">'''+str(x[0][1])+'''</td>
				<td><h3 style="line-height: 6;" >'''+str(x[1])+'''</td>
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