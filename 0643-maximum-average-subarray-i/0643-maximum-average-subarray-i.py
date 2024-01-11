class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wsum = 0
        msum = float('-inf')
        for i in range (0,k):
            wsum = wsum + nums[i]
        max2 = wsum
        if len (nums) <= k:
            q = wsum / k
            w = round(q, 5)
            return w
        for i in range (k,len(nums)):
            wsum = wsum - nums[i-k] + nums[i]
            msum = max(wsum,msum)
        msum = max(msum,max2)
        p = msum / k
        z = round(p, 5)
        return z
        