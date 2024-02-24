from urllib.parse import urlparse
import pickle
from news import Article
from typing import List
import feedparser

def getRSS(url) ->List[Article]:
    feed = feedparser.parse(url)
   
    ls:List[Article] = []

    for entry in feed.entries:
        article = Article(entry.title, entry.summary,entry.link,entry.published,entry.category)
        ls.append(article)

    return ls

# get an RSS that doesnt have category
def getRSSNoCateg(url) ->List[Article]:
    feed = feedparser.parse(url)
   
    ls:List[Article] = []

    for entry in feed.entries:
        article = Article(entry.title, entry.summary,entry.link,entry.published,categ="")
        ls.append(article)

    return ls

# save and name based on the url domain
def save(URL: str,articleList : List[Article]):
    t = urlparse(URL).netloc
    u = '.'.join(t.split('.')[-2:])
    with open(f"output/{u}.pickle", "wb") as f:
        pickle.dump(articleList, f)
    f.close()


if( __name__ == '__main__'):
   pass