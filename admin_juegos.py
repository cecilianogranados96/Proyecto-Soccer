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
cur1 = conn.cursor()
print('''<div class="tg-banner2 tg-haslayout"></div>''')			

print('''
<h2 style="margin-top: 201px;" ><center>Lista de Juegos</h2>
<br><br><br>
<table class="table">
  <tr>
    <th><h2>Juego</th>
    <th><h2>Resultado</th>
    <th><h2>Eliminar</th>
  </tr>
''')
cur.execute("SELECT * FROM fechas")           
for row in cur:
	print('''
	<tr>
    <th><h3>'''+str(row[2])+ " vs "+str(row[4]) +'''</th>
    <th><h3>'''+str(row[7])+ " - "+str(row[8]) +'''</th>
    <th><h3><a href="juego.py?id='''+str(row[0])+'''" class="btn btn-success">Ver/Editar</a></th>
	</tr>
	''')   
	
print('''</table>''')
	
print('''</td>
</tr>
</table>''')



pagina.fin()
