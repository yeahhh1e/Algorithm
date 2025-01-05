def left_find_idx(number): # 왼손 위치 찾는 함수
    global l_x
    global l_y
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    for i in range(len(keypad)):
        for j in range(len(keypad[0])):
            if keypad[i][j] == number:
                l_x, l_y = i, j
                break
    return l_x, l_y

def right_find_idx(number): # 오른손 위치 찾는 함수
    global r_x
    global r_y
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    for i in range(len(keypad)):
        for j in range(len(keypad[0])):
            if keypad[i][j] == number:
                r_x, r_y = i, j
                break
    return r_x, r_y

def solution(numbers, hand):
    global x
    global y
    answer = ''
    l_x, l_y = 3, 0
    r_x, r_y = 3, 2

    for n in numbers:
        l_cnt = 0
        r_cnt = 0
        if n in [1, 4, 7] : # 왼손
            answer += 'L'
            l_x, l_y = left_find_idx(n)

        elif n in [3, 6, 9]: # 오른손
            answer += 'R'
            r_x, r_y = right_find_idx(n)

        else: # 2, 5, 8, 0 인 경우
            if n == 2:
                n_x, n_y = 0, 1 # 2의 좌표
            elif n == 5:
                n_x, n_y = 1, 1  # 5의 좌표
            elif n == 8:
                n_x, n_y = 2, 1  # 8의 좌표
            else:
                n_x, n_y = 3, 1  # 0의 좌표
            l_cnt += abs(n_x - l_x) + abs(n_y - l_y)
            r_cnt += abs(n_x - r_x) + abs(n_y - r_y)

            if l_cnt < r_cnt: # 왼손이 더 가까운 경우
                answer += 'L'
                l_x, l_y = n_x, n_y
            elif l_cnt > r_cnt: # 오른손이 더 가까운 경우
                answer += 'R'
                r_x, r_y = n_x, n_y
            else: # 같은 경우
                if hand == 'left': # 왼손잡이면
                    answer += 'L'
                    l_x, l_y = n_x, n_y
                else:   # 오른손잡이면
                    answer += 'R'
                    r_x, r_y = n_x, n_y

    return answer