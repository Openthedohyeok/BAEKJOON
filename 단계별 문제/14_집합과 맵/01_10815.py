import sys

n = int(sys.stdin.readline())
cards_set = set(map(int, sys.stdin.readline().split()))
# list 로 받아버리면 밑에 반복문에서 i in cards_list 로 찾을 때 cards_list 자체의 복잡도 n 을 가져버린다
# set 을 사용하면 데이터가 아무리 많아도 O(1) 만에 값을 찾는다.

m = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

for i in num_list:
    if i in cards_set:
        print(1, end=' ')
    else:
        print(0, end=' ')

# 5'32" -> 시간 초과 ㅠ