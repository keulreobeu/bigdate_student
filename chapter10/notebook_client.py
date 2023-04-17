from notebook import Note, NoteBook

n1 = Note('노트1')
n2 = Note('노트2')
n3 = Note('노트3')

nb1 = NoteBook('테스트용')
nb1.add_note(n1, 54)
nb1.add_note(n2, 164)
nb1.add_note(n3)


for i in range(1, 301):
    ki = Note('노트 for {} range'.format(i))
    nb1.add_note(ki)


print(nb1)