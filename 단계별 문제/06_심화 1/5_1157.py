# count 를 사용할 수 있다는 것을 알게된 후 푼 풀이
import sys

word = sys.stdin.readline().rstrip().upper()

word_sorted = list(set(word))
max_val = []

for s in word_sorted:
    max_val.append(word.count(s))

if max_val.count(max(max_val)) == 1:
    print(word_sorted[max_val.index(max(max_val))])
else:
    print('?')


############## 내가 처음 푼 풀이 #############################

# import sys

# word = sys.stdin.readline().rstrip()

# up_word = word.upper()

# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# check = list(0 for _ in range(len(alpha)))

# for i in up_word:
#     check[alpha.find(i)] += 1

# max_num = 0
# for j in check:
#     if j == max(check): # 이거를 밖에다가 놓기만 해도 속도가 훨씬 올라간다.
#         max_num += 1
#     else:
#         pass

# if max_num == 1:
#     print(alpha[check.index(max(check))])
# else:
#     print('?')


############# 1/14 풀이 ###################

# import sys

# word = sys.stdin.readline().rstrip().upper()
# word_set = list(set(word))

# cnt = []

# for s in word_set:
#     cnt.append(word.count(s))

# if cnt.count(max(cnt)) > 1:
#     print('?')
# else:
#     print(word_set[cnt.index(max(cnt))])