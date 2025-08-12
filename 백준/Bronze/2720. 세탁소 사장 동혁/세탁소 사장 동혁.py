T = int(input())
for _ in range(1, T+1):
    C = int(input())
    
    q = 0
    d = 0
    n = 0
    p = 0

    q = C // 25
    C = C % 25
    
    d = C // 10
    C = C % 10
    
    n = C // 5
    C = C % 5

    p = C // 1
    C = C % 1

    result = [q, d, n, p]
    print(*result)