import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    binary_number = ""
    for i in range(1, 14):  # 문제에는 13자리 이상이라고 써있지만 14자리 이상으로 생각하고 풀어야됨
        if N == 0: # 0이 되면 종료
            break
        elif N - 2**(-i) >= 0: # 뺄 수 있으면 빼고 1 표시
            N -= 2**(-i)
            binary_number = binary_number + str(1)
        elif N - 2**(-i) < 0:   # 뺄 수 없으면 0 표시하고 넘어가기
            binary_number = binary_number + str(0)
    else:   # N == 0이 되지 않아 for 문이 break를 못 만났을 경우 overflow
        binary_number = "overflow"

    print(f"#{tc} {binary_number}")