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
cur2 = conn.cursor()
cur.execute("SELECT * FROM general")
for row in cur:
    row = row 
	
cur2.execute("select COUNT(id) from equipos")
for row2 in cur2:
    row2 = row2 
	
						
print('''<div class="tg-banner2 tg-haslayout"></div>''')			
print('''
	<br><br><br>
<h1 style="margin-top: 201px;"><center>Administracion de General</center></h1>	<br><br><br>	
<center>
<form class="form-horizontal" action="actualizar_general.py" method="POST">
<fieldset>

<!-- Form Name -->
<legend></legend>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="">Nombre del torneo</label>  
  <div class="col-md-4">
  <input  name="nombre"  value="'''+str(row[0])+'''" type="text" placeholder="" class="form-control input-md" required >
    
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="clasificados">Cantidad de clasificados</label>  
  <div class="col-md-4">
  <input id="clasificados" value="'''+str(row[2])+'''" name="clasificados" type="number" min="1" max="100" placeholder="" class="form-control input-md" required >
    
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="equipos">Cantidad de equipos</label>  
  <div class="col-md-4">
  <input id="equipos" value="'''+str(row2[0])+'''" name="equipos" type="text" placeholder="" class="form-control input-md" disabled>
    
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="empatado">Puntos por partido empatado</label>  
  <div class="col-md-4">
  <input id="empatado" value="'''+str(row[4])+'''" name="empatado" type="number" min="1" max="100" placeholder="" class="form-control input-md" required >
    
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="ganado">Puntos por partido ganado</label>  
  <div class="col-md-4">
  <input id="ganado" value="'''+str(row[3])+'''" name="ganado" type="number" min="1" max="100" placeholder="" class="form-control input-md" required >
    
  </div>
</div>
<center> <button type="submit"  class="btn btn-primary"><h3 style="color:#FFFFFF">Actualizar</button>
</fieldset>
</form>
''')



pagina.fin()
