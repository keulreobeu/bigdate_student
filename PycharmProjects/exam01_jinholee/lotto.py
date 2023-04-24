"""
1. lotto 모듈의 Lotto 클래스는 로또번호개수, 시작번호, 끝번호를 필드으로 가지며
   필드가 외부에 공개되지 않도록 로또번호개수(lotto_n), 시작번호(start), 끝번호(end)
   읽기 전용의 프로퍼티를 제공합니다.

2. Lotto 클래스의 generate_nums 인스턴스 메서드는 로또번호개수, 시작번호, 끝번호
   필드를 이용해 로또번호 리스트 객체를 반환합니다.

3. Lotto 클래스로 생성한 객체 lotto를 print() 함수로 출력하면,
   로또번호개수가 6, 시작번호가 1, 끝번호가 45일 경우
   "로또 번호 1 ~ 45 가운데 6개의 번호를 생성합니다."를 출력할 수 있도록 합니다.
"""
import random


class Lotto(object):

    def __init__(self, lotto_n, start, end):
        self.__lotto_n = lotto_n
        self.__start = start
        self.__end = end

    @property
    def lotto_n(self):
        return self.__lotto_n

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    def generate_nums(self):
        lotto_nums = []
        lotto_nums = random.sample(range(self.__start, self.__end + 1), k=self.__lotto_n)
        print(f'로또 번호 {self.__start} ~ {self.__end} 가운데 {self.__lotto_n}개의 번호를 생성합니다.')
        return sorted(lotto_nums)

    def __str__(self):
        return  f'로또번호 개수 : {self.__lotto_n}, 시작번호 : {self.__start} 끝번호 : {self.__end}'


if __name__ == '__main__':
    lotto_list = Lotto()
    print(lotto_list.generate_nums(6,1,45))



# lotto_nums = []
# def lotto(lotto_n, start, end):
#     lotto_nums = random.sample(range(start, end+1), k=lotto_n)
#     return sorted(lotto_nums)
#
# print(lotto(6, 1, 45))