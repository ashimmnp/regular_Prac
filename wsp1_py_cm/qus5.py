nMax = 20
n = 1
while n <= nMax:
    s1 = 0
    k =1
    while k <=n:
        s1 = s1+k
        k = k +1
    s2 = 0
    k =1
    while k<=n:
        s2 = s2 + k**2
        k = k +1
    s3 = 3*s2//s1
    print('{0:3d} {1:4d} {2:5d} {3:6d}'.format(n,s1,s2,s3))
    n = n +1
    
        
    
