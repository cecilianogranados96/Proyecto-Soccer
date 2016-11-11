#!../python35/python.exe
print ("Content-type: text/html\n")
from contructor import * 
import operator

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer',autocommit=True)
cur = conn.cursor()
cur1 = conn.cursor()
sql = "DELETE FROM `fechas`"
cur.execute(sql)
cur1.execute("UPDATE `general` SET `fecha`= 0 ")
print('''<body><script type="text/javascript">window.location="admin_equipos.py";</script></body>''')