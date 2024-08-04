import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str_list = []
    for _ in range(0,2):
        str = input()
        str_list.append(str)
    # str_list = lst+lst2
    # print(str_list)
    str1 = list(str_list[0])
    str2 = list(str_list[1])

    # print(str1, str2)

    # str_dict = {}
    # for i in range(len(str1)):

    #     for j in str1:

    #         str_dict.setdefault(j, 0)
    # print(str_dict)

    max_cnt = 0
    for i in range(len(str1)):
        a = str1[i]
        cnt = 0
        for j in range(len(str2)):
            if a == str2[j]:
                cnt += 1

        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{test_case} {max_cnt}')