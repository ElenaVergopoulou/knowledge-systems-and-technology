import csv

string_ = "^^xsd:string."
integer_ = "^^xsd:integer."
bool_ = "^^xsd:boolean."

trip_idURI = "http://www.bob.com/trip"
trip_headsignURI = "http://www.bob.com/trip_headsign"
direction_idURI = "http://www.bob.com/direction_id"
block_idURI = "http://www.bob.com/block_id"
trips_has_routes="http://www.bob.com/trips_has_routes"
trips_has_calendar="http://www.bob.com/trips_has_calendar"
routesURI = "http://www.bob.com/routes"
calendarURI = "http://www.bob.com/calendar"

inputF_name = "trips.txt"
outputF_name = "trips_output.txt"
outputRF_name="trips_outputs_RF.txt"
output_F = open(outputF_name, "w")
outputRF=open(outputRF_name, "w")

i = 0
with open(inputF_name) as inF:
	for line in inF:
		i = i + 1
		row = line.split(",")
		route_id=row[0]
		service_id=row[1]
		trip_id= row[2]
		trip_headsign= row[3]
		direction_id = row[4]
		block_id = row[5]
		
		if(i>1):
		        

			output_F.write('<'+trip_idURI  +'/'+trip_id+'> ' + 'a' + ' <' +trip_idURI +'>'+'.'+'\n')
			output_F.write('<'+trip_idURI +'/'+trip_id+'> ' +'<' +trip_headsignURI +'>' +' "' +str(trip_headsign) +'"' + string_ +'\n')
			output_F.write('<'+trip_idURI +'/'+trip_id+'> ' +'<' +direction_idURI +'>' + ' "' +str(direction_id) + '"' + bool_ +'\n')
			output_F.write('<'+trip_idURI +'/'+trip_id+'> ' +'<' +block_idURI +'>' + ' "' +str(block_id) + '"' + integer_ +'\n')
			outputRF.write('<'+trip_idURI +'/'+trip_id+'> ' +'<' +trips_has_routes+'>' + ' <'+routesURI+'/'+route_id+'>.'+'\n')
			outputRF.write('<'+trip_idURI +'/'+trip_id+'> ' +'<' +trips_has_calendar+'>' + ' <'+calendarURI+'/'+service_id+'>.'+'\n')



	
		
print(i)
