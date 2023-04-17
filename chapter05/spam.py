def spam(eggs):
    eggs.append(1)
    eggs = [2, 3]
    eggs_braid = eggs + braid
    print(eggs_braid)

ham = [0]
braid = [2,3,4]
spam((ham))
print(ham)