class Solution:
    def kthCharacter(self, k: int) -> str:
           return self.createWord("a", k)

    def createWord(self, word, k) -> str:

        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                    "v", "w", "x", "y", "z", "a"]

        followingWord = self.wordSecondPart(word, alphabet)

        newWord = word + followingWord

        if len(newWord) >= k:
            return newWord[k-1]

        else:
            return self.createWord(newWord, k)


    def wordSecondPart(self, word, alphabet) -> str:
        following = ""

        for i in range(len(word)):
            for j in range(len(alphabet) - 1):
                if word[i] == alphabet[j]:
                    following += alphabet[j + 1]
        return(following)
        
