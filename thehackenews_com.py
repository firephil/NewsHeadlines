# use rss feed https://feeds.feedburner.com/TheHackersNews
# use explicit import for documentation

from fire_scrapy import Article
from fire_scrapy import scrape

from typing import List

def articles():

    page = scrape('https://thehackernews.com')
    
    articles = page.find_all('h2', class_='home-title')
    
    ls:List[Article] = []

    for article in articles:
        a = Article(article.getText())
        ls.append(a)

    print(ls)

if( __name__ == '__main__'):
    articles()