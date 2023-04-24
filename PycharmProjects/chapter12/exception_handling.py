
# 10번 루프를 반복
for i in range(10):
    #예외처리 불록 구성
    try:
        #10을 반복 제어변수 i로 나눔
        print('10/{} = {:.2f}'.format(i,10/i))
    #0으로 나누었을 때 예회처리
    except ZeroDivisionError as e:
        #예외 매시지 출럭
        print('못나눠잉~')
        print(e.__str__())      # = print(e)와 같음 __str__을 자동으로 불러오기 떄문에.