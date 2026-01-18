n, k = map(int, input().split())

res = []
for i in range(1, n+1):
    if n % i == 0:
        res.append(i)
    else:
        pass

try:
    print(res[k-1])
except:
    print('0')

# 5'39"