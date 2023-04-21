import requests
# url에서 데이터 불러오기
url = 'http://python.cyber.co.kr/pds/books/python2nd/test1.html'

response = requests.get(url)

file_path = './wed_crawling/html.txt'


# f = open(file_path, 'w')
# f.write(response.text)
# f.close()

# f = open(file_path, 'r')
# print(f.read)
# f.close()


# 불러온 파일 쓰고 읽기
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(response.text)

with open(file_path, 'r', encoding='utf-8') as f:
    print(f.read())