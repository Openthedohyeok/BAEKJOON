import sys

word_list = []
word_len = []

while True:
    word = sys.stdin.readline().rstrip()
    if not word:
        break
    word_list.append(word)
    word_len.append(len(word))

answer =''

for i in range(max(word_len)):
    for s in word_list:
        try:
            answer += s[i]
        except:
            pass

print(answer)

# 17'15"