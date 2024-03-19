import math
def isPowerOfFour(n):
   n = abs(n)
   if (n!=0 and n==pow(4,(math.log(n)/math.log(4)))):
      return True
   else:
      return False
