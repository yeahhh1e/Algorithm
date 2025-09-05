def solution(numbers):
    new_numbers = sorted(numbers) 
    return new_numbers[-1] * new_numbers[-2]
