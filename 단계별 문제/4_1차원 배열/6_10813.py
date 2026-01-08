n, m = map(int, input().split())
basket = [x+1 for x in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    # temp = basket[i-1]
    # basket[i-1] = basket[j-1]
    # basket[j-1] = temp
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

# for i in range(n):
#     print(basket[i], end=' ')
    
print(*basket)
