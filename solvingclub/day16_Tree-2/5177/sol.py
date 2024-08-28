import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))

    heap = [0] * (N+1) # node 번호와 인덱스 맞추기 위해 N+1개의 배열 만들어줌

    for i in range(len(n_list)):
        if i == 0: # 처음은 우선 값을 저장
            heap[i + 1] = n_list[i]
        else:
            heap[i + 1] = n_list[i]
            j = i + 1 # heap과 맞춰주기 위해 +1
            while j >= 1:
                if heap[j] < heap[j // 2]: # 부모가 더 크면 바꾸기
                    heap[j], heap[j // 2] = heap[j // 2], heap[j]
                j = j // 2  # 부모 값으로 바꿔서 계속 검사

    # 마지막에 저장한 값의 조상 찾기
    last_node = heap[-1]
    sum_heap = 0
    n = N # 마지막 노드부터 탐색
    while n >= 1:   # 루트까지 더했다면 종료하기
            n = n // 2
            sum_heap += heap[n]

    print(f"#{tc} {sum_heap}")