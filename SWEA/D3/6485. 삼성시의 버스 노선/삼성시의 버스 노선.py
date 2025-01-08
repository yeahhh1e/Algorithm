T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt_list = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnt_list[i] += 1

    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))

    print(f'#{tc}', end = ' ')
    for c in C:
        print(cnt_list[c], end=' ')
    print()