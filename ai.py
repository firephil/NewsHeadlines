import thehackernews_com
import dateparser
# pip install pytrends
# https://github.com/GeneralMills/pytrends

article = thehackernews_com.get()[0]

print(article.date)
print(article.title)
print(dateparser.parse(article.date))