from fire_scrapy import Article
from fire_scrapy import scrape
from fire_scrapy import getRSS

articles = getRSS("https://www.protothema.gr/rss")

for x in articles:
    print(x.getText())
