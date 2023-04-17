for i in range(5):
    if i % 2 == 0:
        continue
    print (i)

    while 1:
        data = input(('데이터를 줘'))
        if data == 'Q':
            break
        print('입력데이터',data)

