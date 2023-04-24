def print_someting(my_name,your_name='teamlb'):
    print(f'hello {your_name},my name is {my_name}.')



print_someting('Sungshul','TEAMLAB')
print_someting(your_name = 'Sungshul',my_name = 'TEAMLAB')
print_someting('Sungshul',your_name ='TEAMLAB')
#print_someting(your_name ='Sungshul','TEAMLAB') 키워드뒤에 포지셔널을 넣을 수 없음.
print_someting('Sungsul')
#print_someting(your_name ='TEAMLAB') my_name은 기본값이 없어서 실행 안됨.

def asterisk_test(a,b,*args):
    print(f'a:{a} b: {b}')
    for i,v in enumerate(args):
        print(f'[{i}]: {v}')


asterisk_test(1,2,3,4,5,6,7,8,range(5))


# def keargs_test(**kwargs):
#     print(kwargs)
#     print('first value is {first}'.format(**kwargs))
#     print('Second value is {second}',format(**kwargs))
#     print('thord value is {third}'.format(**kwargs))
#
# keargs_test(first = 3, second = 4, third = 5)

def test(**kwargs):
    print(kwargs)
    for x in kwargs:
        print(x)
    for x in kwargs.items():
        print(x)
    for k, v in kwargs.items():
        print('"{}":{}'.format(k,v))


test(a=1,b=2,c=3)