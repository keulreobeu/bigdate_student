import random
import datetime

# 6/45 로또 복권 번호를 생성합니다.

#번호 생성기
def choose_nums():
    sample = sorted(random.sample(range(1, 46), 6))
    return sample
# 로또 복권을 발행하는 함수는 자동으로 발행할 로또 복권의 수를 지정할 수 있고,
# 번호 6개를 수동 입력한 복수의 로또 복권을 발행할 수 있습니다.

#별표가 매개변수면 가변형으로 직접 넣거나 언팩(*)을 하여 넣어야함
def issue_lottery_tickets(auto_n, *lotteries):
    lottery_tickets = {}
    j = 0
    #자동 번호 입력
    for _ in range(auto_n):
        j += 1
        lottery_tickets[j] = (choose_nums(), '자동')
    #수동 번호 입력
    for i in lotteries:
        j += 1
        lottery_tickets[j] = (sorted(i), '수동')
    return lottery_tickets

while 1:
    stens = input('작업을 선택하세요.[자동/수동]')

    if stens == '자동':
        count = input('반복횟수 입력')
        if count.isnumeric():
            count = int(count)
            break
        else:
            print('입력한 값이 숫자가 아닙니다.')
    elif stens == '수동':
        lottery_num = ()
        num = input("숫자를 입력하세요")
        if num.isnumeric():
            lottery_num

    else:
        print('잘못 선택하셨습니다.')





lottery_nums = [(22, 8, 12, 5, 23, 32), (21, 41, 2, 34, 39, 10)]
lottery_tickets = issue_lottery_tickets(count, *lottery_nums)

# 자동 3개, 수동 2개로 발행된 로또 복권은 다음과 같이 출력됩니다.
# 1:([4, 6, 7, 18, 27, 44], '자동')
# 2:([3, 22, 25, 35, 36, 41], '자동')
# 3:([4, 9, 11, 22, 36, 42], '자동')
# 4:([5, 8, 12, 22, 23, 32], '수동')
# 5:([2, 10, 21, 34, 39, 41], '수동')


for k, v in lottery_tickets.items():
    print(f'{k}:{v}')



"""
>>>date = list('abcdef')
>>>date
['a','b','c','d','e','f']
>>>x, y, *z = date
"""
