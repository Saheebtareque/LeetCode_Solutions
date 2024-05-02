class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        positive = []
        negative = []
        for num in nums:
            if num <0:
                negative.append(num)
            else:
                positive.append(num)
        maximum = -1
        for pos in positive:
            if -pos in negative:
                maximum = max(maximum,pos)
        return maximum
        