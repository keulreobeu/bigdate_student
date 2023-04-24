#파일열기 with로
with open('dream.txt','r') as f:
    contents = f.read()
#단어별, 라인별로 쪼개기
word_list = contents.replace('\n', ' ').split(' ')
line_list = contents.split('\n')
#단어수, 라인수가 얼마인지 프린트.
print(len(contents))
print(len(word_list))
print((len(line_list)))