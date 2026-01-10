import sys

t= int(input())

for _ in range(t):
    r, s = sys.stdin.readline().split()
    for i in s:
        print(i*int(r),end='')
    print('')
    # print(''.join(i * r for i in s)) 라고 쓸수도 있다.