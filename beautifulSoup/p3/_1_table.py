import bs4 as bs
import urllib.request
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

#table = soup.table
table = soup.find('table') # soup.table and soup.find('table') same thing
#print(table)

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td ]
    print(row)
