# Uses python3
import time
import random
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd(a, b):
    x = 1
    while x != 0:
        x = a % b
        a = b
        b = x 
    return a


a, b = [int(i) for i in input().split()]
print(gcd(a, b))
#print(gcd_naive(a, b))
#print(time.process_time())


#stress testie
#while True:
#    a = int(random.randint(1,20))
 #   b = int(random.randint(1,20))
  #  print(a)
   # print(b)
#    print(gcd(a, b), '==', gcd_naive(a, b))
 #   if gcd(a, b) == gcd_naive(a, b):
  #      pass
   # else :
#        print(gcd(a, b), 'is not equal to', gcd_naive(a, b))
 #       break



