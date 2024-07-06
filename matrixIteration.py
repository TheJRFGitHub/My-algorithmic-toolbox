
f = 4
c = 5

tamanoMatriz = f*c
print(tamanoMatriz)
filas = [0 for i in range(f)]
print("filas: ", filas)
print("columnas: ", c)
matriz = [[0 for j in range(c)] for i in range(f)]
print("Matriz", matriz)
contador = 0
for i in range(f):
    for j in range(c):
        #print("i: ", i)
        #print("j: ", j)
        #print("k: ", k)
        contador += 1
        #print(contador)
        matriz[i][j] = contador
        
        
    
print(matriz)
