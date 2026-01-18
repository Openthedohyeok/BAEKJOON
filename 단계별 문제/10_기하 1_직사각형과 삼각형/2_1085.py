import sys

x, y, w, h = map(int, sys.stdin.readline().split())

dis_list = [x, y, h-y, w-x]

print(min(dis_list))

# 4'38"