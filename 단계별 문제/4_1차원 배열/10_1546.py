import sys

n = int(input())
score = list(map(int, sys.stdin.readline().split()))
sum = 0

for i in range(n):
    sum += 100*score[i]/max(score)
    
print(sum/n)