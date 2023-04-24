def f(x):
    y = x
    x = 5
    return y*y

x = 3
ret_vel = f(x)
print(f(x))
print(x)