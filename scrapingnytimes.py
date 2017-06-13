from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/section/world/africa"
content = urlopen(url)
soup = BeautifulSoup(content, "lxml")

for news in soup.find_all("div", {"class":"story-meta"}):
    print(news.get_text())
