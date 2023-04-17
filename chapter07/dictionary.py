x = { 'a': 1, 'b': 2, 'c': 3}

for k in x:   #key만 나옴
    print(k)

for k in x.keys():  #key를 불러와 그걸로 밸류를 불러옴
    print('{}: {}'.format(k, x[k]))

for k, v in x.items():  #튜플로 불러와 언패킹해서 사용
    print('{}: {}'.format(k, v))

for t in x.items():     #튜플로 불러와 튜플의 인덱스로 값을 불러옴
    print('{}: {}'.format(t[0], t[1]))


list1 = list(range(1,11))

print(list1)

list2 = []

for i in list1:
    if i % 2 == 0:
        list2.append(i)

print(list2)

list3 = [v for v in list1 if v % 2 == 0]   #list, set, tuple, dictionary등 사용 가능.

print(list3)

dict1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

dict2 = {}

for k, v in dict1.items():
    dict2[k] = v

print(dict2)

dict3 = {k:v for k,v in dict1.items()}

print(dict3)

itmes = [('a', 1),('b', 2),('c', 3)]
dict4 = dict(itmes)
print(dict4)

key = list('abc')   #['a', 'b', 'c']

velue = list(range(1,4))    #[1, 2, 3]

data = []
for t in zip(key, velue):
    data.append(t)

print(data)

dict5 = {}

dict5 = dict(data)
print(dict5)