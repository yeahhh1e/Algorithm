N = int(input())
li = [list(input().split()) for _ in range(N)]
di = {}
cnt = 0

for i in li:
    if not di.get(i[0]):
        di[i[0]] = i[1]
    elif di[i[0]] != i[1]:
        cnt += 1
        di[i[0]] = i[1]

print(cnt)