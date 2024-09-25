class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
 
        return self.recursiveFunction(ransomNote, magazine, 0, 0)  

    def recursiveFunction(self, ransomNote, magazine, indexOne, indexTwo) -> int: 
        
        if indexOne < len(ransomNote) and indexTwo == len(magazine)-1:
            return False
        if indexOne == len(ransomNote)-1:
            return True
        if ransomNote[indexOne] == magazine[indexTwo]:
            return self.recursiveFunction(ransomNote, magazine, indexOne + 1, indexTwo)
        return self.recursiveFunction(ransomNote, magazine, indexOne, indexTwo + 1)
        

  
