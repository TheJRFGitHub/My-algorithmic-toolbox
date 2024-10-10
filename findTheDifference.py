class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        return self.recursiveFunction(s, t, 0, 0) 

    def recursiveFunction(self, s, t, indexS, indexT) -> int:

        if len(t) == 1:
            return t[0]

        if s[indexS] == t[indexT]:
            print("s: ", s)
            print("t: ", t)
            print(s[indexS], "equals", t[indexT])
            print("removing: ", t[indexT], "where index: ", indexT)
            t = s.replace(s[indexS], '', 1)
            t = t.replace(t[indexT], '', 1)
            return self.recursiveFunction(s, t, 0, 0)

        if indexT < len(t)-1:
            return self.recursiveFunction(s, t, indexS, indexT + 1)

        if indexT == len(t)-1:
            
            return self.recursiveFunction(s, t, indexS + 1, 0)
 
        
