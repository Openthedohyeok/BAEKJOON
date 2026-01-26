import sys

n = int(sys.stdin.readline())

info = []
for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    info.append([int(age), name, i])

info.sort(key = lambda x:(x[0], x[2]))

for j in range(n):
    print(info[j][0], info[j][1])

# 4'37"

# x[2] 를 쓰지 않아도! x[0] 기준으로만 sort 하고 다른 것은 그대로 냅두기 때문에
# 굳이 x[2] 를 해주지 않아도 된다!
# 아래와 같이 가능. 그러면 시간이 더 줄어들겠지.
# import sys

# n = int(sys.stdin.readline())

# info = []
# for _ in range(n):
#     age, name = sys.stdin.readline().rstrip().split()
#     info.append([int(age), name])

# info.sort(key = lambda x: x[0])

# for j in range(n):
#     print(info[j][0], info[j][1])