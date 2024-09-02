T = int(input()) # 테스트케이스 개수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # max_value 설정
    max_value = arr[0]
    # 리스트를 순회하며 큰 값을 max_value에 넣는다
    for i in range(1, N):
        if max_value < arr[i]: 
            max_value = arr[i]  

    min_value = arr[0]
    # 리스트를 순회하며 큰 값을 min_value에 넣는다
    for i in range(1,N):
        if min_value > arr[i]:
            min_value = arr[i]

    result = max_value - min_value
    print(f'#{tc} {result}')