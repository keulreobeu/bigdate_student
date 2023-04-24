list = [1,2,1,2,1,2,1,2,1,2,1,2,1]
list2 = []

def serch(list, number):
    lists=list.count(number)
    x = 0
    for i in range(lists):
        y=list.index(number,x)
        y2 = str(y)+'번'
        list2.append(y2)
        x = y+1
    if list2 == []:
        print('값이 없습니다.')
    else:
        print('찾으시는 값은 총',len(list2),'개 있고.')
        print('인덱스 값은', end=' ')
        for i in range(len(list2)):
            if i == len(list2)-1:
                print(list2[i], end='입니다.')
            else:
                print(list2[i],end=', ')
serch(list,1)