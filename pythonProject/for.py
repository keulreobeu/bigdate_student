data = [1,2,3,4,5]

for _ in data:
    print('변수를 안쓰면 _를 사용, 관용적 사용임. 변수다.')

for v in data:
    print(v)

for idx, v in enumerate(data, start=2):
    print(idx, v)

for t in enumerate(data):#튜플로 반환함, 변수 두개를 넣으면 언패킹과 같음
    print(t, t[0], t[1])