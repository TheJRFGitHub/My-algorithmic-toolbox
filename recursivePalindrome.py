def palindromo(palabra):
    i = 0
    
    if palabra == "":
        return True
    if palabra[0] != palabra[-1]:
        return False
    else:
        i += 1
        palabra = palabra[i:-i]
        
        return palindromo(palabra)
       
print(palindromo("ahahahaha"))
