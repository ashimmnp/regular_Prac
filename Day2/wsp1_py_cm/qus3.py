nMax= int(input("Enter any positive integer: "))
n =1
while(n <= nMax):
  if (n% 6 == 0):
    print('{0:3d}'.format(n))
  n = n+1
