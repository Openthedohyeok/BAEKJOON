total = int(input())
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    total = total-a*b

if total==0:
    print('Yes')
else:
    print('No')