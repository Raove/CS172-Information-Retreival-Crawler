#used to get url contents apparently
import requests
from bs4 import BeautifulSoup

#Algorithm:
#1.Get website url
#2.Scan through website url
#3.Get any hyperlinks not in the robot.txt/not a duplicate and put in list
#4.Store parse and store website content as txt file
#5.Run txt file through Assignment 1 code
#6.Repeat 4 and 5 for each link stored from 3
#7.Do 6 for amount of levels time


#Testing on one website at the moment
print("Enter website to crawl: ")
url = input()
#gets the html code from the website
output = requests.get(url)
#use soup to get important content in site
content = BeautifulSoup(output.text, "html.parser")

#output
file = open("output.txt", "a")
for element in content.findAll('a', {'class':'s-access-detail-page'}):
    title = element.get('title')
    file.write(title)
    words = element.get('href')
    file.write(words)
file.close()