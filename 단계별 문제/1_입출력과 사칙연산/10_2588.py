a = int(input())
b = input()

b2 = int(b[2])
b1 = int(b[1])
b0 = int(b[0])
# b0, b1, b2=map(int, input()) 으로 해도 된다...

print(a*b2)
print(a*b1)
print(a*b0)
print(a*b0*100+a*b1*10+a*b2)
