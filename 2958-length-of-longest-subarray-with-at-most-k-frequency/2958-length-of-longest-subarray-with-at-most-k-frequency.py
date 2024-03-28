class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counters = defaultdict(int)
        length = 0
        maxlength = 0
        l = 0
        for r in range(len(nums)):
            counters[nums[r]] += 1
            while counters[nums[r]] > k:
                counters[nums[l]] -= 1
                l += 1 
            length = (r-l+1)
            maxlength = max(maxlength,length)
        return maxlength    
            


        