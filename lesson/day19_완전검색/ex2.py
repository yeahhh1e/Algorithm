def func(x):
    x += 1

x = 10 # 함수의 x와 다른 메모리
func(x)
print(x)

def func(x):
    x[0] += 1

x = [10] # 함수의 x와 주소값이 같은 메모리
func(x)
print(x)

