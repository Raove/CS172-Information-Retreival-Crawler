#used to get url contents apparently
import requests
from bs4 import BeautifulSoup

#flask for the web app
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('WebApp.html')

@app.route('/crawl/')
def my_link():
    #To be replaced when actual crawl is made

    #Algorithm:
    #1.Get website url
    #2.Scan through website url
    #3.Get any hyperlinks not in the robot.txt and put in list
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
    
    #up to here
    return 'Click.'

if __name__ == '__main__':
    app.run(debug=True)