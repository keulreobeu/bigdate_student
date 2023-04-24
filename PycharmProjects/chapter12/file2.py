# f = open('dream.txt','r')
# print(type(f))
# content = f.readlines()     #read는 전부, readlins는 한줄한줄 다 리스트에 넣어서 출력, readline은 한줄만 불러옴
# print(type(content))
# print(content)
# f.close()

with open('dream.txt','r') as f:
    contents = f.read()
    print(type(contents),contents)