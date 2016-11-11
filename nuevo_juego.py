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
sql = "INSERT INTO `equipos`(`nombre`, `lema`) VALUES ('"+nombre+"','"+lema+"')"
cur.execute(sql)										
print('''<body><script type="text/javascript">window.location="admin_equipos.py";</script></body>''')