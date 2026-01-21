import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

sum = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            cards_sum = cards[i] + cards[j] + cards[k]
            if cards_sum > sum and cards_sum <= m:
                sum = cards_sum
            else:
                pass

print(sum)

# 9'41"