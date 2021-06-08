#used to get url contents apparently
import requests

#Algorithm:
#1.Get website url
#2.Scan through website url
#3.Get any hyperlinks not in the robot.txt and put in list
#4.Store website content as txt file
#5.Run txt file through Assignment 1 code
#6.Repeat 4 and 5 for each link stored from 3
#7.Do 6 for amount of levels time


#Testing on one website at the moment
print("Enter website to crawl: ")
url = input()
output = requests.get(url)

#output
file = open("output.txt", "a")
file.write(output.text)
file.close()