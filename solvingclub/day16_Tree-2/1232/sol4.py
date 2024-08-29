import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**7)
for tc in range(1, 11):
    N = int(input())
    n_list = [list(map(str, input().split())) for _ in range(N)]
    # print(n_list)
    n = len(n_list)
    left = [0] * (n+1)
    right = [0] * (n+1)
    tree = [0] * (n+1)

    for i in n_list:
        if len(i) >= 4:
            idx = int(i[0]) # 첫번째 값은 tree의 인덱스
            tree[idx] = i[1]
            left[idx] = int(i[2]) # 자식 노드 추가
            right[idx] = int(i[3])
        else:
            tree[int(i[0])] = int(i[1])

    def postorder(node):
        if node == 0:  # 자식이 없으면  패스
            return
        # 후위 순회
        left_node = postorder(left[node])
        right_node = postorder(right[node])

        if tree[node] == "+":
            tree[node] = left_node + right_node
        elif tree[node] == "-":
            tree[node] = left_node - right_node
        elif tree[node] == "/":
            tree[node] = left_node / right_node
        elif tree[node] == "*":
            tree[node] = left_node * right_node

        return tree[node]

    print(f"#{tc} {int(postorder(1))}")
