import requests #requires pip install requests
import re
import codecs
from bs4 import BeautifulSoup #requires pip install beautifulsoup4
import urllib.robotparser
from datetime import datetime
from elasticsearch import Elasticsearch
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from requests.models import Response


URLs = ["https://www.ucla.edu/", "https://uci.edu/", "https://www.ucr.edu/", "https://www.ucsd.edu/"]

#saved path for file crawling test purposes, replace red text in line 41 and 57
#Raoulpath = "C:\Users\raoul\Documents\GitHub\CS172-Information-Retreival-Crawler\files"
#Brianpath = "C:\Users\Brian\Desktop\Git Project\CS172-Information-Retreival-Crawler\files"
Mariopath = ""
#Arturopath = "C:\Users\artur\OneDrive\Documents\CS 172\assignment2\CS172-Information-Retreival-Crawler\files"
list1 = []
def find_body(html_file):
    #html_file =html_file.read()
    #list1 = []
    
    soup = BeautifulSoup(html_file, features="html.parser")

    for script in soup(["script","style"]):
        script.extract()
    
    #text = soup.find_all(text=True)
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    #print(lines)
    chunks = (phrase.strip() for line in lines for phrase in line.split(" "))

    text = ' '.join(chunk for chunk in chunks if chunk)
    return text
#Arturopath = "C:\Users\artur\OneDrive\Documents\CS 172\assignment2\CS172-Information-Retreival-Crawler\files"
def crawler():
    exitProgram = False
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
                    f = open(r"C:\Users\artur\OneDrive\Documents\CS 172\assignment2\CS172-Information-Retreival-Crawler\files" +"\\"+ filename  + ".html", "w", encoding='utf-8')
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
                                    f = open(r"C:\Users\artur\OneDrive\Documents\CS 172\assignment2\CS172-Information-Retreival-Crawler\files" +"\\"+ filename  + ".html", "w", encoding='utf-8')
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
            elastic_pass = "MxOVYVBJTzWEcqsAlMmnY5dA"
            #i-o-optimized-deployment-288542.es.eastus2.azure.elastic-cloud.com:9243
            elastic_endpoint = "i-o-optimized-deployment-288542.es.eastus2.azure.elastic-cloud.com:9243"
            connection_string = "https://elastic:" + elastic_pass + "@" + elastic_endpoint

            #curl -u elastic:MxOVYVBJTzWEcqsAlMmnY5dA
            indexName = "cs172-index"
            esConn = Elasticsearch(connection_string)
            esConn.indices.delete(index=indexName, ignore=[400,404])
            response = esConn.indices.create(index=indexName,ignore = 400)
            print(response)

            indexName = "cs172_index"
            os.chdir(r"C:\Users\artur\OneDrive\Documents\CS 172\assignment2\CS172-Information-Retreival-Crawler\files")
            #print(os.getcwd())
            for html_file in os.listdir(os.getcwd()):
                with open(html_file, 'r', encoding='utf-8') as f:
                    text =find_body(f)
                    #print(text)    
                    doc = {
                        'text': text,
                        'timestamp': datetime.now()
                    }
                    
                
                    response = esConn.index(index=indexName,body=doc)
                    print(response)
                f.close()
            response  = esConn.search(index=indexName, body={"query":{"match_all":{}}})
                    #print(response)
                
            query = "unleash"
            response = esConn.search(index=indexName,body = {
                'query':{
                    'match':{
                        "text":query
                    }
                }
            })
            print(response)
                
            #esConn = Elasticsearch(connection_string)
           # esConn.indices.delete(index=indexName, ignore=[400,404])
            #response = esConn.indices.create(index=indexName,ignore = 400)
            
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

    
crawler()




