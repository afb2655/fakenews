import requests
import re
from bs4 import BeautifulSoup

cnnpage = requests.get("https://www.cnn.com/")

Beauty = BeautifulSoup(cnnpage.content, 'html.parser')

headlinelist = Beauty.findAll('span')

headline = Beauty.findAll('span')

h2test = Beauty.findAll("li")

atest = Beauty.findAll("a")

articletest = Beauty.findAll("article")



teststring = Beauty.prettify()

texttest = Beauty.findAll('text')

strng = Beauty.prettify()


#FOX
FOXpage = requests.get("http://www.foxnews.com/")

FOXbeau = BeautifulSoup(FOXpage.content, 'html.parser')

FOXbeau.prettify()

#MSN
MSNpage = requests.get("https://www.msn.com/en-us/news")

MSNbeau = BeautifulSoup(MSNpage.content, 'html.parser')

MSNbeau.prettify()

#Start of analysis








re_pattern = re.compile(r'\b(?:Trump|trump|Trumps|trumps)\b')

CNN = re.findall(re_pattern,teststring)

print("CNN Trumps ", len(CNN))

FOX = re.findall(re_pattern,FOXbeau.prettify())


print("FOX Trumps: ", len(FOX))

MSN = re.findall(re_pattern,MSNbeau.prettify())

print("MSN Trumps: ", len(MSN))











#print('Trump' in strng)


# for i in range(len(strng)):
#     if(strng[i] == "Trump" or strng[i] == "trump" or strng[i] == "Trump." or strng[i] == """"Trump""""" or strng[i] == "Trump!" or strng[i] == "Trump's" or strng[i] == '"Trump:' or (strng[i] == 'Trump?"' )):
#         print(strng[i-1])
#         print(strng[i])
#         print(strng[i+1])
#         accum += 1
#
# print(accum)

# for line in headlinelist:
#     print(line.text)
#
# for line in headline:
#     print(line.text)
#
# for line in h2test:
#     print(line.text)

# for line in atest:
#     print(line)

# for line in articletest:
#     print(line)

