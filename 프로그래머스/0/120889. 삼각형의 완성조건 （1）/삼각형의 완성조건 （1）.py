def solution(sides):
    answer = 0
    sort_sides = sorted(sides)
    if sort_sides[2] < sort_sides[0] + sort_sides[1]:
        answer = 1
    else:
        answer = 2
    return answer