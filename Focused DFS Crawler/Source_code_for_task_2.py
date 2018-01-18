import requests
import time
from collections import deque
from bs4 import BeautifulSoup
import nltk
import re

url = "https://en.wikipedia.org/wiki/Tropical_cyclone"                                       #seed url
urls_crawled = [url]
queue_urls = deque([])
queue_urls.append(url)

def my_crawler(url1,kw):
                 my_source_code = requests.get(url1)                                          #requests the url to be crawled
                 text_content = my_source_code.text                                           #finds only the main text content on the url to be crawled page
                 soup = BeautifulSoup(text_content, "html.parser")                            #used for parsing the required tags
                 for link in soup.findAll('a' ,href = True):                                  #check if found 'a' tags with some content in it
                    href = "https://en.wikipedia.org" + link.get('href')
                    if href not in urls_crawled and href.find("#") == -1 and href.startswith(
                            "https://en.wikipedia.org/wiki") and len(
                            href.split(':')) <= 2 and len(urls_crawled) < 1000 and href.find(kw) > -1: #remove the unrequired urls,i.e.,cleaning the urls
                            startindex = href.index("/wiki") + 6                                       #this will give the start index of the required string coming after /wiki/
                                                                                                       #added 6 and not 5 because "/wiki" will always be succeeded by "/" based on the previous cleaning done in the steps above
                            endindex = len(href)                                                       #this given the end of string index
                            sb = nltk.stem.SnowballStemmer('english')                                  #using the Snowball Stemmer to stem the words to their roots
                            final_stem = href[startindex:endindex]                                     #this contains the required values we need for further processing
                            required = sb.stem(final_stem)                                                    #gives the required values after stemming that we need to check
                            if re.search(r'_rain_ | _Rain_ | _rain+ | _Rain+|\^rain|\^Rain|_rain',required):  #this regular expression checks for the required urls we need to store
                                urls_crawled.append(href)                                                     #append in the main output url array
                                queue_urls.append(href)                                                       #append in a queue for popping the next url received
                    time.sleep(1)                                                                             #maintains the politeness policy of one second delay between two requests



def depth(dp):
    depthChecker = [url]                                              #keeps a track of the depth level
    dp = 2                                                            #start with depth 2 because depth 1 simply contains one seed url
    while(dp<=6):                                                     #loop till the depth of 6

        try:
            first_elm = queue_urls.popleft()                          #pop the first element at every iteration, maintaining breadth first search.
            keyword = "rain"
            my_crawler(first_elm,keyword)                             #function which crawls the urls along with a keyword passed in the function to find specific "keyword related" links

        except:
            return                                                     #if no more urls left to crawl, exit.

        if(len(urls_crawled) <= 1000):                                 #if 1000 unique urls not yet found, continue crawling
            continue

        if (depthChecker[len(depthChecker)-1] == first_elm and dp!=2): #check for the last url in the depth to determine end of depth
            print('for depth = %d' %dp)
            print(urls_crawled)                                        # print the unique urls found
            print(len(urls_crawled))                                   #print how many unique urls found
            depthChecker.append(urls_crawled[len(urls_crawled)-1])
            dp=dp+1                                                    #increment the depth if reached end of depth

        if(len(urls_crawled) == 1000):
            dp = dp + 1                                                #if breaks at 1000 unique links, urls must be stored in the next depth
            print('for depth = %d' %dp)
            print(urls_crawled)                                        #print 1000 unique urls crawled
            print(len(urls_crawled))                                   #print length of unique urls crawled, which should be 1000
            break

depth(6)                                                               #crawl till the depth of 6

with open('RainurlsCrawled.txt','w') as outfile:                       #Save the output of unique urls crawled in an output file named 'urlsCrawled'.
  for link in urls_crawled:
    outfile.write("%s\n" %link)
