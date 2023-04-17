# 10번 루프를 반복
for i in range(10):
    #예외처리 불록 구성
    try:
        #10을 반복 제어변수 i로 나눔
        print(f'10 / {i} = {10/i:.2f}')
    #0으로 나누었을 때 예회처리
    except Exception as e:  #모든 예외는 Exception을 상속받음
        #예외 매시지 출럭
        print(type(e))
    except ZeroDivisionError as E:
        print(E)
    else:
        print('예외가 발생되지 않음')