import csv

string_ = "^^xsd:string."
integer_ = "^^xsd:integer."
bool_ = "^^xsd:boolean."
date_ = "^^xsd:date."

calendarURI = "http://www.bob.com/calendar"
mondayURI = "http://www.bob.com/monday"
tuesdayURI = "http://www.bob.com/tuesday"
wednesdayURI = "http://www.bob.com/wednesday"
thursdayURI = "http://www.bob.com/thursday"
fridayURI = "http://www.bob.com/friday"
saturdayURI = "http://www.bob.com/saturday"
sundayURI = "http://www.bob.com/sunday"
start_dateURI = "http://www.bob.com/start_date"
end_dateURI = "http://wwww.bob.com/end_date"


inputF_name = "calendar.txt"
outputF_name = "calendar_output.txt"
output_F = open(outputF_name, "w")

i = 0
with open(inputF_name) as inF:
	for line in inF:
		i = i + 1
		row = line.split(",")
		service_id = row[0]
		monday = row[1]
		tuesday = row[2]
		wednesday = row[3]
		thursday = row[4]
		friday = row[5]
		saturday = row[6]
		sunday = row[7]
		temp1 = row[8]
		temp2 = row[9]
		
		start_date_pretty = str(temp1[6:8]+'/'+temp1[4:6]+'/' +temp1[0:4])		
		end_date_pretty = str(temp2[6:8]+'/'+temp2[4:6]+'/' +temp2[0:4])
		

		if(i>1):
		
			output_F.write('<'+calendarURI +'/'+service_id+'> ' + 'a' + ' <' +calendarURI +'>'+'.'+'\n')
			output_F.write('<'+calendarURI +'/'+service_id+'> ' +'<' + mondayURI +'>' +' "' +str(monday) +'"' + bool_ +'\n')
			output_F.write('<'+calendarURI +'/'+service_id+'> ' +'<' + tuesdayURI +'>' +' "' +str(tuesday) +'"' + bool_ +'\n')
			output_F.write('<'+calendarURI +'/'+service_id+'> ' +'<' + wednesdayURI +'>' +' "' +str(wednesday) +'"' + bool_ +'\n')
			output_F.write('<'+calendarURI +'/'+service_id+'> ' +'<' + thursdayURI +'>' +' "' +str(thursday) +'"' + bool_ +'\n')
			output_F.write('<'+calendarURI +'/'+service_id+'> ' +'<' + fridayURI +'>' +' "' +str(friday) +'"' + bool_ +'\n')
			output_F.write('<'+calendarURI +'/'+service_id+'> ' +'<' + saturdayURI +'>' +' "' +str(saturday) +'"' + bool_ +'\n')
			output_F.write('<'+calendarURI +'/'+service_id+'> ' +'<' + sundayURI +'>' +' "' +str(sunday) +'"' + bool_ +'\n')
			output_F.write('<'+calendarURI +'/'+service_id+'> ' +'<' + start_dateURI +'> ' +'"'+str(start_date_pretty) +'"'+ date_ +'\n')	
			output_F.write('<'+calendarURI +'/'+service_id+'> ' +'<' + end_dateURI +'> ' +'"'+str(end_date_pretty) +'"'+ date_ +'\n')	

	
		
print(i)
