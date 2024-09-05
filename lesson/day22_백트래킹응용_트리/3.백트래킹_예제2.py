# 1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
# 단, 순서에 따른 중복을 제거하세요
arr = [i for i in range(1, 11)]
visited = []
path = []

# 버전1
def dfs(level, sum, idx): # idx의 의미: 현재 수보다 작은 수들은 이미 고려가 되었음. 파라미터로 후보군 없애주기
    # 가지치기 : 합이 10이면 종료
    if sum == 10:
        print(*visited)                 # 기저조건: 문제에서 발견하기 힘든 경우가 많다.
        return

    # 가지치기 : 10이상의 숫자면 볼 필요 없음
    if sum > 10:
        return

    for i in range(idx, len(arr)): # idx보다 작은 후보들은 pass
        # 가지치기 : 이미 사용한 숫자라면 생략     # 후보군: 방문처리, 예시
        if arr[i] in visited:
            continue

        visited.append(arr[i])
        dfs(level + 1, sum + arr[i], i)
        visited.pop()


# 버전2
# 트리 구조처럼 사용하면 훨씬 쉽고 빠르다
# 후보를 사용하느냐 마느냐
def dfs2(level, sum):
    if sum > 10:
        return

    if sum == 10:
        print(*path)
        return

    # 모두 선택하지 않으면 합이 10이 넘지 못하므로
    # 기저조건 추가
    if level == len(arr):
        return

    # 선택하는 경우
    visited.append(arr[level])
    dfs2(level + 1, sum + arr[level]) # level을 올리면서 가므로 이전 것들은 다음 케이스에서 고려되지 않음
    visited.pop()

    # 현재 숫자를 선택하지 않는 경우
    dfs2(level + 1, sum)


# dfs(0, 0, 0)
dfs2(0, 0)