# Uses python3
import time
def get_change(m):
    x = [int(a) for a in str(m)]
    length = len(x)
    b, c = 5, 1
    # No. of tens
    a = x[0] * 10 ** (length - 2)
    b = x[1] * 10 ** (length - 3)
    return a, b

def get_change_opt(m): 
    a, b, c = m//10, (m % 10), m % 5
    #print(b)
    b = b//5

    
    #a = x[0] * 10 ** (length - 2)
    #b = x[1] * 10 ** (length - 3)

    return a + b + c

m = int(input())
print(get_change_opt(m))
