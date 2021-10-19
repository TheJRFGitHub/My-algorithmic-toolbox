# python3
import datetime
import time
import math

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    a, b = map(int, input().split())
    x = sum_of_two_digits(a,b)
    print(x, time.process_time())
