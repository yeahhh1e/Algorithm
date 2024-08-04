import sys
sys.stdin = open("input.txt", "r")


for test_case in range(1, 11):
    N = int(input())
    num_list = list(map(int, input().split()))
    # print(num_list)

    # 버블정렬
    # for i in range(len(num_list)):
    #     for j in range(i+1, len(num_list)):
    #         if num_list[i] > num_list[j]:
    #             num_list[i], num_list[j] = num_list[j], num_list[i]
    
    # for n in range(0, N): # 덤프횟수 N
    #     num_list[n] += 1
    #     num_list[-(n+1)] -= 1
    
    # print(num_list)

     # 버블정렬 함수
    def sort_arr(arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

    
    # def find_max(arr):
    #     for i in range(len(arr)):
    #         for j in range(i+1, len(arr)):
    #             if arr[i] > arr[j]:
    #                 arr[i], arr[j] = arr[j], arr[i]
    #     return arr[-1]

    # 리스트를 덤프횟수만큼 계속 정렬하며 최소값 +1, 최대값 -1을 해준다
    for i in range(1, N+1):
        sort_arr(num_list)
        num_list[0] += 1
        num_list[-1] -= 1

    sort_arr(num_list)
    result = num_list[-1] - num_list[0]
    print(f'#{test_case} {result}')



