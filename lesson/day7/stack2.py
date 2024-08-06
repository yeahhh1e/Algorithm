def f2(d, c):
    return d - c

def f1(b, a):
    c = b + a # 30
    d = 10
    return f2(c, d)

a = 10
b = 20
print(f1(a, b)) # 20