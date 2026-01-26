import sys

n = int(input())

points = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append([x, y])

points.sort()

for i in range(n):
    print(f'{points[i][0]} {points[i][1]}')





# try 1
# import sys
# _, *coord_list = sys.stdin.read().rstrip().split('\n')
# print(*sorted(coord_list), sep='\n')
# 이렇게 할 경우 문자열을 기준으로 정렬하게 되어 '10 3' 이 '2 -1' 보다 빨리 나오는 불상사 발생

# 9'54"