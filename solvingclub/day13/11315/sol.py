import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append((list(input())))
    # print(matrix)
    def find_five_o(matrix):
        global check
        check = 0
        while check == 5:
            for i in range(N):
                for j in range(N):
                    cnt = 0
                    if matrix[i][j] == 'o':
                        for x, y in ((i, j+1), (i+1, j), (i, j-1), (i-1, j), (i+1, j+1)):
                            cnt += 1
                            check = 0
                        if matrix[x][y] == 'o': 
                                if cnt == 1:    # 오른쪽으로 다섯개인지 체크
                                    for m in range(5):
                                        if matrix[x][y+m] == 'o':
                                            check += 1
                                elif cnt == 2: # 아래쪽으로 다섯개인지 체크
                                    for m in range(5):
                                        if matrix[x+m][y] == 'o':
                                            check += 1
                                elif cnt == 3:    # 왼쪽으로 다섯개인지 체크
                                    for m in range(5):
                                        if matrix[x][y-1] == 'o':
                                            check += 1
                                elif cnt == 4:    # 위로 다섯개인지 체크
                                    for m in range(5):
                                        if matrix[x-1][y] == 'o':
                                            check += 1
                                elif cnt == 5: # 대각선으로 다섯개인지 체크
                                    for m in range(5):
                                        if matrix[x+m][y+m] == 'o':
                                            check += 1
        if check == 5:
            result = 'YES'
        else:
            result = 'NO'

        return result

    print(find_five_o(matrix))
                                

                        
