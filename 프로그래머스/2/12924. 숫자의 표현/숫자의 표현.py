def solution(n):
    answer = 1
    for i in range(1, n):
        sum = 0
        sum += i
        for j in range(i + 1, n + 1):
            sum += j
            if sum > n:
                break
            elif sum == n:
                answer += 1
                break
    return answer