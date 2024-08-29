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

    val = 0
    # 제일 마지막 left부터 시작하기
    x = N - 1 # 뒤에서 두번째 숫자가 마지막 left 이므로 left부터 시작하기
    while x > 2:

        result = cal(int(tree[x]), int(tree[x+1]), tree[x//2])
        x = x // 2
        if x * 2 == 0: # 짝수 노드면 result는 왼쪽 자식의 값이므로
            cal(result, int(tree[x+1]), tree[x//2])
        else: # 홀수 노드면 result는 오른쪽 자식 값
            cal(int(tree[x + 1]), result, tree[x // 2])

    print(result)
