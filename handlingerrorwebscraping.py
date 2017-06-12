from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getInfo(url):
    try:
        content = urlopen(url)
    except HTTPError as e:
            return None
    try:
        soup = BeautifulSoup(content, "lxml")
        info = soup.a
    except AttributeError as e:
        return None
    return info


link = "https://www.nytimes.com/"
about_info = getInfo(link)

if about_info is None:
    print("No information found !!!")
else:
    print(about_info)
