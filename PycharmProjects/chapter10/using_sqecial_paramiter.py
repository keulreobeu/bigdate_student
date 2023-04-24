def fn1(a, b, c, d):
    print(a, b, c, d)


fn1(1, 2, 3, 4)
fn1(1, 2, 3, d=4)
fn1(1, b=2, c=3, d=4)
fn1(a=1, b=2, c=3, d=4)


def fn2(a, b, *, c=3, d=4):     #에어 아스타 어쩌구
    print(a, b, c, d)


# fn2(1, 2, 3, 4)
# fn2(1, 2, 3, d=4)
fn2(1, 2, c=3, d=4)
fn2(1, b=2, c=3, d=4)


def fn3(a, b, /, c, d):  # 에어 아스타 어쩌구
    print(a, b, c, d)


fn3(1, 2, 3, 4)
fn3(1, 2, 3, d=4)
fn3(1, 2, c=3, d=4)
#fn3(1, b=2, c=3, d=4)


def fn4(a, b, /, *, c, d):  # 에어 아스타 어쩌구
    print(a, b, c, d)


# fn4(1, 2, 3, 4)
# fn4(1, 2, 3, d=4)
fn4(1, 2, c=3, d=4)
#fn4(1, b=2, c=3, d=4)

