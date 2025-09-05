for tc in range(1, 11):
    N = int(input())
    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))
    
    cnt = 0 # 교착 상태의 개수를 저장할 변수
    for i in range(100):
        stack = []  # 스택의 처음이 윗쪽
        for j in range(100):    # 각 열을 위에서부터 순회 (윗부분이 스택의 아래에 쌓이게 됨-> 꺼내면 아래 행부터)
            if matrix[j][i] != 0:   # 극이 있을 때만 스택에 추가
                stack.append(matrix[j][i])
        if stack[0] == 2:   # 스택의 처음이 2(S극)이면 삭제
            stack.pop(0)
        elif stack[-1] == 1:  # 스택의 끝이 1(N극)이면 삭제
            stack.pop(-1)

        for x in range(len(stack)): # 스택
            if x+1 < len(stack) and stack[x] == 1 and stack[x+1] == 2: # 인덱스 범위 안이면서 N극+S극 조합이면 cnt+=1
                cnt += 1
                for n in range(x+2):    # 더해준 후 0으로 바꿔줌
                    stack[n] = 0

    print(f"#{tc} {cnt}")