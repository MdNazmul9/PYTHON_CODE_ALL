import bs4 as bs
import urllib.request
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
#print(soup.title)

#print(soup.tr.text)
#print(soup.td)
"""print(*soup.td)
print(soup.find_all('td'))

for TR in soup.find_all('tr'):
    print(TR.text)

print(soup.text)
"""
# pip install beautifulsoup4
#pip install lxml
for url in soup.find_all('a'):
    #print(url)
    #print(*url)
    #print(url.string)
    #print(url.text)
    print(url.get('href'))
