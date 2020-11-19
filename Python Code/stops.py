import csv

string_ = "^^xsd:string."
integer_ = "^^xsd:integer."
float_ = "^^xsd:float."

latitude = "https://www.w3.org/2003/01/geo/wgs84_pos#lat"
longitude = "https://www.w3.org/2003/01/geo/wgs84_pos#long"

stop_idURI = "http://www.bob.com/stops"
stop_codeURI = "http://www.bob.com/stop_code"
stop_nameURI = "http://www.bob.com/stop_name"
stop_descURI = "http://www.bob.com/stop_desc"
stop_latURI = "http://www.bob.com/stop_latitude"
stop_longURI = "http://www.bob.com/stop_longitute"
location_typeURI = "http://www.bob.com/location_type"

inputF_name = "stops.txt"
outputF_name = "stops_output.txt"
output_F = open(outputF_name, "w")

i = 0
with open(inputF_name) as inF:
	for line in inF:
		i = i + 1
		row = line.split(",")
		stop_id = row[0]
		stop_code = row[1]
		stop_name = row[2]
		stop_desc = row[3]
		stop_lat = row[4]
		stop_lon = row[5]
		location_type = row[6]
		
		if(i>0):
		
			output_F.write('<'+stop_idURI +'/'+stop_id+'> ' + 'a' + ' <' +stop_idURI +'>'+'.'+'\n')
			output_F.write('<'+stop_idURI +'/'+stop_id+'> ' +'<' +stop_codeURI +' "' +str(stop_code) +' "' + integer_ +'\n')
			output_F.write('<'+stop_idURI +'/'+stop_id+'> ' +'<' +stop_nameURI +'> ' +str(stop_name)+ string_ +'\n')	
			output_F.write('<'+stop_idURI +'/'+stop_id+'> ' +'<' +stop_descURI +'>' + ' "' +str(stop_desc) +' "' + string_ +'\n')	
		
			output_F.write('<'+stop_idURI +'/'+stop_id+'> ' +'<' +latitude + '>' + '"' +str(stop_lat) +' "' +'\n')	
			output_F.write('<'+stop_idURI +'/'+stop_id+'> ' +'<' +longitude + '>' +' "' + str(stop_lon) +' "' +'\n')	
			
			output_F.write('<'+stop_idURI +'/'+stop_id+'> ' +'<' +location_typeURI +'>' +' "' +str(location_type).rstrip() +' "' + integer_ +'\n')
		
print(i)
