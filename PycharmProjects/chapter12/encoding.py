with open('count_log.txt', 'w', encoding='utf8') as f:
    for i in range(1,11):
        data = f"{i}번째 줄이다.\n"
        f.write(data)

with open('count_log.txt', 'a', encoding='utf8') as f:
    for i in range(1,11):
        data = f'{i}번째 줄이다.\n'
        f.write(data)

with open('count_log.txt', 'r', encoding='utf8') as f:
    contents = f.read()
    print(contents)