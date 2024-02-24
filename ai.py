import thehackernews_com
import dateparser
article = thehackernews_com.get()[0]

print(article.date)
print(article.title)
print(dateparser.parse(article.date))