import sys

n = int(sys.stdin.readline())

count = [0 for _ in range(10001)]

for _ in range(n):
    count[int(sys.stdin.readline())] += 1

num = 0
for i in count:
    for _ in range(i):
        print(num)
    num += 1

# 카운팅 정렬을 사용하여 메모리 사용 최소화..
# sys 내장함수 활용하여 시간도 최소화...

# 2'11" - 기존 방식은 메모리 초과 : list 에 N을 천만개를 담아버리니 그럴 수 밖에
