import sys

n, m = map(int, sys.stdin.readline().split())

ans_set = set()
check_list = []

for _ in range(n):
    ans_set.add(sys.stdin.readline().rstrip())

for _ in range(m):
    check_list.append(sys.stdin.readline().rstrip())

ans = 0
for i in check_list:
    if i in ans_set:
        ans += 1

print(ans)

# 처음에는 둘다 set 으로 선언해서 풀었는데 틀렸다
# 뒤에 주어지는 문자열은 중복되는게 없다는 말이 없기 때문에 중복을 허용해야 한다.

# 6'20"