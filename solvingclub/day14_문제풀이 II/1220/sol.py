import sys
sys.stdin = open("input.txt", "r")  

for tc in range(1, 11):
    N = int(input())
    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))
    print(matrix)
    
    cnt = 0
    
    for i in range(100):
        stack = []  # 스택의 처음이 윗쪽
        for j in range(100):    # 각 열을 위에서부터 순회
            if matrix[j][i] != 0:   # 극이 있을 때만 스택에 추가
                stack.append(matrix[j][i])
                # if stack[0] == 2:   # 스택의 처음이 2(S극)이면 삭제
                #     stack.pop(0)
                # # elif stack[-1] == 1:  # 스택의 끝이 1(N극)이면 삭제
                #     stack.pop(-1)
            # for x in range(len(stack)): # 스택
            #     if stack[x] == 2:
            #         if stack[x+1] == 1:
            #             cnt += 1
            #             for n in range(x+1):
            #                 stack.pop(n)
            #         else: # 다음에 파란색이 나온다면
            #             while stack[x+i] != 2:
            #
    print(stack)