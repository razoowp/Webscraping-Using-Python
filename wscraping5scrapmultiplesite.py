from urllib.request import urlopen
#from bs4 import BeautifulSoup
import re

urls = ["http://google.com", "http://nytimes.com", "http://cnn.com"]
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)


'''
for url in urls:
	html = urlopen(url)
	content = html.read()
	#print(content[0:50])
	print(content.title)
	'''

i=0
while(i<len(urls)):
	html = urlopen(urls[i])
	content = html.read().decode('utf-8')
	titles = re.findall(pattern, content)
	print(titles)
	i+=1
