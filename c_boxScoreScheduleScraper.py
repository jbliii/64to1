#iterates through calendar and pulls addresses of box score pages so that scraper d can pull player level data

import requests
from bs4 import BeautifulSoup
f = open('C_brefBoxScores_NCAA.csv', 'w')
f.write('URL'+'\n')

#Iterate through months and day
for y in range(2015,2016):
	for m in range(10,13):
		for d in range(1,32):

		#Check if already gone through month
			if (m == 2 and d > 28):
				break
			elif (m in [4, 6, 9, 11] and d > 30):
				break

			#Open scoreboard
			timestamp = str(y) + str(m) + str(d)
			print "Getting data for " + timestamp
			url = "http://www.sports-reference.com/cbb/boxscores/index.cgi?month=" + str(m) + "&day=" + str(d) + "&year=" + str(y)
			page = requests.get(url)

			soup = BeautifulSoup(page.text, 'html.parser')
	  
			for tag in soup.findAll(lambda tag: (tag.name =='a' and tag.text == 'Final'), href=True):
				f.write(tag['href']+'\n')
				print tag['href']
				
for y in range(2016,2017):
	for m in range(1,5):
		for d in range(1,32):

		#Check if already gone through month
			if (m == 2 and d > 28):
				break
			elif (m in [4, 6, 9, 11] and d > 30):
				break
			elif (y == 2016 and m > 4):
				break

			#Open scoreboard
			timestamp = str(y) + str(m) + str(d)
			print "Getting data for " + timestamp
			url = "http://www.sports-reference.com/cbb/boxscores/index.cgi?month=" + str(m) + "&day=" + str(d) + "&year=" + str(y)
			page = requests.get(url)

			soup = BeautifulSoup(page.text, 'html.parser')
	  
			for tag in soup.findAll(lambda tag: (tag.name =='a' and tag.text == 'Final'), href=True):
				f.write(tag['href']+'\n')
				print tag['href']
				
f.close()
