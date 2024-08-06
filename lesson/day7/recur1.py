def f(n):
    global cnt
    cnt += 1

    if n == 0: # 재귀함수는 중단하는 조건을 먼저 적고 진행해야 함
        return
    else:
        return f(n-1)

cnt = 0
f(5)
print(cnt)