import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 이진수로 바꿔주기
    # 1. 빼줄 수 있는 가장 큰 제곱수 n 찾기
    max_n = 0
    while M - (2**max_n) >= (2**max_n): # M에서 뺀 값이 뺀 값보다 작을 때가 가장 큰 수
        max_n += 1

    # 2. n부터 시작해서 빼주기
    binary_number = []
    if M == 0: # 만약 M이 0인 경우 이진수 0
        binary_number.append('0')
    while M > 0: # M이 0이 될 때까지
        for i in range(max_n, -1, -1): # 인덱스 max_n부터 0까지 역순으로 순회
            if M - (2**i) >=0: #
                M -= 2**i
                binary_number.append('1')
            else:
                binary_number.append('0')

    # 3. 뒤에서부터 N만큼 1인지 체크하기
    l = len(binary_number)
    check = "ON"
    if l < N:  # 이진수 길이보다 N이 클 경우
        check = "OFF"
    else:
        for idx in range(-1, -N-1, -1):
            if binary_number[idx] == '0':   # 0인 경우 OFF로 바꾸고 종료
                check = "OFF"
                break

    print(f"#{tc} {check}")

