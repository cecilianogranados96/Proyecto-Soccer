#!../python35/python.exe
print ("Content-type: text/html\n")
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer',autocommit=True)
cur = conn.cursor()
cur1 = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()
cur4 = conn.cursor()
goles1 = form.getfirst("goles1");
goles2 = form.getfirst("goles2");
goleadores1 = form.getfirst("goleadores1");
goleadores2 = form.getfirst("goleadores2");
id = form.getfirst("id");
gol1 = ""
s = 0 
cur.execute("DELETE FROM `goles` WHERE `id_juego`  = "+str(id)+" ")
for x in goleadores1.split(","):
        s += 1
        nombre = x.replace('"',"").replace(']',"").replace('[',"")
        cur3.execute("SELECT id_jugador,nombre_jugador FROM `jugadores` WHERE `nombre_jugador` LIKE '%"+nombre+"%' ")
        for j in cur3:
                j = j
        #print(j)
        gol1 += "<li>"+nombre+"</li>"
        cur.execute("INSERT INTO `goles`(`id_jugador`, `id_juego`) VALUES ("+str(j[0])+","+str(id)+")") 
                
print("Goles",gol1,"Registrados",s)


if int(goles1) > int(s):
        print("<script>alert('Error con el numero de goleadores');window.location='juego.py?id="+str(id)+"';</script>")

gol2 = ""
r = 0
for x in goleadores2.split(","):
        r += 1
        nombre = x.replace('"',"").replace(']',"").replace('[',"")
        cur3.execute("SELECT id_jugador,nombre_jugador FROM `jugadores` WHERE `nombre_jugador` LIKE '%"+nombre+"%' ")
        for j in cur3:
                j = j
        #print(j)
        gol2 += "<li>"+nombre+"</li>"
        cur.execute("INSERT INTO `goles`(`id_jugador`, `id_juego`) VALUES ("+str(j[0])+","+str(id)+")") 

print(goles2,r)
if int(goles2) > int(r):
	print("<script>alert('Error con el numero de goleadores');window.location='juego.py?id="+str(id)+"';</script>")



print(goles1,goles2)
if int(goles1) < int(goles2):
        #GANO 2
        n = int(goles2)-(int(goles2)*2)
        sql = "UPDATE `fechas` SET `gol_equipo1`='"+str(goles1)+"',`gol_equipo2`='"+str(goles2)+"',`anotadores1`='"+str(gol1)+"',`anotadores2`='"+str(gol2)+"',estado=1, gano= id_equipo2, perdio= id_equipo1, gol_gano = '"+str(goles2)+"', gol_perdio= '"+str(n)+"'  WHERE id_fecha = '"+str(id)+"' "
if(int(goles1) > int(goles2)):
                #GANO1
        n = int(goles1)-(int(goles1)*2)
        sql = "UPDATE `fechas` SET `gol_equipo1`='"+str(goles1)+"',`gol_equipo2`='"+str(goles2)+"',`anotadores1`='"+str(gol1)+"',`anotadores2`='"+str(gol2)+"',estado=1, gano= id_equipo1, perdio= id_equipo2, gol_gano = '"+str(goles1)+"', gol_perdio= '"+str(n)+"'  WHERE id_fecha = '"+str(id)+"' "
if int(goles1) == int(goles2):
        #Empate
        sql = "UPDATE `fechas` SET `gol_equipo1`='"+str(goles1)+"',`gol_equipo2`='"+str(goles2)+"',`anotadores1`='"+str(gol1)+"',`anotadores2`='"+str(gol2)+"',estado=1,gano=0, perdio= 0, empato = 1,gol_gano = "+str(goles1)+", gol_perdio="+str(goles1)+" WHERE id_fecha = '"+str(id)+"' "
#print(sql)



cur.execute(sql)        

print('''<body><script type="text/javascript">window.location="admin_juegos.py?id='''+str(id)+'''";</script></body>''')
