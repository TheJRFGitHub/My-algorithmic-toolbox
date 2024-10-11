# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

arreglo = [1,4,8,19,45,50]

left = 0
right = 5

k = int(input("Introduce the number to be found: "))

while (left + 1 < right):
    print("left: ", left)
    print("right: ", right)
    mid = (left+right)//2
    
    if k >= arreglo[mid]:
        left = mid
    else:
        right = mid
    
if arreglo[left] == k:
    print(f"tu numero esta en el indice {left}")
elif arreglo[right] == k:
    print(f"tu numero esta en el indice {right}")
else:
    print("-1")
    
'''   
if left == k:
    print()
'''  
 
