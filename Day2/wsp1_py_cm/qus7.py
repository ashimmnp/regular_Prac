def myPow(x,n):
    i = 1
    while i <n:
        x *= x
        i += 1
    print("The value is:",x)
a = int(input("Enter the number:"))
b = int(input("Enter the power to be raised:"))
myPow(a,b)
