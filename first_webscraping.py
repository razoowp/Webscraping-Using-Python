from urllib.request import urlopen
url="http://google.com"
page = urlopen(url)
print(page.read())