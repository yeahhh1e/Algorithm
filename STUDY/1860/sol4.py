import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))

    # 도착시간 빠른 순으로 정렬하기
    arrival_time = sorted(arrive_time)

    result = "Possible"

    # 1초마다 붕어빵을 만들고 cnt에 저장해
    # 해당 초에 손님이 왔을 때 붕어빵을 빼
    # 줄 붕어빵이 1개 미만이면 실패
    cnt = 0  # 붕어빵 재고 수량

    for i in range(arrival_time[-1] + 1):  # 마지막 손님이 도착하는 시간까지 만들기
        if i > 0 and i % M == 0:
            cnt += K
        for j in arrival_time:  # 손님이 도착한 시간과 현재 시간 비교
            if i == j:  # 손님이 도착했을 때
                if cnt <= 0:
                    result = "Impossible"
                    break
                elif cnt >= 1:
                    cnt -= 1
                    arrival_time.pop(0)

                else:
                    result = "Impossible"

    print(f'#{tc} {result}')