import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = list(input())
    print(N)
   
    new_N = []
    result = 1
    for i in range(len(N)):
        n = N[i]
        
        if n.find('{'):
            a = n.find('{')
            new_N.append(n[a])
        elif n.find('('):
            a = n.find('(')
            new_N.append(n[a])
        elif n.find('}'):
            if new_N[-1] == '}':
                new_N.pop()
            else:
                result = 0
                break
        elif n.find(')'):
            if new_N[-1] == ')':
                new_N.pop()
            else:
                result = 0
                break
    print(result)


    # for i in range(len(N)):
    #     new_N.append(N[i])
    # print(new_N)
    # stack = []
    # result = 1
    # for i in range(len(N)):
    # a = N.find('(')
    # print(a)

