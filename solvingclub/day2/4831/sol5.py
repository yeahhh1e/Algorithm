import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))

    result = 0 # 충전횟수
    energy = K  # 충전량

    # 충전기가 설치된 곳을 1로 표기한 정류장 리스트 만들기
    bus_stop = [0] * (N+1)
    current_idx = 0  # 현재 정류장 번호
    for i in M_list:
        bus_stop[i] = 1 # 충전기가 있는 곳의 값을 1로 바꿔주기

    

    while current_idx < N:
        for _ in range(len(bus_stop)):
            for i in range(current_idx + K, current_idx, -1): # 갈 수 있는 거리 K부터 갈 수 있는 정류장을 거꾸로 찾아줌
                if bus_stop[i] == 1:
                    current_idx = i
                    result += 1
                    energy = energy - i + K
                    break

            if energy <= 0:
                result = 0
                break               

    # for _ in range(len(bus_stop)):
    #     energy -= K
    #     current_idx += K
    #     if energy < 0:  # 충전량이 0이 되면 0 반환하고 종료
    #         result = 0
    #         break
    #     elif current_idx >= N:  # 종점까지 가면 종료
    #         break
    #     elif energy == 0:   # 충전량 0인 경우
    #         if bus_stop[current_idx] == 1:  # 충전소면 충전하기
    #             energy += K
    #             result += 1  # 충전횟수 더해주기
    #         else:   # 충전소 아니면 되돌아가기
    #             for n in range(current_idx - K + 1, current_idx):  # -K+1 에서 +1을 해주는 이유: -K를 하면 이전 충전소로 감
    #                 if bus_stop[n] == 1:  # 충전소를 찾으면 되돌아가기
    #                     energy += current_idx - n  # 되돌아간만큼 에너지 더해주기
    #                     energy += K  # 충전하기
    #                     current_idx = n  # 현재위치 변경
    #                     result += 1  # 충전횟수 더해주기
    #     elif energy > 0: # 충전량이 남은 경우
    #         cnt = 0
    #         while cnt == 0: # 충전하면 종료하기
    #             for n in range(current_idx, current_idx +K+1): # 현재 위치부터 더 먼 곳 충전소 찾기
    #                 if current_idx+K+1 <= N and bus_stop[n] == 1:  # 충전소를 찾으면 더 가기
    #                     energy -= n - current_idx # 더 간 만큼 에너지 차감
    #                     energy += K  # 충전하기
    #                     current_idx = n  # 현재위치 변경
    #                     result += 1  # 충전횟수 더해주기
    #                     cnt += 1
    #             for n in range(current_idx - K+1, current_idx):  # 이전 충전소 찾기
    #                 if bus_stop[n] == 1:  # 충전소를 찾으면 되돌아가기
    #                     energy += current_idx - n  # 되돌아간만큼 에너지 더해주기
    #                     energy += K  # 충전하기
    #                     current_idx = n  # 현재위치 변경
    #                     result += 1  # 충전횟수 더해주기
    #                     cnt += 1

    print(f'#{tc} {result}')


