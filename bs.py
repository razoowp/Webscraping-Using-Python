#Import the necessary libraries
import requests
from bs4 import BeautifulSoup

#create User-Agent
headers = {
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

#get() Request
response = requests.get("https://pandas.pydata.org/", headers=headers)

#Store the webpage Content
webpage = response.content

#Check The Status Code
print(response.status_code)

#Create a BeautifulSoup Object out of the webpage content
soup = BeautifulSoup(webpage, "html.parser")

#Pretty print the webpage html
#print(soup.prettify)
#print(soup.head)
#print(soup.p)
# print(soup.head.contents[3].name) #contents shows the child tags in list, and 3 is third child tag, and name shows tag name.
# print(soup.contents[2].name)
# print(soup.head.contents)
# for tags in soup.head.contents:
#     if(tags != '\n'):
#         print(tags.name)
#
#CHILDREN
# for tags in soup.body.children:
#     if(tags != '\n'):
#         print(tags.name)

#DESCENDANTS
# for tags in soup.header.descendants:
#     if(tags != '\n'):
#         print(tags.name)

# children = [child for child in soup.header.children if child != '\n']
# descendant = [des for des in soup.header.descendants if des != '\n']
# print(len(children))
# print(len(descendant))
# print(children[0].name)
# print(descendant[13]) #descendants le inner tag, tag bich ko value pani linxa
#
# #.parent
# print(soup.title.parent)
# print(soup.title.parent.name)

#.parents
# for parents in soup.a.parents:
#     print(parents.name)

#.next_sibling
# print(soup.i.next_sibling)
#
# #.previous_sibling
# print(soup.i.previous_sibling)

#.next_siblings and .previous_siblings
# for sibling in soup.i.next_siblings:
#     print(sibling)
# for sibling in soup.i.previous_siblings:
#     print(sibling)

#Get Tag Content STrings
print(soup.title.string)

#Strings Generator
for string in soup.body.strings:
    if(string != '\n'):
        print(string)

for string in soup.body.stripped_strings:
    print(string)