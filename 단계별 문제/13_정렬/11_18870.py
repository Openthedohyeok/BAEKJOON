import sys

n = int(sys.stdin.readline())

list_x = list(map(int, sys.stdin.readline().split()))

sorted_li_x = list(set(list_x))
sorted_li_x.sort()

dict_x = {val: i for i, val in enumerate(sorted_li_x)}

for x in list_x:
    print(dict_x[x], end=' ')

# 아래와 같이 푸니 시간초과가 뜬다...
# import sys

# n = int(sys.stdin.readline())

# list_x = list(map(int, sys.stdin.readline().split()))
# ans = []

# for i in list_x:
#     sort_x = sorted(list_x, key=lambda x: (0 if i>x else 1, x))
#     ans.append(sort_x.index(i))

# index() 함수는 리스트의 처음부터 값을 찾을 때까지 훑기 때문에 그 자체로 $O(N)$입니다.

# print(*ans, sep=' ')

# 27'16"