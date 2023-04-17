import sys

# if __name__ == '__main__':      #이모듈이 메인으로 시작했다면.
#     print(f'{type(sys.argv)}, {sys.argv}')
#
# for i, v in enumerate(sys.argv):
#     print(f'[{i}]: {v}')

def cale_sum(*args):       #*는 포지셔널 배리어블 아규먼트,  들어가면 포지셔널은 튜플로  키워드는 딕셔너리 형태로 들어감.
    total = 0
    for v in args:
        total += v
    return total

print(cale_sum(1, 2))
print(cale_sum(1, 2, 3))
print(cale_sum(1, 2, 3, 4, 5))