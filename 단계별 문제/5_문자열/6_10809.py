s = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(26):
    print(s.find(alpha[i]), end=' ')

# alpha = 'abcdefghijklmnopqrstuvwxyz'
# 라고... 할수가 있다...
# 그리고, for i in range(len(alpha)) 라고 해도 된다...
# 또는 그냥 바로 for i in alpha 로 들어가도 됨..