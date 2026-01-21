import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(input())
n0 = int(input())

if (a1 * n0 + a0 <= c * n0) and (a1 <= c):
    print(1)
else:
    print(0)

# 7'44"