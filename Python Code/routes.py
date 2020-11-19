import csv

string_ = "^^xsd:string."
integer_ = "^^xsd:integer."
float_ = "^^xsd:float."

routesURI = "http://www.bob.com/routes"
routes_short_nameURI = "http://www.bob.com/routes_short_nameURI"
routes_long_nameURI = "http://www.bob.com/routes_long_name"
routes_descURI = "http://www.bob.com/routes_desc"
routes_typeURI = "http://www.bob.com/routes_type"
routes_colorURI = "http://www.bob.com/routes_color"
routes_text_colorURI = "http://www.bob.com/routes_text_color"
underground_routeURI= "http://www.bob.com/underground_route"

inputF_name = "routes.txt"
outputF_name = "routes_output.txt"
output_F = open(outputF_name, "w")

i = 0
with open(inputF_name) as inF:
	for line in inF:
		i = i + 1
		row = line.split(",")
		routes_id = row[0]
		routes_short_name = row[1]
		routes_long_name = row[2]
		
		routes_type = row[4]
		routes_color = row[5]
		routes_text_color = row[6]
		
		if(i>1):
		
			output_F.write('<'+routesURI +'/'+routes_id+'> ' + 'a' + ' <' +routesURI +'>'+'.'+'\n')
			output_F.write('<'+routesURI +'/'+routes_id+'> ' +'<' +routes_short_nameURI +'>' +' "' +str(routes_short_name) +'"' + string_ +'\n')
			output_F.write('<'+routesURI +'/'+routes_id+'> ' +'<' +routes_long_nameURI +'>' +str(routes_long_name) + string_ +'\n')
			output_F.write('<'+routesURI +'/'+routes_id+'> ' +'<' +routes_typeURI +'> ' +'"'+str(routes_type) +'"'+ integer_ +'\n')	
			output_F.write('<'+routesURI +'/'+routes_id+'> ' +'<' +routes_colorURI +'> ' +'"'+str(routes_color) +'"'+ string_ +'\n')
			output_F.write('<'+routesURI +'/'+routes_id+'> ' +'<' +routes_text_colorURI +'>' +' "' +str(routes_text_color).rstrip() +' "' + string_ +'\n')
			if(routes_type=='1'):
				underground_route='1'
			else:
				underground_route='0'
			output_F.write('<'+routesURI +'/'+routes_id+'> ' +'<' +underground_routeURI+ '>'+' "' +str(underground_route) +' "'+ integer_ + '\n')




print(i)
