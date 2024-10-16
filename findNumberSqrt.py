# find sqrt of a number

k = 15
# sqrt(15) = 3.872983346

left = 1
right = k

while(left + .00001 < right):
    mid = (left + right) / 2
    
    if mid *mid > k:
        right = mid
    else:
        left = mid
    
print(f"left: {left}")
print(f"mid: {mid}")
print(f"right: {right}")
