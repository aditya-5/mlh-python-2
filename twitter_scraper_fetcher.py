import requests
from bs4 import BeautifulSoup
from config import TWITTER_URL
import re

CONTENT_CLASS_NAME = "dir-ltr"
CONTENT_CONTAINER_TAGS = ["div"]
EMPTY_ITEMS = [None, "", "None", "\n"]
AGENTS= 'Nokia5310XpressMusic_CMCC/2.0 (10.10) Profile/MIDP-2.1 '\
'Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; '\
'Nokia5310XpressMusic) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile'


def get_elements(twitter_handle):
  url = TWITTER_URL + twitter_handle
  response = requests.get(url, headers={'User-Agent':AGENTS})
  html = response.content
  soup = BeautifulSoup(html, "html.parser")
  return soup.find_all(CONTENT_CONTAINER_TAGS, {"class":CONTENT_CLASS_NAME})
    
def get_user_tweets(twitter_handle):
  elements = get_elements(twitter_handle)
  tweets = []
  for post in elements:
    for text in post.contents:
      if text.string not in EMPTY_ITEMS: 
        tweets.append(text.string)
    
  pass

def clean_tweets_data(tweets):
  ## Nothing here yet!
  pass
    
  
            
                

    
