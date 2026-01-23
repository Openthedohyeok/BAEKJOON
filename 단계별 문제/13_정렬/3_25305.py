import sys

n, k = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))

print(sorted(scores)[::-1][k-1])

# 3'33"