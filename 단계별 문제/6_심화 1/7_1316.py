import sys

n = int(input())
cnt = 0

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    #그룹단어인지 확인을 하고 맞으면 cnt +1
    basket = []
    temp = ''
    for s in word:
        if s in basket and s != temp:
            break
        else:
            temp = s 
            basket.append(s)
        if len(basket) == len(word):
            cnt += 1

print(cnt)


# 아래와 같은 풀이도 있으니 참고 #
# import sys

# n = int(sys.stdin.readline())
# count = 0

# for _ in range(n):
#     word = sys.stdin.readline().rstrip()
#     # word.find를 기준으로 정렬하면 같은 문자끼리 뭉치게 됩니다.
#     # 예: 'aabbbccb' -> 'aaabbbcc' (정렬 결과가 원본과 다르면 그룹 단어 아님)
#     if list(word) == sorted(word, key=word.find):
#         count += 1

# print(count)