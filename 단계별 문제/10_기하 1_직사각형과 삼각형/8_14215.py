import sys

len_list = list(map(int, sys.stdin.readline().split()))
other_sum = 0

for i in range(3):
    if i == len_list.index(max(len_list)):
        pass
    else:
        other_sum += len_list[i]

if other_sum > max(len_list):
    print(sum(len_list))
else:
    print(other_sum*2-1)

# 8'13"

# 다른 사람의 풀이를 참고하면..
# len_list.sort() 를 사용하면 max 를 찾기 위해 반복문을 사용할 필요 없음
# 그냥 len_list[2] 가 최댓값이 되는거임