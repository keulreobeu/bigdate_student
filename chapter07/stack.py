word = input("적어라 단어")

word_list = list(word)
print(word_list)

result = []
cnt = len(word_list)
for _ in range(cnt):
    pop = word_list.pop()
    result.append(pop)

print(result)
print(word[::-1])