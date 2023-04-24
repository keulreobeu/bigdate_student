import random

number = random.randint(1,100)


while 1 :
    ans = int(input('답을 입력하세요.'))
    if ans == number:
        print('정답')
        break
    elif ans < number:
        print('숫자가 너무 작습니다.')
    else:
        print('숫자가 너무 큽니다.')