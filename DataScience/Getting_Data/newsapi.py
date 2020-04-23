# apiKey=b5f1f1d799f6450395d37830c518fb5b
import requests
from collections import defaultdict

url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=b5f1f1d799f6450395d37830c518fb5b')
response = requests.get(url)
news = response.json()
articles = news['articles']

print("totalResults :", news['totalResults'])
print("Author List")
for i in range(len(articles)) :
       print(i + 1, ":", articles[i]['author'])
