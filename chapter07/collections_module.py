''' 이런식으로 사용할꺼면 어디에서 뭘 가져다가 쓸것이다 라고 적어놔야해서 코드가 길어짐.
import collections

deque1 = collections.deque()
'''

from collections import deque   #컬랙션에서 데큐를 꺼내 쓴다는뜻, deque를 바로 사용가능.

deque_list = deque()
for i in range(5):
    deque_list.appendleft(i)

print(deque_list)

queue = deque()
for i in range(5):
    queue.appendleft(i)

print('queue: {}'.format(queue))
queue.rotate(2)
print('queue: {}'.format(queue))

stack = deque()
for i in range(5):
    stack.append(i)

print('stack: {}'.format(stack))
stack.rotate(2)
print('stack: {}'.format(stack))
# queue이냐 stack이냐에 따라 로테이션을 돌리면 값이 다름

def sort_by_key(t):     #sorted는 정렬하는 함수
    return t[0]

from collections import OrderedDict     #dict은 순서가 없지만 순서가 필요하면 ordereddict을 사용한다. 순서를 결정하게 해줄 수 있는 함수가 있다.

d = dict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['i'] = 500

for k,v in OrderedDict(sorted(d.items(),key=sort_by_key)).items():
    #key=에 들어가는 값이 비교를 하는 값을 넣어야함. key로 정렬 -> t[0] value로 정렬 -> t[1]
    print(k, v)
"""
#-----------------------------------------------------------------------------------------------------------------------
import random

random.seed(123)

data = random.choices(range(1,21),k=8)     #복원추출 choices, 비복원추출 sample
print(data)

sorted_data = sorted(data, reverse=True)   #key= none에 두개의 원소를 비교하는 값을 넣어야함. -> 함수를 넣어두됨 / 비교방법 디폴트는 오름차순
print(sorted_data)
#-----------------------------------------------------------------------------------------------------------------------
"""
dict1 = {
    'a': 10,
    'c': 25,
    'b': 4
}
print(dict1)

def by_key(t):
    return t[0]

def by_velue(t):
    return t[1]

print(sorted(dict1.items(), key=by_key))
print(sorted(dict1.items(), key=by_velue))

o_dict1 = OrderedDict(sorted(dict1.items(), key=by_key))
print(o_dict1)
for k, v in o_dict1.items():
    print('{}: {}'.format(k,v))

o_dict1 = OrderedDict(sorted(dict1.items(), key=by_velue))
print(o_dict1)
for k, v in o_dict1.items():
    print('{}: {}'.format(k,v))

score = [90, 80, 70, 60]
new_score = []

for v in score:
    new_score.append(v+5)

print(new_score)

def up_5(x):
    return x + 5

new_score2 =[]

for v in map(up_5, score):
    new_score2.append(v)

print(new_score2)

new_score = list(map(up_5, score))
print(new_score)

new_score = list(map(lambda x: x+5, score))
print(new_score)