n = int(input())

paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            paper[j][i] += 1

sum = cnt = 0

for i in range(100):
    for j in range(100):
        if paper[j][i] > 1:
            sum += paper[j][i]
            cnt += 1

print(100*n-sum+cnt)

# 30분 초과 ㅠ.. 아래 때문임. 자세한 내용은 txt 참조
# paper_row = [0 for _ in range(100)]
# paper = [paper_row for _ in range(100)]



# # 아래와 같이 집합을 사용해서 푼 사람도 있다..
# N = int(input())
# covered = set()

# for i in range(N):
#     x, y = map(int,input().split())
#     for j in range(x,x+10):
#         for k in range(y,y+10):
#             covered.add((j,k))
# print(len(covered))



