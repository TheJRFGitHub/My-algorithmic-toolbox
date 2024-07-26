
def sumaDigitos(numero):
    suma = 0
    if numero < 10:
        return numero
    else:
        ultimoDigito = numero%10
        numero = int((numero-ultimoDigito)/10)
        suma = ultimoDigito + sumaDigitos(numero)
        return suma
        
print(sumaDigitos(123456789))
