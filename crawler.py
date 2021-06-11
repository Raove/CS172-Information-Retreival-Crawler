import requests #requires pip install requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup #requires pip install beautifulsoup4

exitProgram = False
URLs = ["https://www.ucr.edu/", "https://www.ucla.edu/", "https://uci.edu/", "https://www.stanford.edu/"]

while(exitProgram != True):
    print("\n\nChoose an option:\n1. Run crawler and make HTML files.\n2. Build index.\n3. Show URL's crawled.\n4. Add URL to crawl.\n5. Exit program.\n")
    option = input()
    print('\n')
    if option == '1':
        print("How many levels do you want to crawl?")
        levels = input()
        source = requests.get('https://www.ucr.edu/').text
        soup = BeautifulSoup(source, 'lxml')
        f = open(r"C:\Users\raoul\Documents\GitHub\CS172-Information-Retreival-Crawler\files\page.html", "w")
        f.write(soup.prettify())
        f.close()
        title = soup.find('title')
        article = soup.find_all('article')
        print(title.text)
        # for arti in article:
        #     print(arti.prettify())
        
    if option == '2':
        print("Good luck arturo")
    if option == '3':
        count = 0
        for url in URLs:
            count += 1
            print(str(count) + '.', url)
    if option == '4':
        print("Enter URL to crawl.")
        add = input()
        URLs.append(add)
    if option == '5':
        exitProgram = True






