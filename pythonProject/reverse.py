my_sty = input('문자열을 입력하십시오: ')

sty_cnt = len(my_sty)
sty = ''
for i in range(sty_cnt-1, -1 , -1):
    sty += my_sty[i]
print(sty)