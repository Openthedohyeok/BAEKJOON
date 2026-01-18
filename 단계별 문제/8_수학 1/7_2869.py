import sys

a, b, v = map(int, sys.stdin.readline().split())

q, r = divmod(v-a, a-b)

if r == 0:
    print(q+1)
else:
    print(q+2)

# 15'44"
# 다시 푸는데 걸린 시간


# 6' 44"
# # 아래와 같은 방법으로 했더니 시간초과 뜸...
# cnt = h = 0

# while True:
#     h += a
#     cnt += 1
#     if h >= v:
#         break
#     h -= b