import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    node_list = [list((input().split())) for _ in range(N)]
    
    left = [0] * (N+1)
    right = [0] * (N+1)
    str_list = [0] * (N+1)
    for i in node_list:
        for j in range(len(i)):
            if j == 0: # 첫 번째는 부모 정점
                str_list[int(i[j])] = i[1] # 부모 정점 값을 2번째 값으로 설정
            elif i[j].isdigit() == True: # 문자열이 아닌 숫자라면 자식 정점이라는 뜻이므로
                if left[int(i[0])] == 0:  # 왼쪽 자식이 없으면 왼쪽 자식에 추가
                    left[int(i[0])] = i[j]
                else:   # 왼쪽이 있으면 오른쪽 자식 추가
                    right[int(i[0])] = i[j]
    # print(left)
    # print(right)
    #
    # print(str_list)
    
    def find_node(x):
        # 왼쪽 자식이 있는지 탐색
        if left[x] != 0:
            find_node(int(left[x])) # 있으면 자식 계속 탐색
        else: # 왼쪽 자식이 없다면
            print(str_list[x]) # 탐색 멈추고 본인 출력
            y = left.index(str(x))
            right_node(y)  # 오른쪽 자식 찾기

    def right_node(y):
        if right[y] != 0: # 오른쪽 자식이 있으면
            find_node(y) # 왼쪽이 있는지 탐색하고
            print(str_list[y])

    print(find_node(1))