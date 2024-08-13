import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time_list = list(map(int, input().split()))

    # 도착시간 빠른 순으로 정렬하기
    arrival_time = sorted(time_list)

    result = "Possible"
    
    # 1초마다 붕어빵을 만들고 cnt에 저장해
    # 해당 초에 손님이 왔을 때 붕어빵을 빼
    # 줄 붕어빵이 1개 미만이면 실패
    cnt = 0   # 붕어빵 재고 수량
    sales = 0 # 판매 수량
    for i in range(N): # 마지막 손님이 도착하는 시간까지 만들기
        # 손님이 도착한 시간과 현재 시간 비교
        cnt = arrival_time[i] // M * K
        if cnt < i+1:  # 손님이 도착했을 때
            result = "Impossible"
            break

    print(f'#{tc} {result}')