# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

matriz = [[0,1,1],
          [1,0,1],
          [0,1,0]]

#print(matriz[coordenadaY][coordenadaX])
#print(matriz[len(matriz)-1][len(matriz)-1])
#print(len(matriz)-1, len(matriz[coordenadaY])
#print(matriz[len(matriz)-1][len(matriz)-1])



def laberinto(coordenadaY, coordenadaX):
    
    if coordenadaY >= len(matriz) or coordenadaX >= len(matriz):
        return False
    if matriz[coordenadaY][coordenadaX] == 1:
        return False
    if coordenadaY == len(matriz)-1 and coordenadaX == len(matriz)-1:
        return True
    
    moverAbajo = laberinto(coordenadaY + 1, coordenadaX)
    
    moverDerecha = laberinto(coordenadaY, coordenadaX + 1)
    
    print("coordenadaY: ", coordenadaY, "coordenadaX: ", coordenadaX)
    
    if moverAbajo == True:
        return True
    if moverDerecha == True:
        return True
        
    else:
        return False
    
print(laberinto1(0,0))        
    
