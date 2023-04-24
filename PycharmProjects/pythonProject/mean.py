kor_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]
midtrem_score = [kor_score,math_score,eng_score]
subject_cut = len(midtrem_score)
stuent_score = [0, 0, 0, 0, 0]
i = 0
for subject in midtrem_score:
    for score in subject:
        stuent_score[i] += score
        i += 1
    i = 0

for seq, total in enumerate(stuent_score, start=1):
    print(seq, total/subject_cut)