import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    subset_list = list(map(int, input().split()))
    print(subset_list)

    N = subset_list[0]
    subset_sum = subset_list[1]
    n = subset_sum - N

    total = [0] * (n+2)
    for i in range(1, n):
        total[0] = i
        for j in range(1, n):
            total[1] = j
            for x in range(1, n):
                total[2] = x
                for y in range(1, n):
                    total[3] = y
                    for z in range(1, n):
                        total[4] = z

                        print(total)  
    # n = subset_sum - N
    # print(n)
    # total = []
    # # for i in range(1, n): # i의 크기는 1과 subset_sum-N 사이
    # #     total.append(i)
    # #     for j in range(i+1, n):
    # #         if subset_sum - i - j > 0:
    # #             total.append(j)
    # #         elif subset_sum - i - j < 0:
    # #             total.pop[-2]
    # #         else:
    # #             total.append(j)
    # #             print(total)
    # print(total)

            
    # while total != subset_sum:
    #     if i in range(1, subset_sum) 


