"""
다음의 요구사항을 만족하는 로또 번호 생성 OOP 프로그램을 완성합니다.

1. main 모듈 시작 시 로또번호개수, 시작번호, 끝번호가 입력되지 않았을 경우
   다음과 같은 메시지가 출력되면서 프로그램이 종료됩니다.

   사용법: python main.py 로또번호개수 시작번호 끝번호
   예: python main.py 6 1 45

2. main 모듈에서 Lotto 클래스로 생성한 lotto 객체의 로또번호개수(lotto_n),
   시작번호(start), 끝번호(end) 프로퍼티를 각각 출력합니다.

3. main 모듈에서 Lotto 클래스로 생성한 lotto 객체를 print() 함수로 출력합니다.

4. main 모듈에서 다음과 같이 정렬된 로또 번호를 출력합니다.
   예: [2, 13, 19, 37, 41, 44]

"""
import sys
from lotto import Lotto

print(sys.argv)
data = sys.argv

try:
    lotto_n = (int(sys.argv[1]))
    start = (int(sys.argv[2]))
    end = (int(sys.argv[3]))

except ValueError:
    print('숫자만 입력해주세요.')
    print('사용법: python main.py 로또번호개수 시작번호 끝번호\n예: python main.py 6 1 45')
    exit()
except IndexError:
    print('숫자를 전부 입력해주세요.')
    print('사용법: python main.py 로또번호개수 시작번호 끝번호\n예: python main.py 6 1 45')
    exit()


lotto = Lotto(lotto_n, start, end)
print(lotto.lotto_n)
print(lotto.start)
print(lotto.end)
print(lotto)
print(lotto.generate_nums())