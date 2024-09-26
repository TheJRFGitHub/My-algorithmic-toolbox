class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
 
        return self.recursiveFunction(ransomNote, magazine, 0, 0, 0)  

    def recursiveFunction(self, ransomNote, magazine, indexOne, indexTwo, counter) -> int: 
        if counter == len(ransomNote):
            return True
        if indexOne == len(ransomNote)-1 and indexTwo == len(magazine)-1:
            return 
        if indexTwo == len(magazine)-1:
            index
            
            
        if ransomNote[indexOne] == magazine[indexTwo]:

            magazine = magazine[:indexTwo] + magazine[indexTwo + 1:]
            print(magazine)
            return self.recursiveFunction(ransomNote, magazine, indexOne + 1, indexTwo, counter + 1) 
        return self.recursiveFunction(ransomNote, magazine, indexOne, indexTwo + 1, counter)
        

  

        
        
