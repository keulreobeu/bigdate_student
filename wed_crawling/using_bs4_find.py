import requests
from bs4 import BeautifulSoup

url = 'http://python.cyber.co.kr/pds/books/python2nd/test2.html'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'html.parser')

print(bs.find("h2").text)
print(bs.find_all("h2")[1].text)

# 짝수번쨰 li의 텍스트를 조회해보세요

print(bs.find_all('li'))

print('-----------------------')
for seq, tag in enumerate(bs.find_all('li'),start=1):
    if seq % 2 == 0:
        print(f'{seq}: {tag.text}')
        
# # 짝수번쨰 li의 텍스트를 조회하고 result.txt파엘에 저장해보세요.   
# file_path = './wed_crawling/result.txt'     
# with open(file_path, 'w', encoding='utf-8') as f:   
#     for seq, tag in enumerate(bs.find_all('li'),start=1):
#         if seq % 2 == 0:
#             f.write(f'{seq}: {tag.text}\n')
# 파일을 열때 for문은 항상 빠르게 사용하여야함, 계속 열려있기 떄문에. 아니면 따로 빼둬야함.

file_path = './wed_crawling/result.txt' 
result = []
for seq, tag in enumerate(bs.find_all('li'),start=1):
    if seq % 2 == 0:
        result.append(f'{seq}: {tag.text}\n')

with open(file_path, 'w', encoding='utf=8') as f:
    f.writelines(result)