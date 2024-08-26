import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())    # 건물 갯수
    arr = list(map(int, input().split()))

    result = 0
    for i in range(2, N-2): # 양 끝 두 자리 무시
        # 현재 조사 대상의 높이
        tmp = arr[i]
        # 양 쪽 두 칸씩 검사
        for j in range(i-2, i+3):
            if i == j:  # 나랑 비교할 필요 없음 -> 건너뛴다
                continue

            # 단축평가로, 양쪽 조망권이 확보 되었고,
            # AND 현재 검사 대상의 높이와 양 쪽 두 칸과의 차가 더 작으면
            if arr[i] > arr[j] and tmp > arr[i] - arr[j]: # 왼쪽이 false면 오른쪽 확인 x (단축평가)
                tmp = arr[i] - arr[j]
            # 나보다 양 옆 건물이 같거나 큰 경우가 한 번이라도 있으면,
            elif arr[i] <= arr[j]:
                # tmp 갱신할 필요 x
                break   # 다음 건물로 검사 넘기기
        else:
            result += tmp


