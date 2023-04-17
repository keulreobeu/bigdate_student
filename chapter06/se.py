"""data = [1,2,3,4,5]

data\
    .append([6,7,8])

print(data)"""

f = open("yesterday.txt",'r')
Yester = f.readlines()
f.close()

contents = ""
for line in Yester:
    contents = contents + line.strip() + "\n"
    print(contents)

n_of_Yester=contents.upper().count("YESTERDAY")
print("예스터데이 개수는", n_of_Yester)