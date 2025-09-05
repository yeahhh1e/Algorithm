import sys
sys.stdin = open('input.txt')

N = int(input())
li = [list(input().split()) for _ in range(N)]
print(li) # [['3', '1'], ['3', '0'], ['6', '0'], ['2', '1'], ['4', '1'], ['3', '0'], ['4', '0'], ['3', '1']]
di = {}
cnt = 0

for i in li:
    if not di.get(i[0]):
        di[i[0]] = i[1]
    elif di[i[0]] != i[1]:
        cnt += 1
        di[i[0]] = i[1]

print(cnt)