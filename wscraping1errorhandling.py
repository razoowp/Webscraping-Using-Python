from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try:
    content = urlopen("http://english.onlinekhabar.com/2017/08/01/404359.html")
    soup = BeautifulSoup(content, "lxml")

except HTTPError:
    print(HTTPError)
    exit()

except AttributeError as ae:
    print(ae)
    exit()

print(soup.h1)
