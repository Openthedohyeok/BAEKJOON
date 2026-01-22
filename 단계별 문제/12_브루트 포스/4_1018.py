import sys

n, m = map(int, sys.stdin.readline().split())

chess_init = []

chess_target1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
chess_target2 = chess_target1[::-1]

for _ in range(n):
    chess_init.append(sys.stdin.readline().rstrip())


num_list = []
for i in range(n-7):
    for j in range(m-7):
        count1 = 0
        count2 = 0  
        for k in range(8):
            for l in range(8):
                if chess_init[k+i][l+j] != chess_target1[k][l]:
                    count1 += 1
                if chess_init[k+i][l+j] != chess_target2[k][l]:
                    count2 += 1
        num_list.append(min(count1, count2))

print(min(num_list))

# 24'18"

