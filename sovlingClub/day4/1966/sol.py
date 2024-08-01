import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    number_list = list(map(int, input().split()))

    n = len(number_list)
    # 선택 정렬
    # 최소값의 인덱스 설정
    
    for i in range(n):
        min_idx = i
        
        for j in range(i+1, n):
            if number_list[min_idx] > number_list[j]:
                min_idx = j
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]
 
    print(f'#{test_case}', *number_list)
    # 버블정렬
    # 리스트를 순회하며 다음 값과 비교해 작으면 그대로 냅두고 다음 숫자로 넘어가고
    # 크면 다음 숫자와 자리를 바꾼다
   
    for i in range(n):
        # 배열의 길이 n에서 계속 i의 값과 1을 빼준다
        for j in range(0, n-i-1):
            if number_list[j] >= number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]

    print(f'#{test_case}', *number_list)








