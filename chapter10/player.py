class SoccerPlayer(object):
    def __init__(self, name, position, back_number):     #셀프, 매개변수들
        self.__name = name
        self.__position = position
        self.__back_number = back_number
        #속성 = 매개변수 / 앞에 __을 넣으면 프라이빗으로 되어 클레스 외부에서 접근을 막을 수 있음.

    @property       #읽는용도로만 사용 가능
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    @position.setter    #쓰기가 가능하게.
    def position(self,new_position):
        if new_position.isalpha():
            self.__position = new_position
        else:
            raise ValueError('알파벳만 사용 가능합니다.')

    @property
    def back_number(self):
        return self.__back_number

    def __str__(self):
        return "name: {}, position: {}, back_number: {}"\
            .format(self.__name, self.__position, self.back_number)

if __name__ == '__main__':   #실행모듈 ,매인에서 실행을 했을때 호출함. 없으면 import한 파일에서도 실행됨.
    son = SoccerPlayer('Son', 'RW', 10)
    #print('현재 선수의 등번호는:', son.__back_number)
    print('현재 선수의 등번호는:', son.back_number)
    print(son)  #뒤에 아무것도 안적었을때 .__str__()가 호출됨
    son.position = 'CF'
    print('포지션은 {}입니다.'.format(son.position))
