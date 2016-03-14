#pulls summary info on every team a team played

import urllib2
import requests
from bs4 import BeautifulSoup

f = open('E_ncaaTeamOpponentInfo.csv', 'w')
f.write('TeamName,teamID,Games,Wins,Losses,WL%,SRS,SOS,ConfW,ConfL,HomeW,HomeL,AwayW,AwayL,PtsFor,PtsAgt,FGM,FGA,FG%,TPM,TPA,TP%,FTM,FTA,FT%,ORB,TRB,AST,STL,BLK,TOV,PF' + '\n')

r=requests.get('http://www.sports-reference.com/cbb/seasons/2016-opponent-stats.html')

print "Getting data..."
url = "http://www.sports-reference.com/cbb/seasons/2016-opponent-stats.html"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

tableTeamInfo = soup.find('table', class_="sortable  stats_table").find('tbody')

rows = tableTeamInfo.findAll('tr', class_="")


for row in rows:
	classtag = row.get('class')
	if 'thead' in classtag or 'thead over_header' in classtag:
		continue
	else:
		name = row.findAll('td')[1].get_text()
		href = row.findAll('td')[1].a['href'].replace('/cbb/schools/','').replace('2016.html','').replace('/','')
		Games = row.findAll('td')[2].string
		Wins = row.findAll('td')[3].string
		Losses = row.findAll('td')[4].string
		WLpct = row.findAll('td')[5].string
		SRS = row.findAll('td')[6].string
		SOS = row.findAll('td')[7].string
		ConfW = row.findAll('td')[8].string
		ConfL = row.findAll('td')[9].string
		HomeW = row.findAll('td')[10].string
		HomeL = row.findAll('td')[11].string
		AwayW = row.findAll('td')[12].string
		AwayL = row.findAll('td')[13].string
		PtsFor = row.findAll('td')[14].string
		PtsAgt = row.findAll('td')[15].string
		FGM = row.findAll('td')[17].string
		FGA = row.findAll('td')[18].string
		FGpct = row.findAll('td')[19].string
		ThreePM = row.findAll('td')[20].string
		ThreePA = row.findAll('td')[21].string
		ThreePpct = row.findAll('td')[22].string
		FTM = row.findAll('td')[23].string
		FTA = row.findAll('td')[24].string
		FTpct = row.findAll('td')[25].string
		ORB = row.findAll('td')[26].string
		TRB = row.findAll('td')[27].string
		AST = row.findAll('td')[28].string
		STL = row.findAll('td')[29].string
		BLK = row.findAll('td')[30].string
		TOV = row.findAll('td')[31].string
		PF = row.findAll('td')[32].string
		print(name, Wins, Losses)
		f.write(name + ',' + href + ',' + Games + ','+ Wins + ',' + Losses + ',' + WLpct + ',' + SRS + ',' + SOS + ',' + ConfW + ',' + ConfL + ',' + HomeW + ',' + HomeL + ',' + AwayW + ',' + AwayL + ',' + PtsFor + ',' + PtsAgt + ',' + FGM +',' + FGA +',' + FGpct + ',' + ThreePM + ',' + ThreePA + ',' + ThreePpct + ',' + FTM + ',' + FTA + ',' + FTpct + ',' + ORB + ',' + TRB + ',' + AST + ',' + STL + ',' + BLK + ',' + TOV + ',' + PF + '\n')


f.close()
