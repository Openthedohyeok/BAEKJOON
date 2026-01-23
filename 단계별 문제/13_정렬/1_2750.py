n = int(input())

num_list = []

for _ in range(n):
    num_list.append(int(input()))

for i in range(n):
    print(sorted(num_list)[i])

# 3'02"