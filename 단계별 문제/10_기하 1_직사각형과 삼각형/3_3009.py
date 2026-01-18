import sys

# x = y = []
# # 이렇게 하면 절대 안된다 진짜 와
# # 이러면 x 와 y 의 메모리 주소가 같아진다..

x = []
y = []

for _ in range(3):
    tmp_x, tmp_y = map(int, sys.stdin.readline().split())

    x.append(tmp_x)
    y.append(tmp_y)

cnt_x = list(set(x))
cnt_y = list(set(y))

answer = []
for i in cnt_x:
    if x.count(i) == 1:
        answer.append(i)

for j in cnt_y:
    if y.count(j) == 1:
        answer.append(j)

# 이거 x, y 따로 하는거 매우 중요....
# 하나의 반복문에 넣어서 append 해버리면 뭐가 먼저 들어갈지 알 수가 없다      

print(*answer)

# 15'26"