import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number_list = list(input())
    
    max_v = 0
    for i in range(N):
        cnt = 0
        check = True
        if number_list[i] == '1':
            while check == True:
                if check == False:
                    break
                for j in range(i, N):
                    if number_list[j] == '1':
                        cnt += 1
                    else:
                        check = False
        if max_v < cnt:
            max_v = cnt

print(max_v)