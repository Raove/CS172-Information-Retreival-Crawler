# CS172-Information-Retreival-Crawler
 
## Raoul 'Raove' Larios
## Arturo 'Big Churro' Delgado
## Mario 'Choduh' Aguirre
## Brian 'Fingerless' Corbita


## Insight

This is the final project for CS172 information retrieval of a basic web crawler. The language used for the program is 'Python 3.9.x'.

## Part 1

We implemented a crawler that crawls html files given a url. The main functionality is in 'crawler.py'. We imported two libraries, 'requests' and 'from urllib.parse import urlparse'. The class 'PyCrawler' takes in an object will extract the information from the starting url. It will check the html from the sites and 'urlparse' will parse the links. The 'crawl' function will check the visited links and extract the infromation of each by specific titles and keywords.

## Part 2

## Part 3

We implemented a web application in which the user can use as an interface for our crawler. To do this, we used Flask to implement the python scripts in the website. Used text boxes for the user to insert the URLs they want to crawl and the amount of levels that the crawler will hop down to. We made the a server.py for the Flask architecture and backend for the website. In the folder, we implemented the WebApp.html as a the template and frontend of the site.
