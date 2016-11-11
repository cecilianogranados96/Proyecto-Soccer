#!../python35/python.exe
print ("Content-type: text/html\n")
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer',autocommit=True)
cur = conn.cursor()
nombre = form.getfirst("nombre");
lema = form.getfirst("lema");
clasificacion = form.getfirst("numero");
siglas = form.getfirst("siglas");
sql = "INSERT INTO `equipos`(`nombre`, `lema`,`clasificacion`,`siglas`) VALUES ('"+str(nombre)+"','"+str(lema)+"','"+str(clasificacion)+"','"+str(siglas)+"')"
#print(sql)
cur.execute(sql)										
print('''<body><script type="text/javascript">window.location="admin_equipos.py";</script></body>''')