class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.strip()
        count = 0
        for i in range (len(x)-1,-1,-1):
            if x[i] == ' ':
                break
            else:
                count +=1
        return count

        