import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) # 방 길이
    box_list = list(map(int, input().split()))
    print(box_list)

    max_drop = 0
    for i in range(len(box_list)):
        cnt = 0 # 자신보다 같거나 높은 층 찾기
        for j in range(i+1, len(box_list)):
            if box_list[i] <= box_list[j]:
                cnt += 1

        # 처음 높이 = 방 길이(N) - i(인덱스)
        # 낙차 = 처음 높이 - 나보다 같거나 큰 수의 개수(cnt) - 1
        drop = N - i - cnt - 1

        if max_drop < drop:
            max_drop = drop

    print(f'#{test_case} {max_drop}')