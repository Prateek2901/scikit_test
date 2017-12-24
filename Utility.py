from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys
sys.setrecursionlimit(10000)

def genData(keys,url):
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	f = open(keys+".csv","w")
	page_soup = soup(page_html,'lxml')
	for tbl in page_soup.findAll("table"):
		for container in tbl.findAll("tr"):
			data = []
			for row in container.findAll("td"):
				if '|' not in row.text :		
					data.append(row.text.strip())
			if len(data) != 0:
				f.write(','.join(data) +"\n")
def makeCSVs():
    pages ={'actors':'https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/actors.html',
        'awtypes':'https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/awtypes.html',
        'casts':'https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/casts.html',
        'main':'https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/main.html'}
    for i,j in zip(pages.keys(),pages.values()):
        genData(i,j)