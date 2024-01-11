class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        count = 0
        for num in nums:
            count += num
            res.append(count)
        return res
