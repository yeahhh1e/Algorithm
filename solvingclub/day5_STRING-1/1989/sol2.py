# 초심자의 회문 검사
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    s = input()
    N = len(s)
    ans = 1
    for i in range(N//2):   # i의 범위는 0부터 N//2-1임. 중간 전까지 탐색
        if s[i] != s[N-1-i]: # 앞부터 비교하다가 불일치하면 break로 종료
            ans = 0
            break
    print(f'#{tc} {ans}')
