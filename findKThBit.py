class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = self.createS(n, "0", 0)
        for i in range(len(s)):
            if k > 0:
                searchedBit = s[k-1]
        print(f"s = {s}")
        print(f"k = {k}")
        return searchedBit


    def createS(self, n: int, s: str, counter: int) -> str:
        inverted = self.invert(s)
        reversed = self.reverse(inverted)
        if counter == n:
            return s
        else:
            return self.createS(n, s + "1" + reversed, counter + 1)


    def invert(self, string) -> str:
        s = ""
        for i in range(len(string)):
            if string[i] == "0":
                s += "1"
            else:
                s += "0"
        return s

    def reverse(self, string) -> str:
        s = string[-1]
        for i in range(len(string) + 1):
            if i > 1:
                s += string[-i]
        return s
        


        
        
