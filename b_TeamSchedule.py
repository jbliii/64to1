#Opens team list created in teamScraper.py and iterates through schedule pages, grabbing basic data about games played.

import requests
import csv
from bs4 import BeautifulSoup

f = open('B_NCAA_TeamSchedules_2016.csv', 'w')
f.write('Team,boxID,Game#,Date,Opponent,Conf,Result,PtsFor,PtsAgnst,OT,W,L,Streak' + '\n')

with open('teamList_2016.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	next(csvreader)

	for teamPage in csvreader:
		#Open Box Score Page
		print "Getting data for " + str(teamPage[0])
		url = "http://www.sports-reference.com/cbb/schools/" + str(teamPage[0]) + "/2016-schedule.html"
		page = requests.get(url)

		soup = BeautifulSoup(page.text, 'html.parser')
		tableSchedule = soup.find('table', id="schedule")
		
		rows = tableSchedule.findAll('tr', class_="")[1:]
		
		
		for row in rows:
			Game = row.findAll('td')[0].string
			boxIDVal = row.findAll('td')[1].find('a')
			if boxIDVal is None:
				boxID = 'Null'
			else: 
				boxID = row.findAll('td')[1].a['href']
			Date = row.findAll('td')[1].get_text().replace(',','')
			OpponentVal = row.findAll('td')[6]
			if OpponentVal.a is None:
				Opponent=OpponentVal.string
			else:
				Opponent=OpponentVal.a.contents[0] 
			if row.findAll('td')[7].get_text() is None:
				OppConf = 'Null'
			else:
				OppConf = row.findAll('td')[7].get_text()
			ResultVal = row.findAll('td')[8].string
			if ResultVal is None:
				Result = 'Null'
			else:
				Result = ResultVal
			PtsForVal = row.findAll('td')[9].string
			if PtsForVal is None:
				PtsFor = 'Null'
			else:
				PtsFor = PtsForVal
			PtsAgainstVal = row.findAll('td')[10].string
			if PtsAgainstVal is None:
				PtsAgainst = 'Null'
			else:
				PtsAgainst = PtsAgainstVal
			OTVal = row.findAll('td')[11].string
			if OTVal is None:
				OT = 'Null'
			else:
				OT = OTVal
			WinsVal = row.findAll('td')[12].string
			if WinsVal is None:
				Wins = 'Null'
			else:
				Wins = WinsVal
			LossesVal = row.findAll('td')[13].string
			if LossesVal is None:
				Losses = 'Null'
			else:
				Losses = LossesVal
			StreakVal = row.findAll('td')[14].string
			if StreakVal is None:
				Streak = 'Null'
			else:
				Streak = StreakVal


			f.write(str(teamPage[0]) + ',' + boxID + ',' + Game + ',' + Date + ',' + 
			Opponent + ','  + OppConf + ',' + 
			Result + ','  + PtsFor + ','  + PtsAgainst + ',' +
			OT + ','  + Wins + ','  + Losses + ',' + Streak + '\n')

	
		
	  
f.close()
