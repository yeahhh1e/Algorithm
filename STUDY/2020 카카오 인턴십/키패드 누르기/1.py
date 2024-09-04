# keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
#
# print(keypad.index(1))

def find_idx(number): # 위치 찾는 함수
    global x
    global y
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    for i in range(len(keypad)):
        for j in range(len(keypad[0])):
            if keypad[i][j] == number:
                x, y = i, j
    return x, y

print(find_idx(1))