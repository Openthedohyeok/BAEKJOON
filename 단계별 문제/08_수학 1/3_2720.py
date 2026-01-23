n = int(input())

current = [25, 10, 5, 1]

for i in range(n):
    money = int(input())

    answer = [0, 0, 0, 0]
    while money != 0:
        i = 0
        for m in current:
            if money // m > 0:
                answer[i] = money//m
                money -= m*(money//m)
            i += 1

    print(*answer)

# 23'28"
# answer = [0 0 0 0] 선언을 global 에 해둬서 for 문 돌때마다 0000 으로 초기화가 되지 않는 탓에... 계속 기존 답에 쌓여서 출력됨..

# # 아래와 같이 푼 사람도 있다.
# # 진짜 벽 느낀다..
# n = int(input())
# r = list(int(input()) for i in range(n))
# for i in r:
#     s1, i = divmod(i, 25)
#     s2, i = divmod(i, 10)
#     s3, i = divmod(i, 5)
#     s4, i = divmod(i, 1)

#     print(s1, s2, s3, s4)
