'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

T = int(input()) # 테스트케이스 개수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 초기값 arr[0]으로 두고 리스트를 순회하며 크기를 비교해 큰 값을 max_v에 넣는다
    max_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]:  # 비교문과 할당문의 순서를 맞춰주는 게 좋다
            max_v = arr[i]  # 위와 동일

    min_v = arr[0]
    for i in range(1,N):
        if min_v > arr[i]:
            min_v = arr[i]

    result = max_v - min_v
    print(f'#{tc} {result}')



