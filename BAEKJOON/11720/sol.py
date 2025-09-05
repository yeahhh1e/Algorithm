import sys
sys.stdin = open("input.txt", "r")

T = int(input())
S = str(input())

n_list = list(map(int, str(S)))
print(n_list)
result = sum(n_list)

print(result)