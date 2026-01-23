import sys

number, b = map(int, sys.stdin.readline().split())

check_num = check_idx = 0

while check_num <= number:
    check_idx += 1
    check_num = pow(b, check_idx)
    
answer_list = []
for i in range(check_idx):
    answer_list.append(number // pow(b, check_idx-i-1))
    number = number % pow(b, check_idx-i-1)

answer = ''
for i in answer_list:
    if i < 10:
        answer += str(i)
    else:
        answer += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i-10]

print(answer)
# answer = ''로 선언하고 answer += str 형식으로 안하고, 
# answer = ''.join(str) 형식으로 해도 된다.

# 17'39"


# # 아래는 제미나이의 아이디어... 진짜 미친듯

# import sys

# n, b = map(int, sys.stdin.readline().split())

# digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# res = []

# # n이 0이 될 때까지 b로 나누며 나머지를 저장
# while n > 0:
#     res.append(digits[n % b])
#     n //= b

# # 리스트에는 낮은 자릿수부터 들어있으므로 뒤집어서 출력
# print(''.join(res[::-1]))