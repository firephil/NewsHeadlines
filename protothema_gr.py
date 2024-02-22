from fire_scrapy import Article
from fire_scrapy import scrape
from fire_scrapy import getRSS

articles = getRSS("https://www.protothema.gr/rss")

first = articles[0]
print(first.getText())