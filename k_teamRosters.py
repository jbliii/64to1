import requests
import csv
from bs4 import BeautifulSoup

f = open('K_TeamRosters.csv', 'w')
f.write('Team,Name,Class_,Position,Height' + '\n')

with open('teamList_2016.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	next(csvreader)

	#Open team summary pages containing roster data
	for teamPage in csvreader:
		print "Getting data for " + str(teamPage[0])
		url = "http://www.sports-reference.com/cbb/schools/" + str(teamPage[0]) + "/2016.html"
		page = requests.get(url)

		soup = BeautifulSoup(page.text, 'html.parser')
		tableRoster = soup.find('table', id="roster")
		
		rows = tableRoster.findAll('tr')[1:]
		
		
		for row in rows:
			#scrub commas from players with suffixes, as this will cause issues with the csv
			name = row.findAll('td')[0].get_text().replace(',','')
			href = row.findAll('td')[0].find('a')
			YearVal = row.findAll('td')[2].string
			if YearVal is None:
				Year = 'NA'
			else:
				Year = YearVal
			Position = row.findAll('td')[3].string
			Height = row.findAll('td')[4].string
			
			f.write(str(teamPage[0]) + ',' + name + ',' + Year + ','  + Position + ','  + Height + 
			'\n')
		  
	f.close()
