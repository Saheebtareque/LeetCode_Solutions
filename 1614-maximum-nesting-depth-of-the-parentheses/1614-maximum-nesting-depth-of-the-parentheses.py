class Solution:
    def maxDepth(self, s: str) -> int:
        maximum = 0
        current = 0
        for i in s:
            if i == "(":
                current += 1
            elif i== ")":
                current -= 1
            maximum = max(maximum,current)
        return maximum
        