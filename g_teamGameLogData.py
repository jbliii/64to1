#pulls basic and advanced gamelog data for every game by every team

import requests
import csv
from bs4 import BeautifulSoup

f = open('G_TeamGameLogStats_Basic.csv', 'w')
g = open('G_TeamGameLogStats_Advanced.csv', 'w')

f.write('teamID,boxID,date,opponentID,TeamPTS,OppPts,FGM,FGA,_3PM,_3PA,FTM,FTA,ORB,TRB,AST,STL,BLK,TOV,PF,OppFGM,OppFGA,Opp3PM,Opp3PA,OppFTM,OppFTA,OppORB,OppTRB,OppAST,OppSTL,OppBLK,OppTOV,OppPF,location' + '\n')
g.write('teamID,boxID,date,opponentID,TeamPts,OppPts,ORtg,DRtg,Pace,FTAtmpRt,_3PAtmpRt,TRB_pct,AST_pct,STL_pct,BLK_pct,OFF_eFG,OFF_TOV,OFF_ORB,OFF_FTFG,DEF_eFG,DEF_TOV,DEF_DRB,DEF_FTFG,location' + '\n')


with open('teamList_2016.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	next(csvreader)

	#Open gamelogs for every team
	for teamPage in csvreader:
		print "Getting data for " + str(teamPage[0])
		url = "http://www.sports-reference.com/cbb/schools/" + str(teamPage[0]) + "/2016-gamelogs.html"
		page = requests.get(url)
		soup = BeautifulSoup(page.text, 'html.parser')

		StatTable1 = soup.find('table', id="stats_basic")
		StatTable2 = soup.find('table', id="stats_advanced")

		rows1 = StatTable1.find('tbody').findAll('tr')
		rows2 = StatTable2.find('tbody').findAll('tr')
		
		for row in rows1:
			classtag = row.get('class')
			if 'thead' in classtag or 'thead over_header' in classtag:
				continue
			else:
				TeamID = str(teamPage[0])
				boxID = row.findAll('td')[2].a['href']
				date_ = row.findAll('td')[2].find('a').get_text()
				opponentID = row.findAll('td')[4].a['href'].replace('/cbb/schools/','').replace('2016.html','').replace('/','')
				TeamPts = row.findAll('td')[6].string
				OppPts = row.findAll('td')[7].string
				FGM = row.findAll('td')[8].string
				FGA = row.findAll('td')[9].string
				_3PM = row.findAll('td')[11].string 
				_3PA = row.findAll('td')[12].string
				FTM = row.findAll('td')[14].string
				FTA = row.findAll('td')[15].string
				ORB = row.findAll('td')[17].string
				TRB = row.findAll('td')[18].string
				AST = row.findAll('td')[19].string
				STL = row.findAll('td')[20].string
				BLK = row.findAll('td')[21].string
				TOV = row.findAll('td')[22].string
				PF = row.findAll('td')[23].string
				OppFGM = row.findAll('td')[25].string
				OppFGA = row.findAll('td')[26].string
				Opp3PM = row.findAll('td')[28].string
				Opp3PA = row.findAll('td')[29].string
				OppFTM = row.findAll('td')[31].string
				OppFTA = row.findAll('td')[32].string
				OppORB = row.findAll('td')[34].string
				OppTRB = row.findAll('td')[35].string
				OppAST = row.findAll('td')[36].string
				OppSTL = row.findAll('td')[37].string
				OppBLK = row.findAll('td')[38].string
				OppTOV = row.findAll('td')[39].string
				OppPF = row.findAll('td')[40].string
				if row.findAll('td')[3].string is None:
					location = 'Home'
				else:
					location = 'Away'
			
			f.write(TeamID + ',' + boxID + ',' + date_ + ',' + opponentID + ',' + TeamPts + ',' + OppPts + ',' + FGM + ',' + FGA + ',' + _3PM + 
			',' + _3PA + ',' + FTM + ',' + FTA + ',' + ORB + ',' + TRB + ',' + AST + ',' + STL + ',' + BLK + ',' + TOV + ',' + PF + ',' + 
			OppFGM + ',' + OppFGA + ',' + Opp3PM + ',' + Opp3PA + ',' + OppFTM + ',' + OppFTA + ',' + OppORB + ',' + OppTRB + ',' + OppAST + 
			',' + OppSTL + ',' + OppBLK + ',' + OppTOV + ',' + OppPF + ',' + location + '\n')
			
		for row in rows2:
			classtag = row.get('class')
			if 'thead' in classtag or 'thead over_header' in classtag:
				continue
			else:
				TeamID = str(teamPage[0])
				boxID = row.findAll('td')[2].a['href']
				date_ = row.findAll('td')[2].find('a').get_text()
				opponentID = row.findAll('td')[4].a['href'].replace('/cbb/schools/','').replace('2016.html','').replace('/','')
				TeamPts = row.findAll('td')[6].string
				OppPts = row.findAll('td')[7].string
				ORtg = row.findAll('td')[8].string
				DRtg = row.findAll('td')[9].string
				Pace = row.findAll('td')[10].string 
				FTAtmpRt = row.findAll('td')[11].string
				_3PAtmpRt = row.findAll('td')[12].string
				TRB_pct = row.findAll('td')[14].string
				AST_pct = row.findAll('td')[15].string
				STL_pct = row.findAll('td')[16].string
				BLK_pct = row.findAll('td')[17].string
				OFF_eFG = row.findAll('td')[19].string
				OFF_TOV = row.findAll('td')[20].string
				OFF_ORB = row.findAll('td')[21].string
				OFF_FTFG = row.findAll('td')[22].string
				DEF_eFG = row.findAll('td')[24].string
				DEF_TOV = row.findAll('td')[25].string
				DEF_DRB = row.findAll('td')[26].string
				DEF_FTFG = row.findAll('td')[27].string
				if row.findAll('td')[3].string is None:
					location = 'Home'
				else:
					location = 'Away'
			g.write(TeamID +  ',' + boxID + ',' + date_ + ',' + opponentID + ',' + TeamPts + ',' + OppPts + ',' + ORtg + ',' + DRtg + ',' + Pace + 
			',' + FTAtmpRt + ',' + _3PAtmpRt + ',' + TRB_pct + ',' + AST_pct + ',' + STL_pct + ',' + BLK_pct + ',' + OFF_eFG + ',' + OFF_TOV + 
			',' + OFF_ORB + ',' + OFF_FTFG + ',' + DEF_eFG + ',' + DEF_TOV + ',' + DEF_DRB + ',' + DEF_FTFG + ',' + location + '\n')
			  
f.close()
