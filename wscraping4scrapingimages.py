from urllib.request import urlopen
from bs4 import BeautifulSoup

i=1
url = "file:///media/programmer/1E2C3FBC2C3F8E31/careertutorials/DATASCIENCE/webscrapingPython/scrapingwebsites/Home%20_%20University%20of%20Waterloo.html"
content = urlopen(url)
soup = BeautifulSoup(content, "html.parser")

for img in soup.findAll("img"):
	temp = img.get('src')


	if temp[:1] == ".":
		temp = temp[1:]
		image = "file:///media/programmer/1E2C3FBC2C3F8E31/careertutorials/DATASCIENCE/webscrapingPython/scrapingwebsites" + temp
	else:
		image = temp

	# This is for name of image
	nametemp = img.get('alt')

	if len(nametemp) == 0:
		filename = str(i)
		i+=i
	else:
		filename = nametemp

	imagefile = open(filename + ".jpeg" ,"wb")
	imagefile.write(urlopen(image).read())
	imagefile.close()