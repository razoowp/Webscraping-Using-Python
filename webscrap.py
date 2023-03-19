# from urllib.request import urlopen
# url = 'https://www.nytimes.com/international/'
# page = urlopen(url)
# print(page.read())

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
url = 'https://pandas.pydata.org/'
# content = urlopen(url)
# soup = BeautifulSoup(content,'lxml')
# print(soup.a.get_text())

import requests
# response = requests.get(url)
# #print(r.status_code)
# #print(response.text)
# webpage = response.content
# #print(webpage)
# #print(response.headers)
#KEEPING RESPONSE HEADERS IN ORGANIZED FORMAT
# for key,value in response.headers.items():
#     print(key, ':', value)

#PRINT USER AGENT
# print(response.request.headers)

#DEFINE OUR OWN USER AGENT TO FIX 5XX Error 
url = 'https://www.amazon.com/'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response.status_code)
