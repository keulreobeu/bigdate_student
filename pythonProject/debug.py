import random

random.seed(11)

data = random.sample(range(1,46),6)
print(data)
result = []
for v in data:
    if v % 2 != 0:
        result.append(v)

#디버그 F8스탭오버: 한개한개 내려감, F7스탭인투: 아래 함수에 들어감.

print(result)