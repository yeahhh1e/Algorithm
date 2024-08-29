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

    def cal(x, y, z):
        global result
        if z == "+":
            result = x + y
        elif z == "-":
            result = x - y
        elif z == "/":
            result = z / y
        else:
            result = z * y
        return result

    for i in n_list:
        if len(i) >= 4:
            idx = int(i[0]) # 첫번째 값은 tree의 인덱스
            tree[idx] = i[1]
            left[idx] = i[2] # 자식 노드 추가
            right[idx] = i[3]
        else:
            tree[int(i[0])] = i[1]

    start = 0
    operator_list = ['+', '-', 'x', '/']
    for s in range(1, len(tree)):
        if tree[s] not in operator_list:
            start = s
            break

    left = ""
    right = ""
    total = 0

    def ():
        left = int(tree[s])
        right = int(tree[s+1])
        result = cal(left, right, s//2)

    print(start)
