class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        i = 0
        count = 1
        maximum = 1
        while i<len(nums)-1:
            if i+1 < len(nums) and nums[i+1] - nums[i] == 1:
                count +=1
                maximum = max(maximum,count)
            elif nums[i+1] - nums[i] > 1:
                count = 1
            i +=1
        return maximum
        