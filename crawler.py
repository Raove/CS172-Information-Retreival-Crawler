import requests #requires pip install requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup #requires pip install beautifulsoup4

exitProgram = False
URLs = ["https://www.ucr.edu/", "https://www.ucla.edu/", "https://uci.edu/", "https://www.stanford.edu/"]

while(exitProgram != True):
    print("\n\nChoose an option:\n1. Run crawler and make HTML files.\n2. Build index.\n5. Exit program.")
    option = input()
    if option == '1':
        print("How many levels do you want to crawl?")
        levels = input()
        
    if option == '2':
        print("Good luck arturo")
    if option == '5':
        exitProgram = True






