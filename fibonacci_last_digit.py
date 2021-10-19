# Uses python3
import random
import time

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_opt(n):
    if n<=1:
        return(n)
    a, b = 0, 1
    for i in range(n-1):
        c = a + b
        c = c % 10
        b, a = c, b
    return(c)






n = int(input())
print(get_fibonacci_last_digit_opt(n))
#print(get_fibonacci_last_digit_naive(n))


#while True:
 #   n=int(random.randint(1,20))
  #  print(n)
   # print(get_fibonacci_last_digit_opt(n),'==', get_fibonacci_last_digit_naive(n))
#    print(time.process_time())
 #   if get_fibonacci_last_digit_opt(n) == get_fibonacci_last_digit_naive(n):
  #      pass 
#    else :
 #       print(get_fibonacci_last_digit_opt(n),'is not equal to', get_fibonacci_last_digit_naive(n))
  #      break



