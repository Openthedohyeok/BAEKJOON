# n, x = map(int, input().split())
# list_a = input().split()
# result = ""

# for i in range(n):
#     if int(list_a[i])<x:
#         result = result + " " + list_a[i]
#     else:
#         pass

# print(result.lstrip()) 
#############################################

# Other solution

n, x = map(int, input().split())
list_a = list(map(int, input().split()))

for i in range(n):
    if list_a[i] < x:
        print(list_a[i], end=' ')

