
# develop by name: vishvdeep
# program web scrapping



import urllib2
from bs4 import BeautifulSoup


quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('class': 'name')
name = name_box.text.strip()

price_box = soup.find('class': 'price')
price = price_box.text

print name

print price