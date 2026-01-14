import sys

max_val = -1
max_idx = [0, 0]

for i in range(9):
    num_list = list(map(int, sys.stdin.readline().split()))

    if max(num_list) > max_val:
        max_val = max(num_list)
        max_idx[0] = i+1
        max_idx[1] = num_list.index(max_val)+1

print(max_val)
print(max_idx[0], max_idx[1])

# 5' 12"

# 모든 숫자가 0일때... 를 고려하여 max_val = -1 로 설정한다..