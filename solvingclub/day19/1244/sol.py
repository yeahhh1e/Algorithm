import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    num, N = map(int, input().split())

    num_list = list(str(num)) # 리스트로 바꿔주기
    # print(num_list)

    cnt = 0 # 변경횟수 저장 변수 설정

    while cnt != N: # cnt가 N이 되면 종료
        # 제일 큰 숫자 찾기
        max_num = num_list[0]
        max_idx = 0
        for i in range(len(num_list)):
            if max_num < num_list[i]:
                max_num = num_list[i]
                max_idx = i

        # 제일 작은 숫자 찾기
        min_num = num_list[0]
        min_idx = 0
        for i in range(len(num_list)):
            if min_num > num_list[i]:
                min_num = num_list[i]
                min_idx = i

        if max_idx != 0: # 첫번째 자리가 아니면 작은 수랑 자리 바꿔주기
            num_list[max_idx], num_list[min_idx] = num_list[min_idx], num_list[max_idx]
            cnt += 1

        # 다음 자리부터
    print(f"#{tc}", *num_list)
