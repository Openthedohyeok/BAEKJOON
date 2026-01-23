r = []

for i in range(10):
    r.append(int(input())%42)

print(len(list(set(r))))