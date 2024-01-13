class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        currsum = 0
        for num in nums:
            if currsum<0:
                currsum = 0
            currsum += num
            maximum = max(maximum,currsum)
        return maximum 