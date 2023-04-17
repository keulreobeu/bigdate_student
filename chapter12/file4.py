#파일열기 with로
with open('dream.txt','r') as f:
    #루프 만들기
    i = 0
    while 1:
        #파일을 라인으로 열기
        contents = f.readline()
        #루프 끝내기
        if not contents:
            break
        #결과값 만들기
        print(str(i)+"\t"+contents.replace('\n',''))
        i += 1