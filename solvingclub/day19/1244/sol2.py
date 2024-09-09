import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    num, N = map(int, input().split())

    num_list = list(str(num)) # 리스트로 바꿔주기
    # print(num_list)
    cnt = 0
    # 제일 큰 수와 제일 작은 수 자리 바꾸는 함수
    def max_money(start):
        global cnt
        if cnt == N:
            return num_list

        # 제일 큰 숫자 찾기
        max_num = num_list[start]
        max_idx = start
        for i in range(start, len(num_list)):
            if max_num <= num_list[i]: # 제일 뒤에 있는 수로 바꾸기
                max_num = num_list[i]
                max_idx = i

        # 큰 숫자가 제일 앞인 경우..(맨앞이 이미 같은 숫자면 다음자리부터)
        if max_idx != 0: # 첫번째 자리가 아니면 작은 수랑 자리 바꿔주기
            num_list[max_idx], num_list[0] = num_list[0], num_list[max_idx]
            cnt += 1
        else:
            max_money(start+1)

        # 제일 작은 숫자 찾기
            min_num = num_list[start]
            min_idx = start
            for i in range(start, len(num_list)):
                if min_num > num_list[i]:
                    min_num = num_list[i]
                    min_idx = i


        # 다음 자리부터

    max_money(0)

    print(f"#{tc}", *num_list)
