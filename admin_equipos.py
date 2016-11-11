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

print('''<div class="tg-banner2 tg-haslayout"></div>''')

			
print('''
	<br><br><br>
<h1 style="margin-top: 201px;"><center>Administracion de equipos</center></h1>	<br><br><br>	
<center>
<table>
<tr>
	<td>
<h2>Nuevo Equipos</h2><h3>
<br><br><br>
<form class="form-horizontal" method="POST" action="nuevo_equipo.py">
<div class="form-group">
  <label class="col-md-4 control-label" for="equipo">Nombre equipo</label>  
  <div class="col-md-4">
  <input id="equipo" name="nombre" type="text" placeholder="Nombre Equipo" class="form-control input-md" required >
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="equipo">Siglas</label>  
  <div class="col-md-4">
  <input id="equipo" name="siglas" type="text" placeholder="Siglas" class="form-control input-md" maxlength="3" required >
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="equipo">Numero Clasificacion</label>  
  <div class="col-md-4">
  <input id="equipo" name="numero" type="text" placeholder="Numero" class="form-control input-md" maxlength="2" required >
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="lema">Lema del equipo</label>
  <div class="col-md-4">                     
    <textarea class="form-control" id="lema" name="lema" ></textarea>
  </div>
</div>
<button type="submit"  class="btn btn-primary"><h3 style="color:#FFFFFF">Enviar</button>
</fieldset>
</form>
	</td>
	<td>''')
print('''
<h2>Lista de Equipos</h2>
<br><br><br>
<table class="table">
  <tr>
    <th><h2>Nombre</th>
    <th><h2>Lema</th>
    <th><h2>Eliminar</th>
  </tr>
''')
cur.execute("SELECT * FROM equipos where id!=0")           
for row in cur:
    print('''   <tr>
    <th><h3>'''+str(row[1])+'''</th>
    <th><h3>'''+str(row[2])+'''</th>
    <th><h3><a href="eliminar_equipo.py?borrar='''+str(row[0])+'''" class="btn btn-danger">Eliminar</a></th>
	</tr>
	''')          					
print('''</table>''')
	
print('''</td>
</tr>
</table>''')



pagina.fin()