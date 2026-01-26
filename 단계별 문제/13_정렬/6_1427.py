import sys

n = sys.stdin.readline().rstrip()

print(*sorted(n)[::-1], sep='')

# 2'56"