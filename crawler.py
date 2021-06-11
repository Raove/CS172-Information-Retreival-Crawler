import requests #requires pip install requests
import re
from bs4 import BeautifulSoup #requires pip install beautifulsoup4
import urllib.robotparser

exitProgram = False
URLs = ["https://www.ucla.edu/", "https://uci.edu/", "https://www.ucr.edu/", "https://www.ucsd.edu/"]

#saved path for file crawling test purposes, replace red text in line 41 and 57
Raoulpath = "C:\Users\raoul\Documents\GitHub\CS172-Information-Retreival-Crawler\files"
Brianpath = "C:\Users\Brian\Desktop\Git Project\CS172-Information-Retreival-Crawler\files"
Mariopath = ""
Arturopath = ""

while(exitProgram != True):
    print("\n\nChoose an option:\n1. Run crawler and make HTML files.\n2. Build index.\n3. Show URL's crawled.\n4. Add URL to crawl.\n5. Exit program.\n")
    option = input()
    print('\n')
    if option == '1':
        print("How many levels do you want to crawl per site?")
        levels = input()
        levels = int(levels)
        for url in URLs:
            rp = urllib.robotparser.RobotFileParser()
            print(url)
            try:
                source = requests.get(url).text
            except requests.exceptions.ConnectionError:
                requests.status_codes = "Connection Refused"
                print("Connection refused")
            pageUrls = []
            level = 1
            pageUrls.append(url)
            rp.set_url(url + "robots.txt")
            rp.read()
            rp.crawl_delay('*')
            while pageUrls and level < levels:
                soup = BeautifulSoup(source, 'lxml')
                filename = url.translate({ord(i): '' for i in ' |!@#$%^&*\()_+=<>\",.:;?/\\[]\{\}~`\n\t\r\b\f-\''})
                filename = filename.replace('http', '')
                f = open(r"C:\Users\raoul\Documents\GitHub\CS172-Information-Retreival-Crawler\files" +"\\"+ filename  + ".html", "w", encoding='utf-8')
                f.write(soup.prettify())
                f.close()
                for urls in soup.find_all('a', href=True):
                    if urls not in pageUrls:
                        # print(urls)
                        if 'http' in urls.get('href'):
                            if rp.can_fetch('*',urls.get('href')) == True:
                                try:
                                    source2 = requests.get(urls.get('href')).text
                                except requests.exceptions.ConnectionError:
                                    requests.status_codes = "Connection Refused"
                                    print("Connection refused")
                                soup2 = BeautifulSoup(source2, 'lxml')
                                filename = urls.get('href').translate({ord(i): '' for i in ' |!@#$%^&*\()_+=<>\",.:;?/\\[]\{\}~`\n\t\r\b\f-\''})
                                filename = filename.replace('http', '')
                                f = open(r"C:\Users\raoul\Documents\GitHub\CS172-Information-Retreival-Crawler\files" +"\\"+ filename  + ".html", "w", encoding='utf-8')
                                f.write(soup2.prettify())
                                f.close()
                                print("Level:",level)
                                pageUrls.append(urls.get('href'))
                                if level == levels:
                                    break
                                level += 1
                            # print("We got here")
                            else:
                                print("Robots.txt denied this link")
                                pageUrls.append(urls.get('href'))
            # print(pageUrls)

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






