import sys
sys.stdin = open("input.txt", "r")

pascal = []

for i in range(1, 11):
    pascal.append([1]*i) # 1로 채운 길이가 10인 삼각형 미리 만들어 놓기

for i in range(2, 10): # 세번째 줄부터 바꾸기
    for j in range(1, i): # i번째 줄의 j번째 숫자를 i-1까지만 바꾸기
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j] # 해당 값을 인덱스 [i-1][j-1] + [i-1][j]를 더한 값으로 바꿔준다

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = pascal[0:N]
    print(f'#{tc}')
    for str in result:
        print(*str)
