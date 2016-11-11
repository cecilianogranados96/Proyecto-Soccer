#!../python35/python.exe
print ("Content-type: text/html\n")
from contructor import * 
pagina.inicio()

import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer')
cur = conn.cursor()						
print('''
		<div class="tg-banner2 tg-haslayout">

		</div>

		<h1><center><br><br><br>
	<a href="admin_general.py" class="btn btn-lg btn-danger">Administracion General</a><br><br>
	<a href="admin_equipos.py" class="btn btn-lg btn-primary">Administracion de equipos</a><br><br>
	<a href="admin_jugadores.py" class="btn btn-lg btn-success">Administracion de Jugadores</a><br><br>
	<a href="admin_juego.py" class="btn btn-lg btn-warning">Administracion de Juegos</a><br><br><br>
  
  
''')

pagina.fin()