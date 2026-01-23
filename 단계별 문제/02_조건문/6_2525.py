h, m = map(int, input().split())
t = int(input())

new_h = h + (m+t)//60

print(f'{new_h%24} {(m+t)%60}')