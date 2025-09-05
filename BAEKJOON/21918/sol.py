import sys
sys.stdin = open('input.txt', 'r')

N, M = list(map(int, input().split()))
current = list(map(int, input().split()))
current.insert(0, 0)

di = {}
for i in range(1, N+1):
    di[i] = current[i]

# print(di) # {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

def first(x, y):
    di[x] = y

def second(l, r):
    for n in range(l, r+1):
        if di[n] == 0:
            di[n] = 1
        else:
            di[n] = 0

def third(l, r):
    for n in range(l, r+1):
        di[n] = 0

def fourth(l, r):
    for n in range(l, r + 1):
        di[n] = 1

for _ in range(M):
    num, i, j = list(map(int, input().split()))
    if num == 1:
        first(i, j)
    elif num == 2:
        second(i, j)
    elif num == 3:
        third(i, j)
    else:
        fourth(i, j)

print(*di.values())