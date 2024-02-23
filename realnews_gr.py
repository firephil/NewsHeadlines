from fire_scrapy import Article
from fire_scrapy import getRSS
from typing import List
import pickle

URL = "https://www.real.gr/teleutaies_eidiseis/rss/"

def get()->List[Article]:
    return getRSS(URL)

def save():
    ls = get()
    with open("output/realnews_gr.pickle", "wb") as f:
        pickle.dump(ls, f)


if( __name__ == '__main__'):
    save()