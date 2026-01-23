n = int(input())

div_3 = n//3
div_5 = n//5
vin_list = []

for i in range(div_5+1):
    for j in range(div_3+1):
        if 5*i+3*j == n:
            vin_list.append(i+j)

if vin_list:
    print(min(vin_list))
else:
    print(-1)

# 7'59"