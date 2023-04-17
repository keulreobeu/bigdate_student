import os, random, datetime
# os.mkdir("log")    #폴더를 만듬


#폴더가 있는지 확인후 없으면 생성
log = 'log'
if not os.path.isdir(log):        #로그 폴더가 없다면 폴더를 만들어라.
    os.mkdir(log)

path = f'{str(log)}//count_log.txt'
#파일이 있는지 확인 없으면 생성
if not os.path.exists(path):
    with open(path, 'w', encoding='utf8') as f:
        f.write('기록의 시작지점\n')

#파일에 랜덤값을 추가.
with open(path, 'a', encoding='utf8') as f:
    #난수와 데이터타임을 만들어 파일에 추가함. 10회
    for i in range(1,11):
        stamp = str(datetime.datetime.now())
        value = random.random()*1000000
        log_line = f'{stamp}\t{str(value)}값이 생성되었다.\n'  #반복문 안에서 문자열 접합(+)을 하면 안됨, 매모리를 너무 많이씀
        f.write(log_line)

print(type(datetime.datetime.now()))