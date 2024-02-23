from fire_scrapy import Article
from fire_scrapy import scrape
from fire_scrapy import getRSS
from typing import List
import pickle

URL = "https://www.protothema.gr/rss"

def get()->List[Article]:
    return getRSS(URL)

def save():
    ls = get()
    with open("protothema.pickle", "wb") as f:
        pickle.dump(ls, f)

if( __name__ == '__main__'):
    save()