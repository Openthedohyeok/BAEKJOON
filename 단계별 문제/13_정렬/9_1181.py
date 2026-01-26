import sys

n = int(sys.stdin.readline())

words = []
for _ in range(n):
    words.append(sys.stdin.readline().rstrip())

words = list(set(words))
words.sort(key=lambda x:(len(x), x))

print(*words, sep='\n')

# 아래 풀이는 lambda 함수에 대해 모를 때의 풀이이다.
# import sys

# n = int(input())

# word_idx_list = []
# for _ in range(n):
#     word = sys.stdin.readline().rstrip()
#     if [len(word), word] in word_idx_list:
#         pass
#     else:
#         word_idx_list.append([len(word), word])

# word_idx_list.sort()

# for i in range(len(word_idx_list)):
#     print(word_idx_list[i][1])

# 11'22"