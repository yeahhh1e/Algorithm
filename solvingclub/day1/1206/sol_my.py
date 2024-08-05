import sys
sys.stdin = open("input.txt", "r")


for test_case in range(1, 11):
    N = int(input())
    n_list = list(map(int, input().split()))

    n = len(n_list)
    # 총 층 수 저장하는 변수 total_count 설정
    total_count = 0
    for i in range(2, n-2): # 양쪽 두 칸을 제외한 세 번째 칸부터 끝에서 세 번째 칸까지를 기준 인덱스 i로 설정
        min_count = n_list[i] # 0으로 설정시 초기값이 너무 적어 min_count가 저장되지 않게 되므로 처음 빌딩 높이로 정해줌
        for j in range(i-2, i+3): # i 기준 양 쪽 두 칸을 검사하며 결국 검사는 제시된 모든 칸을 다 하게 됨
            if i == j: # 둘이 같은 칸일 경우 검사 x
                continue
            elif n_list[i] > n_list[j]: # i칸 층이 j칸 층보다 더 높은 경우
                if min_count > n_list[i] - n_list[j]: # 층의 차이가 최소값인 min_count에 저장된 수 보다 작은 경우만 저장
                    min_count = n_list[i] - n_list[j]
            else: # i층보다 j층이 높은 경우 조망권 없으므로 min_count를 0으로 초기화 하고 for문 종료
                min_count = 0 # 아래 total에 더해줘야 되므로 n_list[i]로 하면 안 됨 어차피 다시 n_list[i]로 초기화 시켜줌
                break
        total_count += min_count
    print(f'#{test_case} {total_count}')