nMax= int(input("Enter an odd positive integer: "))
if nMax%2 == 0 or nMax<1:
  print("Error, Please enter a valid integer")
else:
  n =1
  sum = 0
  while(n <= nMax):
    if (n% 2 != 0):
      sum = sum+n
      print('{0:3d} {1:6d}'.format(n,sum))
    n = n+1
