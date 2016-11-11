#!../python35/python.exe
print ("Content-type: text/html\n")
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer',autocommit=True)
cur = conn.cursor()
borrar = form.getfirst("borrar");
sql = "DELETE FROM `jugadores` WHERE `id_jugador` = '"+str(borrar)+"'"
cur.execute(sql)										
print('''<body><script type="text/javascript">window.location="admin_jugadores.py";</script></body>''')