n, m = map(int, input().split())
basket = [0]*n
# basket = 0 for x in range(n) 이라고도 적을 수 있다.

for i in range(m):
    i, j, k = map(int, input().split())
    for x in range(i-1,j):
        basket[x] = k

for i in range(n):
    print(basket[i], end=' ')
