from fire_scrapy import Article
import feeder

from typing import List

URL = "https://www.darkreading.com/rss.xml"


def get() -> List[Article]:
    return feeder.getRSSNoCateg(URL)

def saveToFile():
    feeder.save(URL,get())


if( __name__ == '__main__'):
    saveToFile()