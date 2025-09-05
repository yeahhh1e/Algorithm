import sys
sys.stdin = open("input.txt", "r")

# 쿼터 = 25 , 다임 = 10, 니케 =  5, 페니 = 1
# 항상 500 센트 이하, 동전 개수 최소로

T = int(input())
for tc in range(1, T+1):
    C = int(input())
    
    q = 0
    d = 0
    n = 0
    p = 0

    q = C // 25
    C = C % 25
    
    d = C // 10
    C = C % 10
    
    n = C // 5
    C = C % 5

    p = C // 1
    C = C % 1
    
    result = [q, d, n, p]
    print(*result)