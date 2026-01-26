import sys

n = int(input())

points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append([y, x])

points.sort()

for i in range(n):
    print(points[i][1], points[i][0])

# 3'12"