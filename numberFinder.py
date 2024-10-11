

arreglo = [1,4,8,19,45,50]

left = 1
right = 100
numero = 28




while (left + 1 < right):
    
    mid = (left+right)//2 
    respuesta = input(f"Tu numero es mayor o igual que {mid}?")
    if respuesta == "si":
        left = mid
    else:
        right = mid
    
    print(mid)
    
answer = input(f"tu numero es {left}?")
    
if answer == "si":
    print(f"tu numero es {left}")
        
else:
    print(f"tu numero es {right}")    

