
# devlop by name: vishvdeep
# main_content is in variable text_data
# image is in variable downlaod_img



import urllib2
from bs4 import BeautifulSoup
import time

#name is th variable that is given by the user
name = "somthing"
page = 'http://timesofindia.indiatimes.com/{name}'

response = page=page.format(name = name)

url = urllib2.urlopen(response)

soup = BeautifulSoup(url.content, 'html.parser')

#scraping the main text content 
text_box = soup.find('div', attrs('class': 'Normal'))
text_data = text_box.text

#scraping the highlight image 
image = soupo.find('section', attrs('highlight clearfix')).find_all('img', src=Ture)
for images in image
	timestamp = time.asctime()
	txt = open('%s.jpg' % timestamp, "wb")
	images = images["src"].split("src=")[-1]
	downlaod_img = urllib2.urlopen(images)
	txt.write(downlaod_img.read())

# stroing data into json format 
import json

data = {
	'Text': 'text_data'
	'image': 'downlaod_img'
}

#writing json file
json_data = json.dumps(data)

