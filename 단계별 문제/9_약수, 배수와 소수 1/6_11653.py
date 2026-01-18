n = int(input())

while True:
    for i in range(2, n+1):
        if n % i == 0:
            n = n//i
            print(i)
            break
    if n==1:
        break

# 11'34"
# 시간 줄이려면 이것도 역시 제곱근으로 생각해서 풀면 된다...