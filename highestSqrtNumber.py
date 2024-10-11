
k = 24

# imprimir el numero sqrt mas cercano por debajo o igual a k

left = 1
right = k
counter = 0
while (left + 1 < right):
    
    mid = (left+right)//2
    ''' 
    print(f"left: {left}")
    print(f"mid: {mid}")
    print(f"right: {right}")
    ''' 
    
    if mid*mid > k:
        right = mid
    else:
        left = mid
'''      
print(f"left: {left}")
print(f"mid: {mid}")
print(f"right: {right}")
''' 
if right * right <= k:
    print(f" the highest sqrt number smaller than or equal to {k} is {right * right}")
    counter += 1 
if mid * mid <= k and counter == 0:
    print(f" the highest sqrt number smaller than or equal to {k} is {mid * mid}")
    counter += 1
    
if left * left <= k and counter == 0:
    print(f" the highest sqrt number smaller than or equal to {k} is {left * left}")
        
        
        
    

