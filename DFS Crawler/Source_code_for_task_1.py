import requests
#import time
from collections import deque
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Tropical_cyclone"                 #seed url
urls_crawled = [url]
queue_urls = deque([])
queue_urls.append(url)

def my_crawler(url1):
                 my_source_code = requests.get(url1)                   #requests the url to be crawled
                 text_content = my_source_code.text                    #finds only the main text content on the url to be crawled page
                 soup = BeautifulSoup(text_content, "html.parser")     
                 for link in soup.findAll('a' ,href = True):           
                    href = "https://en.wikipedia.org" + link.get('href')
                    if href not in urls_crawled and href.find("#") == -1 and href.find("Main_Page") == -1 and href.startswith(
                            "https://en.wikipedia.org/wiki") and len(
                            href.split(':')) <= 2 and len(urls_crawled) < 1000:    #remove the unrequired urls,i.e., cleaning the urls
                              urls_crawled.append(href)                            
                              queue_urls.append(href)                              
                    #time.sleep(1)                                      #maintains the politeness policy


def depth(dp):
    depthChecker = [url]                                               #keeps a track of the depth level
    dp = 2                                                             
    while(dp<=6):                                                      

        first_elm = queue_urls.popleft()                               #pop the first element at every iteration, maintaining breadth first search.
        my_crawler(first_elm)                                          

        if (depthChecker[len(depthChecker)-1] == first_elm and dp!=2): #check for the last url in the depth to determine end of depth
            print('for depth = %d' %dp)
            print(urls_crawled)                                        
            print(len(urls_crawled))                                   
            depthChecker.append(urls_crawled[len(urls_crawled)-1])
            dp=dp+1                                                    #increment the depth if reached end of depth

        if(len(urls_crawled) == 1000):                                 #if breaks at 1000 unique links, urls must be stored in the next depth
            print('for depth = %d' %dp)
            print(urls_crawled)                                        
            print(len(urls_crawled))                                   
            return dp

crawl_to_depth = depth(6)                                              #crawl till the depth of 6

with open('urlsCrawled.txt','w') as outfile:                           #Save the output of unique urls crawled in an output file named 'urlsCrawled'.
  for link in urls_crawled:
    outfile.write("%s\n" %link)
  outfile.write("Maximum depth reached : %d" %crawl_to_depth)
