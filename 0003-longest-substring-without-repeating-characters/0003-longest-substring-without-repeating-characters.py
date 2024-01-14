class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        maxstreak = 0
        l= 0
        alphabets = set()
        for r in range (len(s)):
            while s[r] in alphabets:
                alphabets.remove(s[l])
                l += 1
            alphabets.add(s[r])
            maxstreak = max(maxstreak,r-l+1)
        return maxstreak 


        