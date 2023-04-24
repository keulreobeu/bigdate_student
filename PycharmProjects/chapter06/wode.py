data_str = "  10, 20, 3o, 40, 50  "
data_list = []

data_replace = data_str.replace(" ", "")
print(data_replace)

res_val = data_replace.split(',')
for i, v in enumerate(res_val):
    if v.isdigit():
        data_list.append(int(v))
    else:
        print('[{}]: {}은 숫자포맷이 아닙니다.'.format(i,v))
print(data_list)