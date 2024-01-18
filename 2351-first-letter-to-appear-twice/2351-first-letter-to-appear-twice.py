class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashset = {}
        for c in s:
            if c in hashset:
                return c
            else:
                hashset[c] = 1
        
        