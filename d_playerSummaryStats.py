#pulls summary data on every player from team pages

import requests
import csv
from bs4 import BeautifulSoup

f = open('D_brefPlayerSummaryStats.csv', 'w')
f.write('Team,RankPts,Name,GamesPlayed,Minutes,FGM,FGA,FGpct,FG2PM,FG2PA,FG3PM,FG3PA,FG3pct,FTM,FTA,FTpct,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS' + '\n')

with open('teamList_2016.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	next(csvreader)

	#Open season summary pages for each team in the for loop
	for teamPage in csvreader:
		print "Getting data for " + str(teamPage[0])
		url = "http://www.sports-reference.com/cbb/schools/" + str(teamPage[0]) + "/2016.html"
		page = requests.get(url)

		soup = BeautifulSoup(page.text, 'html.parser')
		tableRoster = soup.find('table', id="totals")
		
		rows = tableRoster.findAll('tr')[1:]
		
		
		for row in rows:
			teamRankPts = row.findAll('td')[0].string
			name = row.findAll('td')[1].get_text().replace(',','')
			href = row.findAll('td')[1].find('a')
			GamesPlayed = row.findAll('td')[2].string
			Minutes = row.findAll('td')[3].string
			FGMVal = row.findAll('td')[4].string
			if FGMVal is None:
				FGM = '0'
			else:
				FGM = FGMVal
			FGAVal = row.findAll('td')[5].string
			if FGAVal is None:
				FGA = '0'
			else:
				FGA = FGAVal
			FGpctVal = row.findAll('td')[6].string
			if FGpctVal is None:
				FGpct = '0'
			else:
				FGpct = FGpctVal
			FG2PMVal = row.findAll('td')[7].string
			if FG2PMVal is None:
				FG2PM = '0'
			else:
				FG2PM = FG2PMVal
			FG2PAVal = row.findAll('td')[8].string
			if FG2PAVal is None:
				FG2PA = '0'
			else:
				FG2PA = FG2PAVal
			FG3PMVal = row.findAll('td')[10].string
			if FG3PMVal is None:
				FG3PM = '0'
			else:
				FG3PM = FG3PMVal
			FG3PAVal = row.findAll('td')[11].string
			if FG3PAVal is None:
				FG3PA = '0'
			else:
				FG3PA = FG3PAVal
			FG3pctVal = row.findAll('td')[12].string
			if FG3pctVal is None:
				FG3pct = '0'
			else:
				FG3pct = FG3pctVal
			FTMVal = row.findAll('td')[13].string
			if FTMVal is None:
				FTM = '0'
			else:
				FTM = FTMVal
			FTAVal = row.findAll('td')[14].string
			if FTAVal is None:
				FTA = '0'
			else:
				FTA = FTAVal
			FTpctVal = row.findAll('td')[15].string
			if FTpctVal is None:
				FTpct = '0'
			else:
				FTpct = FTpctVal
			ORBVal = row.findAll('td')[16].string
			if ORBVal is None:
				ORB = '0'
			else:
				ORB = ORBVal
			DRBVal = row.findAll('td')[17].string
			if DRBVal is None:
				DRB = '0'
			else:
				DRB = DRBVal
			TRBVal = row.findAll('td')[18].string
			if TRBVal is None:
				TRB = '0'
			else:
				TRB = TRBVal
			ASTVal = row.findAll('td')[19].string
			if ASTVal is None:
				AST = '0'
			else:
				AST = ASTVal
			STLVal = row.findAll('td')[20].string
			if STLVal is None:
				STL = '0'
			else:
				STL = STLVal
			BLKVal = row.findAll('td')[21].string
			if BLKVal is None:
				BLK = '0'
			else:
				BLK = BLKVal
			TOVVal = row.findAll('td')[22].string
			if TOVVal is None:
				TOV = '0'
			else:
				TOV = TOVVal
			PFVal = row.findAll('td')[23].string
			if PFVal is None:
				PF = '0'
			else:
				PF = PFVal
			PTSVal = row.findAll('td')[24].string
			if PTSVal is None:
				PTS = '0'
			else:
				PTS = PTSVal

			f.write(str(teamPage[0]) + ',' + teamRankPts + ',' + name + ',' + 
			GamesPlayed + ','  + Minutes + ','  + FGM + ','  + FGA + ','  + FGpct + ',' +
			FG2PM + ','  + FG2PA + ','  + FG3PM + ',' + FG3PA + ','  + FG3pct + ','  + FTM + ',' +
			FTA + ','  + FTpct + ','  + ORB + ',' + DRB + ','  + TRB + ','  + AST + ',' +
			STL + ','  + BLK + ',' + TOV + ','  + PF + ',' + PTS +
			'\n')

		
			
		  
	f.close()
