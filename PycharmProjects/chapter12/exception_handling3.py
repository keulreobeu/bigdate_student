
# 10번 루프를 반복
for i in range(10):
    fmt = '10/{} = {:.2f}'
    result = 0
    # 예외처리 불록 구성
    try:
        #10을 반복 제어변수 i로 나눔
        result = 10 / i
    #0으로 나누었을 때 예회처리
    except ZeroDivisionError as e:
        print(e.__str__())      # = print(e)와 같음 __str__을 자동으로 불러오기 떄문에.

    else:        #예외가 발생되지 않을때
        print(fmt.format(i,result))

    finally:        #예외발생에 관계없이 무조건 출력
        print('결과')