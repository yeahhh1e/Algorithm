def KFC(x):
    if x == 2:
        return

    KFC(x+1)
    KFC(x+1)
    print(x)

KFC(0)