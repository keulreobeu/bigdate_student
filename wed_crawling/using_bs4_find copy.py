import requests
from bs4 import BeautifulSoup

url = 'http://python.cyber.co.kr/pds/books/python2nd/test2.html'
# 데이터 호출한 다음 bs4에 연결하기
respones = requests.get(url)
bs = BeautifulSoup(respones.text, 'html.parser')

# 원하는 곳에 있는 데이터 불러오기 h2, 2번째 h2
print(bs.find('h2').text)       #첫번째 객채만 가져옴
print(bs.find_all('h2')[1].text)        #전부 가져옴 리스트로

for i in bs.find_all('h2'):
    print(i)
print(type(bs.find_all('h2')))
# 짝수번쨰 li의 텍스트를 조회해보세요



# # 짝수번쨰 li의 텍스트를 조회하고 result.txt파엘에 저장해보세요.   



# 파일을 열때 for문은 항상 빠르게 사용하여야함, 계속 열려있기 떄문에. 아니면 따로 빼둬야함.

