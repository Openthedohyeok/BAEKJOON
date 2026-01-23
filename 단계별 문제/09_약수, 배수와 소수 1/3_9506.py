while True:
    n = int(input())
    if n == -1:
        break
    
    res = []
    for i in range(1, n):
        if n % i == 0:
            res.append(i)
    
    if sum(res) == n:
        print(f'{n} = ', end='')
        for s in res:
            print(s, end='')
            if s==res[len(res)-1]:
                print('')
                break
            print(' + ', end='')
    else:
        print(f'{n} is NOT perfect.')

# 10'12"    