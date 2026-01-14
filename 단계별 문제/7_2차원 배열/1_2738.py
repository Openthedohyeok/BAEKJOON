import sys

n, m = map(int, input().split())

A = []
B = []

for _ in range(n):
    A.append(list(sys.stdin.readline().split()))

for _ in range(n):
    B.append(list(sys.stdin.readline().split()))

for i in range(n):
    for j in range(m):
        print(int(A[i][j]) + int(B[i][j]), end=' ')
    print('')

# 7' 42"