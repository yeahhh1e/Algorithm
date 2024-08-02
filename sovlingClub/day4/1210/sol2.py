import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    T = input()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    ladder_list = []
    for i in range(100):
        ladder_list.append(list(map(int, input().split())))


    # 좌표는 ladder_list[x][y] 형식
    # 도착점 X의 좌표 = ladder_list[99][99]
    # 도착점 X에서 시작할 것이므로 초기 값 x, y를 99로 설정
    x = 99
    y = 99


    # 델타 이용하기





