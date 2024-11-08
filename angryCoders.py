x = 3
n = 5
arrayN = [1,2,4,6]
p = 3


contador = 1
contadorAux = 0
for i in range(len(arrayN)-1):
    contadorAux += arrayN[i+1]-arrayN[i]
    print(f"contadorAux = {arrayN[i+1]}-{arrayN[i]}: {contadorAux}")
    if contadorAux >= x:
        contador += 1
        contadorAux = 0
        print(f"contador = {contador}")
if contador >= p:
    print("yes")
else:
    print("no")
