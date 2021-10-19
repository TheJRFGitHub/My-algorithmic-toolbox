# Uses python3
import time
def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)



def calc_fib_opt(n):
    a = []
    a.insert(0, 0)
    a.insert(1, 1)
    a.insert(2, 2)
    if (n <= 1):
        return n
    else :
        for i in range(n):
            x = a[-1] + a[-2]
            a.append(x)
        a.remove(a[-3])
        a.remove(a[-2])
        a.remove(a[-1])
        return a[-1]



n = int(input())
print(calc_fib_opt(n))
#print(calc_fib_naive(n))
#print(time.process_time())




