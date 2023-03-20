nMax = int(input("Enter any positive number:"))
n = 1
while n <= nMax:
    fact = 1
    i = 1
    while i <= n:
      fact *= i
      i += 1
    print('{0:3d}! {1:16d}'.format(n, fact))
    n += 1
