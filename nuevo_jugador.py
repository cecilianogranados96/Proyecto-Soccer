#!../python35/python.exe
print ("Content-type: text/html\n")
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer',autocommit=True)
cur = conn.cursor()
nombre = form.getfirst("nombre");
posicion = form.getfirst("posicion");
equipo = form.getfirst("equipo");
numero = form.getfirst("numero");
import os


fileitem = form['img']
if fileitem.filename:
   fn = os.path.basename(fileitem.filename)
   open("images/player/" +fn, 'wb').write(fileitem.file.read())
   imagen = fn
else:
   imagen = "None"
   
   
print(nombre,posicion,equipo,numero)
sql = "INSERT INTO `jugadores`(`nombre_jugador`, `id_equipo`, `posicion`, `numero`,foto) VALUES ('"+str(nombre)+"','"+str(equipo)+"','"+str(posicion)+"','"+str(numero)+"','"+str(imagen)+"')"
cur.execute(sql)										
print('''<body><script type="text/javascript">window.location="admin_jugadores.py";</script></body>''')