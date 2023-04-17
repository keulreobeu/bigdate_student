# 비만 계산 방법은 신체질량지수인 BMI(Body Mass Index)에 근거한 방식으로
# BMI= 몸무게(kg) ÷ (신장(m) × 신장(m))입니다.
# 산출된 값이 18.5 이하면 저체중, 18.5 ~ 23은 정상, 23 ~ 25는 과체중,
# 25 ~ 30은 비만, 30이상은 고도비만으로 나누어집니다.
# 주어진 학생들의 정보에서 몸무게(weight)와 키(height) 정보를 이용해
# bmi와 비만 정도를 업데이트 하십시오.
# 이 때, 학생들의 정보(students)는 dict 타입으로 구성하고,
# bmi_level 함수는 BMI를 계산하는 코드, 몸무게, 신장을 인자로 사용합니다.

import random

random.seed(123)
weight = random.choices(range(45, 91), k=40)
height = random.choices(range(150, 191), k=40)
std_no = list(range(1, 41))




def bmi_level(func, w, h):
    bmi = func(w,h)
    leval = '저체중'

    if bmi >= 30:
        leval = '고도비만'
    elif bmi >= 25:
        leval = '비만'
    elif bmi >= 23:
        leval = '과체중'
    elif bmi >= 18.5:
        leval = '정상'

    return (bmi, leval)



students = dict(zip(std_no, zip(weight, height)))
def calc_bmi(w, h):
    return round((w / ((h/100)**2)),2)

for k, v in students.items():
    # bmi, level = bmi_level(calc_bmi,v[0],v[1])
    bmi, level = bmi_level(lambda w, h: round((w / ((h/100)**2)),2),
                           v[0], v[1])
    students[k] = (v[0], v[1], bmi, level)


print(students)

# print(list(zip(weight,height)))
# print(list(zip(std_no, zip(weight, height))))
# print(dict(zip(std_no, zip(weight, height))))

