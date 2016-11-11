#!../python35/python.exe
print ("Content-type: text/html\n")
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer',autocommit=True)
cur = conn.cursor()


nombre = form.getfirst("nombre");
clasificados = form.getfirst("clasificados");

equipos = form.getfirst("equipos");
empatado = form.getfirst("empatado");
ganado = form.getfirst("ganado");


#print(goles1,goles2,goleadores1,goleadores2)
sql = "UPDATE `general` SET `nombre_torneo`='"+str(nombre)+"',`equipos_participan`='"+str(equipos)+"',`equipos_clasifican`='"+str(clasificados)+"',`puntos_p_ganado`='"+str(ganado)+"',`puntos_p_empatado`='"+str(empatado)+"' "
#print (sql)
cur.execute(sql)										
print('''<body><script type="text/javascript">window.location="admin_general.py?id='''+str(id)+'''";</script></body>''')