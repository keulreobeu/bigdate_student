"""
from roboadvisor.analysis.series import series_test

series_test()

#or

import roboadvisor.analysis.series     #import 뒤에는 클래스 함수만 남아야함.

roboadvisor.analysis.series.series_test()

#or

from roboadvisor.analysis import series     #from다음에는 모듈, 패키지만

series.series_test()

import roboadvisor.analysis.series      #import만 쓰면 모듈만
from roboadvisor.analysis import series     #모듈
from roboadvisor.analysis.series import series_test     #함수 모듈 클래스
"""

import random

random.seed(42)

lotto = random.sample(range(1,46), k=6)
print(sorted(lotto))