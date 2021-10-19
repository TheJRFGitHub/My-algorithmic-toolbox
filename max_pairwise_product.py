import time
import random

def max_pairwise_product_naive(numbers):
    n = len(numbers)
    if n > 1:
        max_product = 0
        for first in range(n):
            for second in range(first + 1, n):
                max_product = max(max_product,
                        numbers[first] * numbers[second])
    else :
        max_product = numbers[0]

    return max_product

def max_pairwise_product(numbers):
    sortednums = sorted(numbers)

    if len(sortednums) > 1:
        result = sortednums[-1] * sortednums[-2]
    else :
        result = sortednums[0]

    return result




if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
    #print(time.process_time())


#while True:
 #   a=[]
  #  n=int(random.randint(1,20))
   # for j in range(n):
#        a.append(random.randint(0,10000))
 #   print(n)
  #  print(a)
   # print(max_pairwise_product(a),'==', max_pairwise_product_naive(a))
#    print(time.process_time())
 #   if max_pairwise_product(a) == max_pairwise_product_naive(a):
  #      pass 
   # else :
#        print(max_pairwise_product(a),'is not equal to', max_pairwise_product_naive(a))
 #       break


 



