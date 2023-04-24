from collections import defaultdict     #딕셔너리의 디폴트 값을 설정할 수 있음

d = defaultdict(lambda: 0)
print(d["first"])

from collections import Counter     #빈도분석 딕셔너리로 값이 나옴

text = list('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur accumsan laoreet leo non ultrices. Praesent porttitor convallis laoreet. Maecenas sit amet sagittis nisi. Nunc rutrum, turpis et dapibus sagittis, orci ligula dapibus orci, a tempor nunc orci at dolor. Vivamus sollicitudin odio vitae neque malesuada ornare. Vestibulum ac ipsum urna. Donec lectus nisi, commodo at enim vel, tincidunt ullamcorper odio. Sed pellentesque laoreet accumsan. Morbi id lacus nulla. Proin quis ipsum blandit, vestibulum felis in, aliquet leo. Fusce nulla ipsum, faucibus ut maximus in, semper id mi. Duis vitae gravida purus. Nulla facilisi. Suspendisse potenti. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.')

c = Counter(text)
print(c)

print(sorted(c.items(), key=lambda x: x[0]))
print(sorted(c.items(), key=lambda x: x[1], reverse=True)[:5])

"""print(list(c.elements()))#실제 값을 카운터로 생성할 수 있음
"""
#카운터에서 나온 값은 같은 키끼리 연산가능

from collections import namedtuple      #이름을 부여한 튜플 -> 객채처럼 만들어서 사용 가능
Point = namedtuple('Point',['x','y'])
P = Point(11, y=22)
print(p)