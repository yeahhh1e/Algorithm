N = int(input())
result = []

def push(stack, num):
    stack.append(num)

def pop(stack):
    try:
        print(stack.pop())
    except:
        print(-1)

def size(stack):
    print(len(stack))

def empty(stack):
    if not stack:
        print(1)
    else:
        print(0)

def top(stack):
    if not stack:
        print(-1)
    else:
        print(stack[-1])

for _ in range(N):
    line = input().split()
    if line[0] == 'push':
        push(result, line[1])
    elif line[0] == 'pop':
        pop(result)
    elif line[0] == 'size':
        size(result)
    elif line[0] == 'empty':
        empty(result)
    elif line[0] == 'top':
        top(result)