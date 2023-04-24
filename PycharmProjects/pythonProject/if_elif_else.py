import time

score = int(input('점수를입력하세요: '))
if score >= 90:
    grned = 'A'
elif score >=80:
    grned = 'B'
elif score >=70:
    grned = 'C'
elif score >=60:
    grned = 'D'
else:
    grned = 'F'

print(grned)

year = input('태어난 연도를 입력하세요.: ')
age = 2023 - year + 1
if 20 <= age <= 26:
    print('대학생')
elif 20 < age <= 17:
    print('고등학생')
elif 17 < age <= 14:
    print('중학생')
elif 14 < age <= 8:
    print('초등학생')
else:
    print('학생이 아닙니다.')