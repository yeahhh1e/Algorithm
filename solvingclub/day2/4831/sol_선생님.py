import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # K = 한 번에 가는 거리, N = 종점, M = 충전기 설치된 정류장 개수
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))  # 충전소 위치 정보
    # 정류소 만들기
    station = [0 for _ in range(N+1)]
    for i in data:
        station[i] = 1

    # 충전 횟수
    count = 0
    now = K # 현재 위치 -> 처음 = 0 + + 최대 이동 가능 거리
    charge = 0 # 마지막 충전 위치 -> 처음이니까 0
    while now < N:
        if station[now] == 1:   # 현재 위치에 충전소가 있으면
            count += 1 # 충전한다 += 1
            charge = now
            now += K   # 현재 위치 + 최대 이동거리
        else:
            now -= 1
        # 마지막 충전소까지 다시 후진했으면, 실패
        if charge == now:
            count = 0
            break
    print(count)