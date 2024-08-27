'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# left, right 를 쓰는 버전
# 단, 입력이 반드시 각 노드당 최대 2번 씩만 들어온다고 가정한 코드
# 전위 순회 (나 -> 왼쪽 -> 오른쪽)
def preorder(node):
    if node == 0: # 자식이 없으면  패스
        return
    print(node, end=' ') # 전위 순회
    preorder(left[node])
    # print(node, end=' ') # 중위 순회 -> 왼쪽을 보고 나서, 본인을 확인
    preorder(right[node])
    # print(node, end=' ') # 후위 순회 -> 왼쪽, 오른쪽 자식들을 모두 보고 나서, 본인을 확인

N = int(input())        # 정점의 개수. 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장 (1부터 시작하므로 +1)
# ex) left[3] = 2 => 3번 부모의 왼쪽 자식은 2다.
right = [0]*(N+1)       #
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장


for i in range(0, len(arr), 2):
    parent, child = arr[i], arr[i+1]

    # 왼쪽 자식이 없다면, 왼쪽에 삽입
    if left[parent] == 0:
        left[parent] = child
    # 왼쪽 자식은 있는데, 오른쪽 자식이 없다면 오른쪽 삽입
    else:
        right[parent] = child


root = 1 # 시작점은 1이다라고 가정.
preorder(root)