import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for a in range(1, T+1):
    test_num = int(input())
    test_case = [list(map(int, input().split())) for _ in range(100)]

    i = len(test_case) # 행의 수
    j = len(test_case[0]) # 열의 수

    max_sum = 0
    
    # 행들의 합 중 최대값 구하기
    for x in range(i):
        # 행들의 총합을 저장하는 변수 sum_row 설정
        sum_row = 0
        for y in range(j):
            # 리스트를 순회하며 각 행의 값들을 더해준다
            sum_row += test_case[x][y]
        # sum_row의 최댓값을 max_sum에 저장    
        if max_sum < sum_row:
            max_sum = sum_row
    # print(max_sum)


    # 열들의 합 중 최대값 구하기
    for y in range(j):
        # 열들의 총합을 저장하는 변수 sum_col 설정
        sum_col = 0
        for x in range(i):
            # 리스트를 순회하며 각 열의 값들을 더해준다
            sum_col += test_case[x][y]
        # sum_row의 최댓값을 max_sum에 저장    
        if max_sum < sum_col:
            max_sum = sum_col
    # print(max_sum)
    
    # 대각선의 합 구하기
    sum_cross = 0
    for x in range(i):
        sum_cross += test_case[x][x]
    if max_sum < sum_cross:
            max_sum = sum_cross
    pprint(max_sum)

    # 반대 대각선의 합 구하기
    sum_reverse_cross = 0
    for x in range(i):
        
        sum_reverse_cross += test_case[x][-(x+1)]
    if max_sum < sum_reverse_cross:
            max_sum = sum_reverse_cross
    print(f'#{a} {max_sum}')