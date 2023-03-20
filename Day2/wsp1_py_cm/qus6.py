def squarebox(n):
    x = "*"
    space = " "
    i = 1
    while i<=n:
        if (i==1 or i==n):
            print(x*n)
        else:
            print(x+space * (n-2)+x)
        i +=1
squarebox(5)
