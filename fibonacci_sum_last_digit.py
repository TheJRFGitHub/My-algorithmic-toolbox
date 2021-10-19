# Uses python3
import time

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum_fast(n):
    rem = n % 60
    a, b = 0, 1
    for i in range(rem + 1):
        a, b  = b, (a+b)

    return (b-1) % 10 

n = int(input())
print(fibonacci_sum_fast(n))
#print(fibonacci_sum_naive(n))



