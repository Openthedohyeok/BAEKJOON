import sys

while True:
    len_list = list(map(int, sys.stdin.readline().split()))
    
    if len_list == [0, 0, 0]:
        break

    tri_check = []
    for s in len_list:
        tri_check.append(s)
    tri_check.remove(max(len_list))

    if max(len_list) >= sum(tri_check):
        print('Invalid')
    else:
        if len(set(len_list)) == 1:
            print('Equilateral')
        elif len(set(len_list)) == 2:
            print('Isosceles')
        else:
            print('Scalene ')

# 13'31"