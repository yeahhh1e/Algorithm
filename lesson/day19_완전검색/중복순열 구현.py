path = []
arr = ['O', 'X']

def run(lev):
    if lev == 3:
        print(path)
        return

    for i in range(2):
        path.append(arr[i])
        run(lev + 1)
        path.pop()

run(0)