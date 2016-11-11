#! 

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='soccer')
cur = conn.cursor()

def equipos_header():
        cur.execute("SELECT * FROM equipos limit 10")
        x = ""
        for row in cur:
                x += ("<li><a href='jugadores.py?id="+str(row[0])+"'>"+row[1]+"</a></li>")
        return (x)
equipos_header()
		
	
	

