class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        g,h = -1,-1
        d = {}
        mapts = {}
        for i in range (len(s)):
            p = s[i]
            if p not in d:
                d[p] = t[i]
            elif t[i] != d[p]:
                g = 1
                break
        if g == 1:
            temp = False
        else:
            temp = True
        for j in range (len(t)):
            z = t[j]
            if z not in mapts:
                mapts[z] = s[j]
            elif s[j] != mapts[z]:
                h = 1
                break
        if h==1:
            temp2 = False
        else:
            temp2 = True 
        return (temp and temp2)



        



        