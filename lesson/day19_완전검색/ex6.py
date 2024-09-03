path = []

def recur(level):
    if level == 3:
        print(*path)
        return
    for i in range(1, 7):
        # if i in path:
        #     continue
        path.append(i)
        KFC(level+1)
        path.pop()

recur(0)