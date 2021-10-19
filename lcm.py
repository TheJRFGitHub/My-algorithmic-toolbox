# Uses python3
import time
import random

#class gcd(a, b):
 #   def gcd(a, b):
  #      x = 1
   #     while x != 0:
    #        x = a % b
     #       a = b
      #      b = x 
#    return a

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd(a, b):
    x = 1
    while x != 0:
        x = a % b
        a = b
        b = x 
    return a

def lcm(a, b):
    result = a * b / gcd(a, b)
    return result



a, b = [int(i) for i in input().split()]
print(int(lcm(a, b)))
#print(lcm_naive(a, b))

#stress testie
#while True:
 #   a = int(random.randint(1,20))
  #  b = int(random.randint(1,20))
   # print(a)
#    print(b)
 #   print(lcm(a, b), '==', lcm_naive(a, b))
  #  print(time.process_time())
   # if lcm(a, b) == lcm_naive(a, b):
    #    pass
#    else :
 #       print(lcm(a, b), 'is not equal to', lcm_naive(a, b))
  #      break


