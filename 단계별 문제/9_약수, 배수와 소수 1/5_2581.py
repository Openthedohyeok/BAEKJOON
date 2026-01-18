m = int(input())
n = int(input())
res = []
for i in range(m, n+1):
    
    cnt = 0
    for j in range(1, i+1):
        if i%j == 0:
            cnt += 1
        if cnt > 2:
            break
    if cnt == 2:
        res.append(i)

if res:
    print(sum(res))
    print(res[0])
else:
    print('-1')

# 5' 51"



# 시간을 줄이는 법 : 제곱근까지만 약수를 계산
# 아래는 내 스타일대로 위의 내용을 구현한 코드

# m = int(input())
# n = int(input())
# res = []
# for i in range(m, n+1):
    
#     if i == 1:
#         continue
    
#     is_prime = True
#     for j in range(2, int(i**0.5)+1):
#         if i%j == 0:
#             is_prime = False
#             break

#     if is_prime:
#         res.append(i)

# if res:
#     print(sum(res))
#     print(res[0])
# else:
#     print('-1')
