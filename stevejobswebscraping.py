from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Steve_Jobs"
content = urlopen(url)
soup = BeautifulSoup(content, "lxml")
#to get image files within the site
# for link in soup.find("div", {"id":"bodyContent"}).find_all("a", href=re.compile("^(/wiki/File:)((?!:).)*$")):
for link in soup.find("div", {"id":"bodyContent"}).find_all("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

