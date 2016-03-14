#Iterates through school list and creates a csv of all the teams with a valid season played in 2016

import urllib2
import requests
import re
from bs4 import BeautifulSoup

f = open('teamList_2016.csv', 'w')
f.write('TeamAddress,TeamName' + '\n')
Rk = re.compile('Rk')

print "Getting data..."
url = "http://www.sports-reference.com/cbb/schools"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

bigTable = soup.find('table', id="schools")

dataRows = bigTable.findAll('tr', class_="")[1:]


for row in dataRows:
	if row.next_element.string == Rk:
		pass
	elif int(row.findAll('td')[4].contents[0]) < 2016:
		pass
	else:
		Team = row.findAll('td')[1].a.contents[0]
		teamHref = row.findAll('td')[1].a['href'].replace('/cbb/schools/','').replace('/','')
		print(teamHref + "," + Team)
		f.write(teamHref + "," + Team + '\n')
	
f.close()


