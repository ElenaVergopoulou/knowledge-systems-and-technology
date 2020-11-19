import csv
from datetime import datetime

string_ = "^^xsd:string."
integer_ = "^^xsd:integer."
time_ = "^^xsd:dateTime."

stop_timesURI = "http://www.bob.com/stop_times"
tripURI = "http://www.bob.com/trip_id"
trip_id_URI="http://www.bob.com/trips"
stop_id_URI="http://www.bob.com/stops"
arrival_timeURI = "http://www.bob.com/arrival_time"
departure_timeURI = "http://www.bob.com/departure_time"
stop_idURI = "http://www.bob.com/stop_id"
stop_sequenceURI = "http://www.bob.com/stop_sequence"
pickup_typeURI = "http://www.bob.com/pickup_type"
drop_off_typeURI = "http://www.bob.com/drop_off_type"
stop_times_has_trips= "http://www.bob.com/stop_times_has_trips"
stop_times_has_stops= "http://www.bob.com/stop_times_has_stops"


inputF_name = "stop_times.txt"
outputF_name = "stop_times_output.txt"
outputRF_name="stoptimes_outputs_RF.txt"
output_F = open(outputF_name, "w")
outputRF=open(outputRF_name, "w")

i = 0
with open(inputF_name) as inF:
	for line in inF:
		i = i + 1
		row = line.split(",")
		trip_id = row[0]
		arrival_time = row[1]
		departure_time = row[2]
		stop_id = row[3]
		stop_sequence= row[4]
		pickup_type = row[5]
		drop_off_type = row[6]
		
		if(i>1):
		
			output_F.write('<http://www.bob.com/trips/' +trip_id+'/stops/'+stop_id+'> ' + 'a' + ' <' +stop_timesURI +'>'+'.'+'\n')
			output_F.write('<http://www.bob.com/trips/' +trip_id+'/stops/'+stop_id+'> ' + '<'+ arrival_timeURI + '>' +' "' + str(arrival_time)+ '"' + time_ + '\n')	
			output_F.write('<http://www.bob.com/trips/' +trip_id+'/stops/'+stop_id+'> ' + '<'+ departure_timeURI + '>' +' "' + str(departure_time)+ '"' + time_ + '\n')	
			output_F.write('<http://www.bob.com/trips/' +trip_id+'/stops/'+stop_id+'> ' + '<'+ stop_sequenceURI + '>' +' "' + str(stop_sequence)+ '"' + integer_ + '\n')
			output_F.write('<http://www.bob.com/trips/' +trip_id+'/stops/'+stop_id+'> ' + '<'+ pickup_typeURI + '>' +' "' + str(pickup_type)+ '"' + integer_ + '\n')		
			output_F.write('<http://www.bob.com/trips/' +trip_id+'/stops/'+stop_id+'> ' + '<'+ drop_off_typeURI + '>' +' "' + str(drop_off_type).rstrip()+ '"' + integer_ + '\n')		
			outputRF.write('<http://www.bob.com/trips/' +trip_id+'/stops/'+stop_id+'> ' + '<'+ stop_times_has_trips + '>' + ' <'+trip_id_URI+'/'+trip_id+'>.'+'\n')
			outputRF.write('<http://www.bob.com/trips/' +trip_id+'/stops/'+stop_id+'> ' + '<'+ stop_times_has_stops + '>' + ' <'+stop_id_URI+'/'+stop_id+'>.'+'\n')
		

		
print(i)
