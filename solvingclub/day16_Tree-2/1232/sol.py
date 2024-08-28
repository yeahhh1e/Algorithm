import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**7)
for tc in range(1, 11):
    N = int(input())
    n_list = [list(map(str, input().split())) for _ in range(N)]

    n = len(n_list)
    left = [0] * (n+1)
    right = [0] * (n+1)
    tree = [0] * (n+1)

    for i in n_list:
        if len(i) >= 4:
            idx = int(i[0]) # 첫번째 값은 tree의 인덱스
            tree[idx] = i[1]
            left[idx] = i[2] # 자식 노드 추가
            right[idx] = i[3]
        else:
            tree[int(i[0])] = i[1]

    value_list = []
    def find_node(x):
        # 1. 자식 찾기
        # 왼쪽 자식이 있는지 탐색
        if left[x] != 0:
            find_node(int(left[x]))  # 있으면 자식 계속 탐색
            return tree[x]
        # 왼쪽 없으면 오른쪽 탐색
        elif right[x] != 0:
            if tree[x] != 0:
                value_list.append(tree[x])
            tree[x] = 0  # 다시 탐색 방지 위해 0으로 바꿔줌
            find_node(int(right[x]))  # 얘도 자식이 있는지 확인
        else:  # 2. 자식이 없다면 부모 탐색
            if str(x) in left:  # x를 왼쪽 자식으로 갖고 있으면
                q = left.index(str(x))  # 부모 노드 값 q를 설정
                if q != 0:
                    if tree[x] != 0:  # 위로 올라가기 전에 출력
                        value_list.append(tree[x])
                    tree[x] = 0
                    left[q] = 0
                    find_node(q)  # q의 다른 자식 있는지 찾기
            elif str(x) in right:  # x를 오른쪽 자식으로 갖고 있으면
                q = right.index(str(x))
                if q != 0:
                    if tree[x] != 0:
                        value_list.append(tree[x])
                    tree[x] = 0
                    right[q] = 0
                    find_node(q)
    find_node(1)
    # print(value_list)
    total = 0
    for v in range(len(value_list)):
        if value_list[v].isdigit(): # 숫자면 total에 더해주기
            total += int(value_list[v])
        else:   # 연산자인 경우
            if value_list[v] == '-':    # - 라면
                total -= 2*(int(value_list[v+1])) # 숫자 오면 더해줄 거므로 미리 두 배 빼주기
            elif value_list[v] == '+':  # - 라면
                pass # 이따 더해줄 거므로 패스
            elif value_list[v] == 'x':    # x 라면
                total = (total * int(value_list[v+1])) - int(value_list[v+1]) # 숫자 오면 더해줄 거므로 미리 빼주기
            else:
                total = (total // int(value_list[v+1])) - int(value_list[v+1])

    print(total)
