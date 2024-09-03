N = 3
path = []


def run(lev, start):
    if lev == N: # level: 몇 번째 주사위
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        run(lev + 1, i) # 중복이 가능하므로 i로 넘겨줌 (중복 불가 -> i+1)
        path.pop()


run(0, 1)
