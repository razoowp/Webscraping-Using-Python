from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#Below code will scrap all the links of website and keep those link titles in list form
def getInfo(url):
    try:
        content = urlopen(url)
    except HTTPError as e:
            return None
    try:
        list =[]
        soup = BeautifulSoup(content, "lxml")
        for anchor in soup.find_all("a"):
            list.append(anchor.get_text())
    except AttributeError as e:
        return None
    return list


link = "https://www.nytimes.com/"
about_info = getInfo(link)

if about_info is None:
    print("No information found !!!")
else:
    print(about_info)
