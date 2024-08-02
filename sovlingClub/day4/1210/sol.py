import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    T = input()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    ladder_list = []
    for i in range(100):
        ladder_list.append(list(map(int, input().split())))
    # print(ladder_list)
    # print(len(ladder_list))
    # print(ladder_list[99][99])

    # 좌표는 ladder_list[x][y] 형식
    # 도착점 X의 좌표 = ladder_list[99][99]
    # 도착점 X에서 시작할 것이므로 초기 값 x, y를 99로 설정
    x = 99
    y = 99
    # print(ladder_list[x][y-1])
    # print(ladder_list[x-4][y-1])
    # while x != 0: # x가 0이 되면 시작점을 찾으므로 종료
    #     if 0 <= y-1 < 100 and ladder_list[x][y-1] == 1:
    #         y -= 1
    #     elif 0 <= y+1 < 100 and ladder_list[x][y+1] == 1:
    #         y += 1
    #     elif y-1 < 0 or y-1 >= 100:
    #         pass
    #     elif y+1 < 0 or y+1 >= 100:
    #         pass
    #     else:
    #         x -= 1


    # print(123)
    # while x != 0:
    #     if 0 <= y-1 < 100 and ladder_list[x][y-1] == 1:
    #         y -= 1
    #     elif 0 <= y+1 < 100 and ladder_list[x][y+1] == 1:
    #         y += 1
    #     elif y-1 < 0:
    #         ladder_list[x][y] = 0
    #         x -= 1
    #     elif y+1 >= 100:
    #         ladder_list[x][y] = 0
    #         x -= 1
    #     else: # 양 옆에 1이 없으면 위로 올라간다.
    #         ladder_list[x][y] = 0
    #         # print(ladder_list[x][y])
    #         x -= 1
    #         # ladder_list[x+1][y] = 0 # 다시 못돌아가게 0으로 바꿔버리기
    #     # print(ladder_list[x][y])

    # print(f'#{T} {y}')




