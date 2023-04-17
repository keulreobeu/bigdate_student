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

students = {}


def bmi_level(func, w, h):
    for i in func:
        wet = w[i-1]
        hit = h[i-1]/100
        BMI = wet / (hit*hit)

        if BMI <=18.5:
            students[i] = [f'몸무게:{wet}kg', f'키:{hit}m', f'BMI는 {BMI:.1f}로 저체중 입니다.']

        elif BMI <=23:
            students[i] = [f'몸무게:{wet}kg', f'키:{hit}m', f'BMI는 {BMI:.1f}로 정상 입니다.']

        elif BMI <=25:
            students[i] = [f'몸무게:{wet}kg', f'키:{hit}m', f'BMI는 {BMI:.1f}로 과체중 입니다.']

        elif BMI <=30:
            students[i] = [f'몸무게:{wet}kg', f'키:{hit}m', f'BMI는 {BMI:.1f}로 비만 입니다.']

        else:
            students[i] = [f'몸무게:{wet}kg', f'키:{hit}m', f'BMI는 {BMI:.1f}로 고도비만 입니다.']

bmi_level(std_no, weight, height)


print(students)