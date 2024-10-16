# find minimum altitude 

array = [1,1,1,1,1]
k = 5

left = 0
right = 0
for i in range(len(array)):
    if array[i] > right:
        right = array[i]
        
right += 1

while (left + 1 < right):
    counter = 0 
    mid = (left + right) // 2
    print(f"left: {left}")
    print(f"mid: {mid}")
    print(f"right: {right}")
    
    for i in range(len(array)):
        if array[i] >= mid:
            counter += 1
        

    if counter <= k:
        right = mid
        
    else: 
        left = mid
        
print(f"left: {left}")
print(f"right: {right}")  

for i in range(len(array)):
        if array[i] >= left:
            counter += 1

        
if counter <= k:
    print(f"minimum required altitude: {left}")
else: 
    print(f"minimum required altitude: {right}")
