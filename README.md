# CS172-Information-Retreival-Crawler
 
## Raoul Larios
## Arturo Delgado
## Mario Aguirre
## Brian Corbita


## Insight

This is the final project for CS172 information retrieval of a basic web crawler. The language used for the program is 'Python 3.9.x'.

## Part 1

We implemented a crawler that crawls html files given a url. The main functionality is in 'crawler.py'. We imported two libraries, 'requests' and 'from urllib.parse import urlparse'. The class 'PyCrawler' takes in an object will extract the information from the starting url. It will check the html from the sites and 'urlparse' will parse the links. The 'crawl' function will check the visited links and extract the infromation of each by specific titles and keywords.

## Part 2
When choosing option 2 the program will then be prompted to index the the html links that are in the list. If the user has not put in a link using option four then it will only go through UCLA, UCI,UCR,UCSD website. If another one is added then it will be appended to the list and then use must run option one again so the page rank for the one you want will show up in html files on your computer. THose files are then used in part of the ElasticSearch indexing. We decided to use Elasticsearch for our indexing. The program is really straight forward but was confusing at first to learn. Using resources provided to use we were able to figure it out. We run a for loop that goes through the html files in the first options directory and then runs it in to a function that takes out all the words in the website. Those words are then made into a large string which is then used to index them by the text and the timestamp. Then using a query that was chosen or can be changed. We then check if there is anything that matches it. Then the respone is then shown withe max value and if it was hit or not. The one that is a hit is then displayed on the terminal.

## Part 3

We implemented a web application in which the user can use as an interface for our crawler. To do this, we used Flask to implement the python scripts in the website. Used text boxes for the user to insert the URLs they want to crawl and the amount of levels that the crawler will hop down to. We made the a server.py for the Flask architecture and backend for the website. In the folder, we implemented the WebApp.html as a the template and frontend of the site.
