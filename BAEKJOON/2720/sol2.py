import sys
sys.stdin = open("input.txt", "r")

# 쿼터 = 25 , 다임 = 10, 니케 =  5, 페니 = 1
# 항상 500 센트 이하, 동전 개수 최소로

T = int(input())
coins = [25, 10, 5, 1]

for _ in range(T):
    C = int(input())
    result = []

    for coin in coins:
        result.append(C // coin)
        C = C % coin
        
    print(*result)