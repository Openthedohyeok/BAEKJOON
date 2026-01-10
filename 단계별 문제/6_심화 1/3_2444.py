# n = int(input())

# for i in range(1,n+1):
#     print(f'{"*"*(2*i-1):^{2*n-1}}')

# for i in range(1, n):
#     print(f'{"*"*(2*n-1-2*i):^{2*n-1}}')

# 위의 방식으로 했더니만, 오른쪽에 공백이 만들어져서 출력 오류로 틀렸다....

n = int(input())

for i in range(n):
    print(' '*(n-i-1)+'*'*(2*i+1))

for i in range(n-1):
    print(' '*(i+1)+'*'*(2*n-3-2*i))