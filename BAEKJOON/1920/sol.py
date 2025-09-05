import sys
sys.stdin = open("input.txt", "r")

N = int(input())
N_list = list(input().split())

M = int(input())
M_list = list(input().split())

for m in range(len(M_list)):
    cnt = 0
    for n in N_list:
        if M_list[m] == n:
            cnt += 1
    M_list[m] = cnt # N 리스트에 있는 수만큼 바꿈

print(*M_list, sep="\n")

# 시간 초과