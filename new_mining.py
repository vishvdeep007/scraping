#Develop by name: vishvdeep
#This is Open source Code for scraping Time of india website

import urllib2
from bs4 import BeaultifulSoup

#scraping data 
def scrap(name):
	#url fir data mining
	page = page=  'http://timesofindia.indiatimes.com/{name}'

	response = (page=page.format(name = name))

	url = urllib2.urlopen(response)

	soup = BeaultifulSoup(url.content, 'html.parser')

	#text scraping 
	Text_box = soup.find('div', attrs('class': 'Normal'))
	Text_data = Text_box.text

	#image scraping 
	image = soup.find('section', attrs('highlight clearfix')).find_all('img', src=Ture)
	for images in image
		timestamp = time.asctime()
		txt = open('%s.jpg' % timestamp, "wb")
		images = images["src"].split("src=")[-1]
		downlaod_img = urllib2.urlopen(images)
		txt.write(downlaod_img.read())

#storing data into json file
def store_data_json(Text_data, image):
	import json

	data ={
		'Text': 'Text_data',
	}

	json_data = json.dumps(data)


def main():
	scrap(name)
	store_data_json(Text_data, image)


if __name__ = '__main__':
	main()