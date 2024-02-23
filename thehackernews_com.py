from fire_scrapy import Article
from fire_scrapy import getRSS
import pickle
import feedparser
from typing import List

URL = "https://feeds.feedburner.com/TheHackersNews"

def get() -> List[Article]:
    return getRSS(URL)

def getRSS(url) ->List[Article]:
    feed = feedparser.parse(url)
   
    ls:List[Article] = []

    for entry in feed.entries:
        article = Article(entry.title, entry.summary,entry.link,entry.published)
        ls.append(article)

    return ls

def save():
    ls = get()
    with open("output/hackernews.com.pickle", "wb") as f:
        pickle.dump(ls, f)
    f.close()

if( __name__ == '__main__'):
    save()