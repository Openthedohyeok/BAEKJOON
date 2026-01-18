x = int(input())

n = cnt = 0

while n < x:
    n += cnt
    cnt += 1

if cnt%2 == 0:
    print(f'{(n-x)+1}/{cnt-1-(n-x)}')
else:
    print(f'{cnt-1-(n-x)}/{(n-x)+1}')

# 9'47"
# 지그재그로 숫자가 커진다는 것을 안봐서 처음에 틀림;;