import player

'''     #@propoty하기 전 코드
son = player.SoccerPlayer('Son', 'RW', 10)
print('현재 선수의 등번호는:', son.__back_number)
print(son)
print('이름: {}'.format(son.get_name()))
print('이름: {}'.format(son.__name))

print('위치: {}'.format(son.get_position()))
print('위치: {}'.format(son.__position))

son.set_position('CF')

print('위치: {}'.format(son.get_position()))
print('위치: {}'.format(son.__position))

son.__position = 'GN'

print('위치: {}'.format(son.get_position()))
print('위치: {}'.format(son.__position))
'''

son = player.SoccerPlayer('Son', 'RW', 10)
print('현재 선수의 등번호는:', son.back_number)
print(son)

print('이름: {}'.format(son.name))

print('위치: {}'.format(son.position))

print('위치: {}'.format(son.position))

son.position = 'GN'


print('위치: {}'.format(son.position))
print("-------------------------")      #이름을 알면 접근이 가능하긴 함.
print(son._SoccerPlayer__name)
print(son._SoccerPlayer__position)
print(son._SoccerPlayer__back_number)