def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    min_pair = numbers[0] * numbers[1]
    max_pair = numbers[-1] * numbers[-2]
    return max(min_pair, max_pair)