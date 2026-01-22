n = int(input())

for i in range(1, n+1):
    if i + sum(list(map(int, str(i)))) == n:
        print(i)
        break
    if i == n:
        print(0)

# 10'11"