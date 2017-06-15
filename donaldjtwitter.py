from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://twitter.com/realDonaldTrump"
content = urlopen(url)
soup = BeautifulSoup(content, "lxml")

for tweets in soup.findAll('div',{"class":"content"}):
    print(tweets.find('p').text)
