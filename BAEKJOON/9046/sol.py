import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    sentence = str(input())
    s_list = list(map(str, sentence))

    max = -1
    most = '?'
    check = True

    for x in s_list:
        if x == ' ':
            continue
        cnt = 0
        for y in range(len(s_list)):

            if x == s_list[y]:
                cnt += 1
        if max < cnt:
            max = cnt
            most = x
            check = True

        elif max == cnt and most != x:
            check = False

    if check == True:
        print(most)
    elif check == False:
        print('?')


