import sys

a, b = sys.stdin.readline().split()

rev_a = int(a[::-1])
rev_b = int(b[::-1])

print(max(rev_a, rev_b))

# 아래는 내가 푼 멍청한 풀이....
# 위에는 제미나이가 풀어준 풀이. 사실 저렇게 풀었어야 했다. 오늘 복습도 했잖아.
# a, b = map(list, sys.stdin.readline().split())

# a.reverse()
# b.reverse()

# new_a = new_b =''

# for i in range(3):
#     new_a += a[i]
#     new_b += b[i]

# print(max(int(new_a), int(new_b)))