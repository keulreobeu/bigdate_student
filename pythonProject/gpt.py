'''data = []
def duplicate_check(STR):
    for i in range(len(STR)):
        if STR[i] in data:
            print('True')
            return True
        elif i == len(STR)-1:
            print('False')
            return False
        else:
            data.append(STR[i])
            print(data)'''

'''def duplicate_check(string):
    char_set = [False for _ in range(128)] # ASCII 코드에 해당하는 리스트
    for char in string:
        val = ord(char)
        if char_set[val]:
            return True
        char_set[val] = True
    return False
'''


def duplicate_check(string):
    data = []
    print(string)
    data.extend(string)
    print(data)
    for i in string:
        for i in data:

            return True
        print(i)

    return False





print(duplicate_check('qwertyuiopasdfhjklzxcvbnm1234567890'))
print(duplicate_check('world'))
print(duplicate_check('asdoo'))
