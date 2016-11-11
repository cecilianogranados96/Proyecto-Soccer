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
id = form.getfirst("id");
cur2.execute("SELECT * FROM fechas where id_fecha = '"+id+"'")
for row2 in cur2:
    row2 = row2
	

cur.execute("SELECT * FROM fechas where id_fecha = '"+id+"' and (id_equipo1 = '"+str(row2[3])+"' or id_equipo2 = '"+str(row2[5])+"') ")
for row in cur:
    row = row

consulta = "SELECT * FROM jugadores  where id_equipo = '"+str(row2[3])+"' or id_equipo = '"+str(row2[5])+"' "
cur.execute(consulta)
s =[]
x =[]
for row2 in cur:
    s.append(row2[1]) 
for j in s:
	r = j.split()
	x.append(j)
	
print('''<div class="tg-banner2 tg-haslayout"></div>''')			
print('''
<script src="http://textextjs.com/js/jquery-1.8.2.js" type="text/javascript" charset="utf-8"></script>
<script src="http://textextjs.com/js/doc.js" type="text/javascript" charset="utf-8"></script>
<link rel="stylesheet" href="http://textextjs.com/textext/css/textext.core.css" type="text/css" />
<link rel="stylesheet" href="http://textextjs.com/textext/css/textext.plugin.tags.css" type="text/css" />
<link rel="stylesheet" href="http://textextjs.com/textext/css/textext.plugin.autocomplete.css" type="text/css" />
<link rel="stylesheet" href="http://textextjs.com/textext/css/textext.plugin.focus.css" type="text/css" />
<link rel="stylesheet" href="http://textextjs.com/textext/css/textext.plugin.prompt.css" type="text/css" />
<link rel="stylesheet" href="http://textextjs.com/textext/css/textext.plugin.arrow.css" type="text/css" />
<script src="http://textextjs.com/textext/js/textext.core.js" type="text/javascript" charset="utf-8"></script>
<script src="http://textextjs.com/textext/js/textext.plugin.tags.js" type="text/javascript" charset="utf-8"></script>
<script src="http://textextjs.com/textext/js/textext.plugin.autocomplete.js" type="text/javascript" charset="utf-8"></script>
<script src="http://textextjs.com/textext/js/textext.plugin.suggestions.js" type="text/javascript" charset="utf-8"></script>
<script src="http://textextjs.com/textext/js/textext.plugin.filter.js" type="text/javascript" charset="utf-8"></script>
<script src="http://textextjs.com/textext/js/textext.plugin.focus.js" type="text/javascript" charset="utf-8"></script>
<script src="http://textextjs.com/textext/js/textext.plugin.prompt.js" type="text/javascript" charset="utf-8"></script>
<script src="http://textextjs.com/textext/js/textext.plugin.ajax.js" type="text/javascript" charset="utf-8"></script>
<script src="http://textextjs.com/textext/js/textext.plugin.arrow.js" type="text/javascript" charset="utf-8"></script>
<style>
	.text-core .text-wrap .text-tags.text-tags-on-top {
    z-index: 2;
    margin-left: 215px;
}
.text-core .text-wrap .text-tags {
	margin-left: 215px;
}
.text-core .text-wrap .text-dropdown.text-position-below {
   margin-left: 215px;
}

</style>
	<br><br><br>
<h1 style="margin-top: 201px;"><center>Ver / Editar Juego</center></h1>	<br><br><br>	
<center>
<form class="form-horizontal" action="actualizar_juego.py?id='''+id+'''" method="GET">
<fieldset>
<input value="'''+str(id)+'''" name="id" type="hidden" hidden>
<table border="0">
<tr>
	<td>
		<table border="0">
			<tr>
				<td>
					Goles
				</td>
				<td>
					Equipo
				</td>
			</tr>
			<tr>
				<td>
				  <input value="'''+str(row[7])+'''" name="goles1" type="text" style="    width: 60px;" class="form-control input-md">
				</td>
				<td>
					<select id="equipo1" name="equipo" class="form-control">
						<option value="'''+str(row[3])+'''">'''+str(row[2])+'''</option>
					</select>
				</td>
			</tr>
		</table>
		Goleadores Actuales: '''+str(row[9])+'''
		<h3>Goleadores:
		<textarea id="textarea"  name="goleadores1" class="example" rows="1" style="    margin-left: 148px;" ></textarea>
	</td>
<td>
	<h1>VS</h1>
</td>
<td>
	<table border="0">
				<tr>
				<td>
					Equipo
				</td>
				<td>
					Goles
				</td>
			</tr>
	<tr>
	<td>
    <select id="equipo" name="equipo2" class="form-control">
		<option value="'''+str(row[5])+'''">'''+str(row[4])+'''</option>
    </select>
</td>
	<td><h1>
	 <input id="clasificados" len= "3" value="'''+str(row[8])+'''" name="goles2" type="text" style="width: 60px;" class="form-control input-md">
	</td>
	</tr>
	
	
</table>
		Goleadores Actuales: '''+str(row[10])+'''
		<h3>Goleadores:
		<textarea id="textarea2" name="goleadores2" class="example"  rows="1" style="margin-left: 148px;"></textarea>
</td>
</tr>
</table>
<script type="text/javascript">
    $('#textarea')
        .textext({
            plugins : 'tags autocomplete'
        })
        .bind('getSuggestions', function(e, data)
        {
            var list = '''+str(list(x))+''',
                textext = $(e.target).textext()[0],
                query = (data ? data.query : '') || ''
                ;

            $(this).trigger(
                'setSuggestions',
                { result : textext.itemManager().filter(list, query) }
            );
        });
</script>
<script type="text/javascript">
    $('#textarea2')
        .textext({
            plugins : 'tags autocomplete'
        })
        .bind('getSuggestions', function(e, data)
        {
            var list = '''+str(list(x))+''',
                textext = $(e.target).textext()[0],
                query = (data ? data.query : '') || ''
                ;

            $(this).trigger(
                'setSuggestions',
                { result : textext.itemManager().filter(list, query) }
            );
        });
</script>

<br><br><br><br>

<center> <button type="submit"  class="btn btn-primary"><h3 style="color:#FFFFFF">Actualizar</button>
</fieldset>

<br><br><br><br>
</form>

<br><br><br>
''')



pagina.fin()
