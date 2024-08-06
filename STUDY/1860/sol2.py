import sys
sys.stdin = open("input3.txt", "r")

T = int(input())
for tc in range(1, T+1):
    nmk_list = list(map(int, input().split()))
    arrive_time = list(map(int, input().split()))

    N = nmk_list[0] # 손님 총 수
    M = nmk_list[1] # 만드는 데 걸리는 시간
    K = nmk_list[2] # M초의 시간당 만들 수 있는 붕어빵

    # print(N, M, K)

    # 도착시간 빠른 순으로 정렬하기
    sorted_time = sorted(arrive_time)
    # print(sorted_time)
    a = float(K/M) # 1초당 만들 수 있는 붕어빵의 갯수
    # print(a)

    result = "Possible"
    
    # 1초마다 붕어빵을 만들고 cnt에 저장해
    # 해당 초에 손님이 왔을 때 붕어빵을 빼
    # 줄 붕어빵이 1개 미만이면 실패
    cnt = 0   # 붕어빵 재고 수량
    sales = 0 # 판매 수량
    for i in range(1, sorted_time[-1]+1): # 마지막 손님이 도착하는 시간까지 만들기
        cnt += a    # 1초마다 붕어빵 만들기
        for j in sorted_time: # 손님이 도착한 시간과 현재 시간 비교
            if i == j:  # 손님이 도착했을 때
                if j < M:   # 다 못 만들었는데 손님이 도착했을 때
                    result = "impossible"
                    break
                elif j < a * j:
                    result = "impossible"
                elif 1 and (j / M - sales) >= 1: # 1개 이상 남아있고 도착시간/만드는데 걸리는 시간 - 판매수량 >=1 이상일때만
                    cnt -= 1
                    sales += 1
                    sorted_time.pop(0)
                else:
                    result = "impossible"
            else:
                break

    print(f'#{tc} {result}')