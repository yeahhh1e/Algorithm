import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    T = input()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    ladder_list = []
    for i in range(100):
        ladder_list.append(list(map(int, input().split())))

    # 좌표는 ladder_list[x][y] 형식
    # 100번째 행에서 도착점의 y좌표를 찾는다
    for i in range(100):
        if ladder_list[99][i] == 2:
            find_2 = i
            break
    
    # 시작점 설정
    x = 99
    y = find_2

    while x != 0:
        if 0 <= y - 1 < 100 and ladder_list[x][y - 1] == 1:  # 왼쪽 노드가 1이면
            ladder_list[x][y] = 0  # 0으로 바꿔줌
            y -= 1  # 왼쪽으로 이동

        elif 0 <= y + 1 < 100 and ladder_list[x][y + 1] == 1:  # 오른쪽 노드가 1이면
            ladder_list[x][y] = 0  # 0으로 바꿔줌
            y += 1  # 오른쪽으로 이동

        else:  # 양 옆에 1이 없으면 위로 올라간다.
            ladder_list[x][y] = 0
            x -= 1

    print(f'#{T} {y}')









