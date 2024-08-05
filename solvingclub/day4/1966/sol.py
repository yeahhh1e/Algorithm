import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    number_list = list(map(int, input().split()))

    n = len(number_list)
    # 선택정렬
    for i in range(n):
        # 최소값의 인덱스 설정
        min_idx = i
        
        for j in range(i+1, n): # i인덱스의 다음부터 리스트의 끝까지 순회한다
            # 최소값의 인덱스의 값이 인덱스 j의 값보다 크면
            if number_list[min_idx] > number_list[j]: # number_list[i]로 비교하면 i 값 고정되어서 갱신된 최소값 인덱스랑 비교 할 수 없음
                # 최소값의 인덱스를 i에서 j로 바꿔준다
                # 리스트의 끝까지 순회하며 제일 최소값의 인덱스인 j를 찾는다
                min_idx = j
        # 찾은 인덱스 j와 i인덱스 값의 위치를 서로 바꿔줘 최소값이 앞으로 가게 바꿈        
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]
 
    print(f'#{test_case}', *number_list)
    # 버블정렬
    # 리스트를 순회하며 다음 값과 비교해 작으면 그대로 냅두고 다음 숫자로 넘어가고
    # 크면 다음 숫자와 자리를 바꾼다
   
    for i in range(n):
        # 배열의 길이 n에서 i의 값과 1을 빼준다
        for j in range(0, n-i-1):
            if number_list[j] >= number_list[j+1]:                                                                                                                                                                                                 
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]

    print(f'#{test_case}', *number_list)








