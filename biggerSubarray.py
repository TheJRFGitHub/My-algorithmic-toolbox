

def sumaTotal(arreglo, total):
    for i in range(len(arreglo)):
        total += arreglo[i]
    return total
    


arreglo = [3,5,7,1,9,18,25]
arreglo.sort(reverse = True)

total = sumaTotal(arreglo, 0)
suma = 0

for i in range(len(arreglo)):
    print("i: ",i)
    suma += arreglo[i]
    total = total - arreglo[i]
    
  
    if  suma > total:
       print("resultado: ", suma)
       print(arreglo[0:i+1])
       break

print(arreglo)
