num = []
N = 3
def dice(lev, start):
    if lev == N:
        print(*num)
        return

    for i in range(start, 7):
        num.append(i)
        dice(lev + 1, i)
        num.pop()

dice(0, 1)