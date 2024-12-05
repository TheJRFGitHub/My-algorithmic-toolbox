class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        word = self.createWord(n, "0", 1)
        print(f"word: {word}")
        return int(word[k-1])
            
    def createWord(self, n, word, index) -> list:
        newWord = ""
        if index == n:
            return word
        else:        
            for i in range(len(word)):
                
                newSegment = self.newSegment(word[i])
                newWord += newSegment
        return self.createWord(n, newWord, index + 1)

    def newSegment(self, character) -> list:

        if character == "0":
            newSegment =  "01"
           
        if character == "1":
            newSegment =  "10"

        return newSegment
