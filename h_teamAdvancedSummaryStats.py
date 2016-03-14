import urllib2
import requests
from bs4 import BeautifulSoup

f = open('H_TeamSummaryAdvancedStatsOffense.csv', 'w')
f.write('TeamName,teamID,Games,Wins,Losses,WL%,SRS,SOS,ConfW,ConfL,HomeW,HomeL,AwayW,AwayL,PtsFor,PtsAgt,Pace,ORtg,FTr,_3PAr,TRBpct,ASTpct,STLpct,BLKpct,eFGpct,TOVpct,ORBpct,FTFGA' + '\n')

r=requests.get('http://www.sports-reference.com/cbb/seasons/2016-advanced-school-stats.html')

print "Getting data..."
url = "http://www.sports-reference.com/cbb/seasons/2016-advanced-school-stats.html"
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
		#advancedStats
		Pace = row.findAll('td')[17].string
		ORtg = row.findAll('td')[18].string
		FTr = row.findAll('td')[19].string
		_3PAr = row.findAll('td')[20].string
		TRBpct = row.findAll('td')[22].string
		ASTpct = row.findAll('td')[23].string
		STLpct = row.findAll('td')[24].string
		BLKpct = row.findAll('td')[25].string
		eFGpct = row.findAll('td')[26].string
		TOVpct = row.findAll('td')[27].string
		ORBpct = row.findAll('td')[28].string
		FTFGA = row.findAll('td')[29].string
		print(name, Wins, Losses)
		f.write(name + ',' + href + ',' + Games + ','+ Wins + ',' + Losses + ',' + WLpct + ',' + SRS + ',' + SOS + ',' + ConfW + ',' + ConfL + ',' + HomeW + ',' + HomeL + ',' + AwayW + ',' + AwayL + ',' + PtsFor + ',' + PtsAgt + ',' + Pace + ',' + ORtg + ',' + FTr + ',' + _3PAr + ',' + TRBpct + ',' + ASTpct + ',' + STLpct + ',' + BLKpct + ',' + eFGpct + ',' + TOVpct + ',' + ORBpct + ',' + FTFGA + '\n')


f.close()
