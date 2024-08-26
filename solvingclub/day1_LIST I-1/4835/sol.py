import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    M = lst[1]
    number_lst = list(map(int, input().split()))

    n = len(number_lst)
    # 구간 수만큼 합한 것을 초기 최소,최댓값으로 놓기 (구간수대로 안 더하면 최소,최대값이 비교가 안 됨)
    min_sum = sum(number_lst[:M]) 
    max_sum = sum(number_lst[:M])

    # 리스트를 순회하며 더하기
    # 최소값이면 최소값에 저장 최대값이면 최대값에 저장
    for i in range(0, n-M+1):
        total = 0
        for j in range(i, i+M):
            total += number_lst[j]
       
        if min_sum > total:
            min_sum = total

        if max_sum < total:
            max_sum = total

    result = max_sum - min_sum
    print(f'#{test_case} {result}')
    