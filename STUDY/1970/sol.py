import sys

sys.stdin = open('input.txt')

# 입력
T = int(input())
lst = []
for _ in range(T): # T 수만큼 단어 입력 받기
    N = int(input())

# 처리
a = 50000
b = 10000 
c = 5000 
d = 1000 
e = 500
f = 100
g = 50
h = 10

lst = [a, b, c, d, e, f, g, h]

while N == 0:
    for i in lst:
        print(N // i)
        N -= (N // i)

  
