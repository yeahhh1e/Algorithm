import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, N = input().split()
    N = int(N)

    str_list = input().split()
    # print(f'#{test_case}', N, str_list)

    number_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    str_dict = {}
    # 딕셔너리 사용하기
    for k in str_list:
        str_dict.key = number_list[k]
        str_dict.value = 0
    print(str_dict)
    #
    # print(f'#{test_case}')
    # print(*sort_list)
