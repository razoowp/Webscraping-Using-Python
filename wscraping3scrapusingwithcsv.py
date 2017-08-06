from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

#url= "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card"
url="file:///media/programmer/1E2C3FBC2C3F8E31/careertutorials/DATASCIENCE/webscrapingPython/Graphics%20Cards%20and%20Video%20Cards%20-%20Newegg.com.html"

content = urlopen(url)
soup = BeautifulSoup(content, "lxml")

containers = soup.findAll("div", {"class":"item-container"})

#f = open("scrap.csv", "w")
#headers = "products, price \n"
#f.write(headers)

with open("scrap1.csv", "a") as csv_file:
	csv_app = csv.writer(csv_file)
	csv_app.writerow(['product_name', 'price'])


for container in containers:
	#print(container.div.div.a.img["title"])
	title = container.find("a", {"class":"item-title"})
	product_name = title.text
	pricelist = container.find("li", {"class":"price-current"})
	dollar = pricelist.strong.text
	cents = pricelist.sup.text
	price = dollar + cents


	#f.write(product_name.replace(",", "|") + "," + price.replace(",", " ") + "\n")
	with open("scrap1.csv", "a") as csv_file:
		csv_app = csv.writer(csv_file)
		csv_app.writerow([product_name, price])
	