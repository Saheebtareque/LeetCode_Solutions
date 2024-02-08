import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] == letter:
                count += 1
        percentage = math.floor((count/len(s)* 100))
        return percentage
        
        