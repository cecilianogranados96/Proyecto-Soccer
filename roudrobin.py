#!../python35/python.exe
print ("Content-type: text/html\n")
from contructor import * 
import operator

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer',autocommit=True)
cur = conn.cursor()
cur1 = conn.cursor()
cur2 = conn.cursor()
cur.execute("SELECT * FROM equipos where id != 0")
cur3 = conn.cursor()

s = []
for row in cur:				
	s.append(row[0])
def fixtures(teams):
    if len(teams) % 2:
        teams.append(0) #Dia extra 
    rotation = list(teams)
    fixtures = []
    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]
    return fixtures
matches = fixtures(s)
z = []
for f in matches:
	z.append(list(zip(*[iter(f)]*2)))
n_fecha = 0
sql = "DELETE FROM `fechas`"
cur.execute(sql)
for x in z:
	n_fecha += 1 
	for fechas in x:
		cur1.execute("SELECT * FROM equipos where id = '"+str(fechas[0])+"'")
		for row in cur1:
			row = row
		cur2.execute("SELECT * FROM equipos where id = '"+str(fechas[1])+"'")
		for row2 in cur2:
			row2 = row2
		print(n_fecha,fechas,row[1],row2[1])
		sql = "INSERT INTO `fechas`(`fecha`, `equipo1`, `id_equipo1`, `equipo2`, `id_equipo2`) VALUES ('"+str(n_fecha)+"','"+str(row[1])+"','"+str(fechas[0])+"','"+str(row2[1])+"','"+str(fechas[1])+"')"
		print(sql)
		cur.execute(sql)
cur3.execute("UPDATE `general` SET `fecha`= 1 ")
print('''<body><script type="text/javascript">window.location="fechas.py";</script></body>''')