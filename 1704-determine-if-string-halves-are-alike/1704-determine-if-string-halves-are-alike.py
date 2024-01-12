class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        p = len(s)
        q = p//2
        vowels = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
        count = 0
        count2 = 0
        for i in range (0,q):
            if s[i] in vowels:
                count += 1
        for j in range (q,p):
            if s[j] in vowels:
                count2 += 1
        return count == count2
        