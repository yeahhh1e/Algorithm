T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lst= list(map(int, input().split()))
    N = lst[0]
    M = lst[1]
    matrix = []
    for _ in range(N):
        matrix_lst = list(map(int, input().split()))
        matrix.append(matrix_lst)

    max_sum = -99999 # 최대합 저장할 변수 설정
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            total = 0 # 총 합한 값 저장할 변수 설정

            for x, y in ((i, j), (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]): # 인덱스 범위 내만 더해줌
                    total += matrix[x][y]
            if max_sum < total: 
                max_sum = total
               
    print(f'#{test_case} {max_sum}')