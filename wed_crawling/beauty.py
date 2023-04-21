import requests
from bs4 import BeautifulSoup

url = 'http://python.cyber.co.kr/pds/books/python2nd/test1.html'
html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')

print(bs.html.head.title)     # __str__()객체를 반환한것
print(bs.html.head.title.text)
print(bs.html.body.text)
print(bs.html.body.h2)
print(bs.html.body.h2.text)
print(bs.h2.text)
print(bs.ol.text)
print(bs.ol.li)    # 첫번째거가 나옴.
print(type(bs.ol.li))