#iterates through box score URLs pulled from scraper C and grabs all the player data from each game

import requests
import csv
from bs4 import BeautifulSoup

f = open('F_brefBoxScorePlayerData.csv', 'w')
f.write('boxID,Player,Team,HomeAway,Start-or-Bench,Minutes,FGM,FGA,FGM2p,FGA2p,FGM3p,FGA3p,FTM,FTA,ORB,DRB,TRB,AST,STL,BLK,TOV,FOUL,PTS' + '\n')

with open('C_brefBoxScores_NCAA.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	next(csvreader)
	
	for boxID in csvreader:
		#Open Box Score Page
		print "Getting data for " + str(boxID[0])
		url = "http://www.sports-reference.com" + str(boxID[0])
		page = requests.get(url)

		soup = BeautifulSoup(page.text, 'html.parser')
		TableTeamInfo = soup.find('table', class_="border_gray")
		StatTableAway = soup.findAll('table', class_="sortable  stats_table")[0]
		StatTableHome = soup.findAll('table', class_="sortable  stats_table")[2]
		homeTeamID = TableTeamInfo.findAll('td', class_="align_center padding")[1].a['href'].replace('/cbb/schools/','').replace('2016.html','').replace('/','')
		awayTeamID = TableTeamInfo.findAll('td', class_="align_center padding")[0].a['href'].replace('/cbb/schools/','').replace('2016.html','').replace('/','')
		
		AwayStarterRows = StatTableAway.findAll('tr')[2:7]
		AwayBenchRows = StatTableAway.findAll('tr')[9:]
		HomeStarterRows = StatTableHome.findAll('tr')[2:7]
		HomeBenchRows = StatTableHome.findAll('tr')[9:]

		for row in AwayStarterRows:
			name = row.findAll('td')[0].get_text()
			minutes = row.findAll('td')[1].string
			fgm = row.findAll('td')[2].string
			fga = row.findAll('td')[3].string
			fgm2p = row.findAll('td')[5].string
			fga2p = row.findAll('td')[6].string
			fgm3p = row.findAll('td')[8].string
			fga3p = row.findAll('td')[9].string
			ftm = row.findAll('td')[11].string
			fta = row.findAll('td')[12].string
			orb = row.findAll('td')[14].string
			drb = row.findAll('td')[15].string
			trb = row.findAll('td')[16].string
			ass = row.findAll('td')[17].string
			stl = row.findAll('td')[18].string
			blk = row.findAll('td')[19].string
			tov = row.findAll('td')[20].string
			foul = row.findAll('td')[21].string
			pts = row.findAll('td')[22].string
			
			f.write(str(boxID[0]) + ',' + name + ',' + awayTeamID + ',' + 'Away,Starter,' + minutes + ',' + fgm + ',' + fga + ',' + fgm2p + ',' + fga2p + ',' + fgm3p + ',' + fga3p + ',' + ftm + ',' + fta + ',' + orb + ',' + drb + ',' + trb + ',' + ass + ',' + stl + ',' + blk + ',' + tov + ',' + foul + ',' + pts + '\n')

		for row in AwayBenchRows:
			name = row.findAll('td')[0].get_text()
			minutes = row.findAll('td')[1].string
			fgm = row.findAll('td')[2].string
			fga = row.findAll('td')[3].string
			fgm2p = row.findAll('td')[5].string
			fga2p = row.findAll('td')[6].string
			fgm3p = row.findAll('td')[8].string
			fga3p = row.findAll('td')[9].string
			ftm = row.findAll('td')[11].string
			fta = row.findAll('td')[12].string
			orb = row.findAll('td')[14].string
			drb = row.findAll('td')[15].string
			trb = row.findAll('td')[16].string
			ass = row.findAll('td')[17].string
			stl = row.findAll('td')[18].string
			blk = row.findAll('td')[19].string
			tov = row.findAll('td')[20].string
			foul = row.findAll('td')[21].string
			pts = row.findAll('td')[22].string
			
			f.write(str(boxID[0]) + ',' + name + ',' + awayTeamID + ',' + 'Away,Bench,' + minutes + ',' + fgm + ',' + fga + ',' + fgm2p + ',' + fga2p + ',' + fgm3p + ',' + fga3p + ',' + ftm + ',' + fta + ',' + orb + ',' + drb + ',' + trb + ',' + ass + ',' + stl + ',' + blk + ',' + tov + ',' + foul + ',' + pts + '\n')	
			
		for row in HomeStarterRows:
			name = row.findAll('td')[0].get_text()
			minutes = row.findAll('td')[1].string
			fgm = row.findAll('td')[2].string
			fga = row.findAll('td')[3].string
			fgm2p = row.findAll('td')[5].string
			fga2p = row.findAll('td')[6].string
			fgm3p = row.findAll('td')[8].string
			fga3p = row.findAll('td')[9].string
			ftm = row.findAll('td')[11].string
			fta = row.findAll('td')[12].string
			orb = row.findAll('td')[14].string
			drb = row.findAll('td')[15].string
			trb = row.findAll('td')[16].string
			ass = row.findAll('td')[17].string
			stl = row.findAll('td')[18].string
			blk = row.findAll('td')[19].string
			tov = row.findAll('td')[20].string
			foul = row.findAll('td')[21].string
			pts = row.findAll('td')[22].string
			
			f.write(str(boxID[0]) + ',' + name + ',' + homeTeamID + ',' + 'Home,Starter,' + minutes + ',' + fgm + ',' + fga + ',' + fgm2p + ',' + fga2p + ',' + fgm3p + ',' + fga3p + ',' + ftm + ',' + fta + ',' + orb + ',' + drb + ',' + trb + ',' + ass + ',' + stl + ',' + blk + ',' + tov + ',' + foul + ',' + pts + '\n')			

		for row in HomeBenchRows:
			name = row.findAll('td')[0].get_text()
			minutes = row.findAll('td')[1].string
			fgm = row.findAll('td')[2].string
			fga = row.findAll('td')[3].string
			fgm2p = row.findAll('td')[5].string
			fga2p = row.findAll('td')[6].string
			fgm3p = row.findAll('td')[8].string
			fga3p = row.findAll('td')[9].string
			ftm = row.findAll('td')[11].string
			fta = row.findAll('td')[12].string
			orb = row.findAll('td')[14].string
			drb = row.findAll('td')[15].string
			trb = row.findAll('td')[16].string
			ass = row.findAll('td')[17].string
			stl = row.findAll('td')[18].string
			blk = row.findAll('td')[19].string
			tov = row.findAll('td')[20].string
			foul = row.findAll('td')[21].string
			pts = row.findAll('td')[22].string
			
			f.write(str(boxID[0]) + ',' + name + ',' + homeTeamID + ',' + 'Home,Bench,' + minutes + ',' + fgm + ',' + fga + ',' + fgm2p + ',' + fga2p + ',' + fgm3p + ',' + fga3p + ',' + ftm + ',' + fta + ',' + orb + ',' + drb + ',' + trb + ',' + ass + ',' + stl + ',' + blk + ',' + tov + ',' + foul + ',' + pts + '\n')				
		  
	f.close()
