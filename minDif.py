# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
array1 = [1,6,80,78,7]
array2 = [3,19,29,12,17,60,1000,82]

array1.sort()
array2.sort()

print(array1)
print(array2)

dif = 0
minDif = 100000000000
currentPointer = 0
i = 0
j = 0

while i <= len(array1)-1 and j <= len(array2)-1:
    
    
    if array1[i] > array2[j]:
        currentPointer = i 
        dif = array1[currentPointer] - array2[j]
        print("dif = ", array1[currentPointer], "-", array2[j], "=",dif)
        if dif < 0:
            dif * -1
        if dif < minDif:
            minDif = dif
        if currentPointer - array2[j + 1] < currentPointer - array2[j]:
            j += 1
        
        
    if array1[i] < array2[j]:
        currentPointer = j 
        dif = array2[currentPointer] - array1[i]
        print("dif = ", array2[currentPointer], "-", array1[i], "=",dif)
        if dif < 0:
            dif * -1
        if dif < minDif:
            minDif = dif
        if currentPointer - array2[i + 1] < currentPointer - array2[i]:
            i += 1
        
    if array1[i] == array2[j]:
        minDif == 0
        print("Diferencia minima: ", minDif)
        break
        
    
        
print("Diferencia minima: ", minDif)