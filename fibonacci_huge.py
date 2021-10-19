# Uses python3
import time
import random

def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
# Fabonagi module
def fib_mod(n, m):
    if n<=1:
        return(n)
    a, b = 0, 1
    lst = []
    for i in range(n-1):
        c = a + b 
        c = c % m 
        b, a = c, b
        lst.append(c)
    lst.remove(lst[0])
    return lst


# Now lets find Pisano length function
def get_pisanoperiod_len(n, m):
    lst1 = fib_mod(n, m)
    i = 0
    while True:
        i += 1
        if lst1[i] == lst1[0] and lst1[i+1] == lst1[1] and lst1[i+2] == lst1[2]:
            break
    return i

# This is where the fun begins
def fibonacci_hugh(n,m):
    length = get_pisanoperiod_len(n, m)
    preresult = n % length
    result = preresult % m
    

    return preresult, result

#Optimized
def pisano_period(m):

    if m <= 1:
        return m
    
    a, b = 0, 1
    for i in range((m*m)+1):
        a, b = b, (a+b) % m
        if a==0 and b==1:
            return i + 1

def fibonacci_hugh_fast(n,m):
    if n <= 1:
        return n
    remainder = n % pisano_period(m)
    if remainder <= 1:
        return remainder
    a, b = 0, 1
    for i in range(remainder - 1):
        a, b = b, (a+b)

    return b % m




a, b = [int(i) for i in input().split()]

print(fibonacci_hugh_fast(a, b))
#print(fibonacci_huge_naive(a, b))
#print(time.process_time())
