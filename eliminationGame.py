class Solution:
    def lastRemaining(self, n: int) -> int:
        array = [i for i in range(1, n + 1)]
        print("Initial array: ", array)
        
        return self.recursiveFunction(n, 0, array,1)  

    def recursiveFunction(self, n, iterador, array, rightLeft) -> int: 
        
        
        print("rightLeft: ",rightLeft)
        if n == 1:
            return 1
        if iterador >= len(array):
            rightLeft = rightLeft + 1
            print("rightLeft: ", rightLeft)
            print("hey hey hey")
            iterador = 0
        else:
            
            if rightLeft % 2 == 1:
                print("indice: ", iterador)
                if len(array) == 2:
                    return array[1]
                if len(array) == 3:
                    return array[1]
                print("popped: ", array.pop(iterador), " from right")
                
                print(array)
                
                return self.recursiveFunction(n, iterador+1, array, rightLeft)

            if rightLeft % 2 == 0:
                
                iterador = iterador -1
                print("indice: ", iterador)
                if len(array) == 2:
                    return array[0]
                if len(array) == 3:
                    return array[1]
                print("popped: ", array.pop(iterador), " from left")
               
                print(array)
                
                return self.recursiveFunction(n, (iterador+1) * -1, array, rightLeft)
            
        
