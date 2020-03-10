import bs4 as bs
import urllib.request
#C:/Users/User/Desktop/Day1/indexHK.html
#This is work
# f = urllib2.urlopen(r'file:///c|\mypage.html')
#sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
sauce = urllib.request.urlopen(r'file:///C:/Users/User/Desktop/Day1/indexHK.html').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

'''
#table = soup.table
table = soup.find('table') # soup.table and soup.find('table') same thing
#print(table)

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td ]
    print(row)'''
