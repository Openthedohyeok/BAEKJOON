import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==b==0:
        break

    q, r = divmod(a, b)
    if q == 0:
        if b%a == 0:
            print('factor')
        else:
            print('neither')
    else:
        if r==0:
            print('multiple')
        else:
            print('neither')

# 4'53"