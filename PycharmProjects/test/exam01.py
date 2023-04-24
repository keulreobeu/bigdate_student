# sales.csv 파일은 2020년 ~ 2022년 샘플 매출정보가 담겨있습니다.
# 레코드는 9955건이 있으며, 필드의 순서는 다음과 같으며 ,로 구분되어 있습니다.
# 주문번호,주문일시,주문금액
# 1,2020-01-01 12:09:57,22000
# 2,2020-01-01 13:00:49,112000
# 3,2020-01-01 14:57:56,13000
# ...
# 9954,2022-12-30 19:02:25,176000
# 9955,2022-12-30 19:33:43,142000

import csv
from datetime import datetime

# [문제1: 20점]
# 딕셔너리 내포에서 cvs.reader() 함수로 sales.csv 파일을 읽어들여 딕셔너리 타입의 주문 데이터 객체(data_sales)를
# 생성합니다. 이 때, 주문번호를 키 필드로, 주문일시와 주문금액을 값 필드로 하며, 각 필드의 타입을 다음과 같이 설정합니다.
# 주문일시 필드에 대해서는 datetime.fromisoformat() 함수를 이용해 datetime 객체를 생성합니다.
# *주문번호: int
# *주문일시: datetime
# *주문금액: int
data_sales = None
with open("./data/sales.csv", "r", encoding="utf-8") as f:
    pass

# [문제2: 20점]
# filter() 함수를 사용해 2022년 여름 두 달(7~8월)동안의 데이터만 조회합니다.


# [문제3: 20점]
# data_sales의 주문일시와 주문가격 사이에 분기정보(Q1, Q2, Q3, Q4)를 추가합니다.
# 이 때, 월 정보를 인자로 전달하면 분기 정보를 반환하는 quarter() 함수를 정의해 사용합니다.
def quarter(month):
    pass


# [문제4: 20점]
# map() 함수에서 사용할 quarter_for_map(key) 함수를 정의합니다. quarter_for_map(key) 함수는
# 월 정보(data_sales[key].month)를 이용해 키와 분기 정보를 반환합니다.
# map() 함수를 통해 개별 항목의 키와 분기 정보를 얻어 data_sales의 주문일시와 주문가격 사이에
# 분기정보(Q1, Q2, Q3, Q4)를 추가합니다.

def quarter_for_map(key):
    pass


# [문제5: 20점]
# 다음과 같이 분기정보가 포함된 최종 결과를 출력합니다.
# 1 : 2020-01-01 12:09:57, Q1, 22000
# 2 : 2020-01-01 13:00:49, Q1, 112000
# 3 : 2020-01-01 14:57:56, Q1, 13000
# ...
# 9954 : 2022-12-30 19:02:25, Q4, 176000
# 9955 : 2022-12-30 19:33:43, Q4, 142000