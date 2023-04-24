try:

    while True:
        value = input("정수 입력")
        for i in value:
            if i not in '0123456789':
                raise ValueError("숫자가 아님")
        print(int(value))

except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)
else:
    print('예외가 발생 안함')      #절대 실행 안되는 데드코드
finally:
    print('항상 수행되는 코드')