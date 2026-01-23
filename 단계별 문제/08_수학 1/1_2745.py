import sys

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

number, n = sys.stdin.readline().rstrip().split()

answer = 0

for i in range(len(number)):
    try:
        answer += pow(int(n),i) * (alpha.index(number[len(number)-i-1])+10)
    except:
        answer += pow(int(n),i) * int(number[len(number)-i-1])

print(answer)

# 9'51"


# 아래와 같이 풀 수도 있다 .. 참내

# # N과 B를 입력받습니다. (예: ZZZZZ 36)
# n, b = input().split()

# # int() 함수를 사용하여 b진법 n을 10진수로 변환합니다.
# # 변환된 결과를 출력합니다.
# print(int(n, int(b)))