T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))

    # 도착시간 빠른 순으로 정렬하기
    sorted_time = sorted(arrive_time)
    a = float(K/M) # 1초당 만들 수 있는 붕어빵의 갯수

    result = "Possible"
    # 1초마다 붕어빵을 만들고 cnt에 저장해
    # 해당 초에 손님이 왔을 때 붕어빵을 빼
    # 줄 붕어빵이 1개 미만이면 실패
    cnt = 0
    sales = 0
    for i in range(0, sorted_time[-1]+1): # 마지막 손님이 도착하는 시간까지 만들기
        cnt += a    # 1초마다 붕어빵 만들기
        for j in sorted_time: # 손님이 도착한 시간과 현재 시간 비교
            if i == j:  # 손님이 도착했을 때
                if i < M:   # 다 못 만들었는데 손님이 도착했을 때
                    result = "Impossible"
                    break
                elif cnt >= 1: # 1개 이상 남아있을 때
                    if (j / M * K - sales) >= 1:
                        cnt -= 1
                        sales += 1 # 판 고객 수 증가
                else:
                    result = "Impossible"
                    break


    print(f'#{tc} {result}')