import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    knm_list = list(map(int, input().split()))
    K = knm_list[0]
    N = knm_list[1]
    M = knm_list[2]
    print(K, N, M)
    M_list = list(map(int, input().split()))

    print(M_list)
    result = 0
    energy = K  # 충전량
    current_idx = 0 # 현재 정류장 번호
    # 빈리스트를 만들어볼까
    def bus(K, N):
        global energy
        global current_idx
        global result
        min_idx = M_list[0]  # 첫 충전소 위치로 기본 설정

        for i in range(N):
            energy -= K # K만큼 이동
            current_idx += K    # K만큼 이동
            if current_idx in M_list:   # 만약 이동했는데 충전소면 충전하기
                energy += K
                result += 1

            elif current_idx not in M_list: # 이동했는데 충전소가 아니면
                # 제일 가까운 다음 충전소 찾기
                for m in range(len(M_list)):
                    if current_idx < min_idx: # 첫 충전소를 더 가야된다면 0
                        result = 0
                    elif current_idx > min_idx: # 첫 충전소를 지나쳤다면
                        if current_idx - min_idx
                    if current_idx > M_list[m]: #충전소를 지나친 경우
                        current_idx = M_list[m] # 전의 충전소로 돌아간다
                        energy += (current_idx -  M_list[m])
                        result += 1
                    elif current_idx < M_list[m]: # 현재 위치보다 충전소가 더 먼 경우
                        result = 0


            else:   # 충전소가 아닌 경우
                for m in range(len(M_list)):
                    if current_idx < M_list[m]: # 현재 위치보다 충전소가 더 멀은 경우
                        result = 0
                    elif current_idx > M_list[m]: #충전소를 지나친 경우
                        current_idx = M_list[m] # 전의 충전소로 돌아간다
                        energy += (current_idx -  M_list[m])
                        result += 1

    print(result)


