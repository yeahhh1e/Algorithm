li = list(input().split())

li[0] = int(li[0])
li[1] = int(li[1])

if li[0] > li[1]:
    print('>')
elif li[0] < li[1]:
    print('<')
else:
    print('==')