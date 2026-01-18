import sys

n = int(input())
x = []
y = []

for _ in range(n):
    tmp_x, tmp_y = map(int, sys.stdin.readline().split())
    x.append(tmp_x)
    y.append(tmp_y)

print((max(x)-min(x))*(max(y)-min(y)))

# 3'39"