nMax = 10
n = 1
while n <= nMax:
    sum1n=0
    i = 1
    while i <= n:
        sum1n += i
        i += 1
    print('{0:3d} {1:6d}'.format(n,sum1n))
    n += 1
    
