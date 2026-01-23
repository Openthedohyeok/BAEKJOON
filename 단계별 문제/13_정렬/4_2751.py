import sys
n = int(input())

num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

for i in num_list:
    print(i)

# 1'33" -> 시간 초과;;
# 아래와 같이 하면 반복문 돌때마다 정렬을 해야하므로 시간이 엄청 배가 된다.
# for i in range(n):
#     print(sorted(num_list)[i])

# 다른 사람의 풀이 참고
# import sys
# _, *num = map(int,sys.stdin.read().split())
# print(*sorted(num), sep='\n')