n = int(input())

for i in range(n):
    word = input()
    print(word[0], end='')
    print(word[len(word)-1])

# 옛날엔 이렇게 풀기도 했었군
# t = int(input())
# for _ in range(t):
#     str_input = input()
#     print(f'{str_input[0]}{str_input[-1]}')