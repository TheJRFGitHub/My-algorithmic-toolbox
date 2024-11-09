# find the x (which represents the amount of space were trying to create between the programerrs) through binary search

x = 3
n = 5
arrayN = [1, 2, 4, 7, 16]
totalSpace = arrayN[-1] - arrayN[0]
p = 3

left = 0
right = totalSpace


def canBeAccomodated(x, arrayN, p):
    contador = 1
    contadorAux = 0
    for i in range(len(arrayN) - 1):
        contadorAux += arrayN[i + 1] - arrayN[i]
        print(f"contadorAux = {arrayN[i + 1]}-{arrayN[i]}: {contadorAux}")
        if contadorAux >= x:
            contador += 1
            contadorAux = 0
            print(f"contador = {contador}")
    if contador >= p:
        return True
    else:
        return False

def angryProgrammers(arrayN, p, left, right):
    print(arrayN)
    while (left + 1 < right):
        mid = (left + right) // 2
        print(f"mid: {mid}")
        cba = canBeAccomodated(mid, arrayN, p)
        print(f"can be accommodated? {cba}")
        if cba == True:
            left = mid
        else:
            right = mid
    return left


print(angryProgrammers(arrayN, p, left, right))
