import sys
import pprint
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input())))
    # print(matrix)

    center = N//2
    top = 0
    bottom = N-1
    
    # 가운데 값 계산
    center_sum = 0
    for y in range(N):
        center_sum += matrix[center][y]

    print(center_sum)

    # 왼쪽 값 계산
    for i in range(center): # 더해주는거 0 , 1
        for j in range[center-i:center+i+1] # 열 선택
            matrix[i][] 