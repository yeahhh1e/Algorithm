import sys
sys.stdin = open("input.txt", "r")

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort() # [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]

M = int(input())
M_list = list(map(int, input().split())) # ['10', '9', '-5', '2', '3', '4', '5', '-10']

for m in M_list:
    print(N_list.count(m), end=" ")