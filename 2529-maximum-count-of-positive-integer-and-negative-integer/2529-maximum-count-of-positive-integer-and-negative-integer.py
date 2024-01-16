class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        maxpositive = 0
        maxnegative = 0
        for num in nums:
            if num <0:
                maxnegative += 1
            elif num >0:
                maxpositive += 1
        result = max(maxpositive,maxnegative)
        return result
        