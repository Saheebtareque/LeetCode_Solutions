class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs (start):
            if start == n:
                res.append(nums[:])
                return
            for i in range (start,n):
                nums[start],nums[i] = nums[i],nums[start]
                if nums not in res:
                    dfs(start+1)
                nums[start],nums[i] = nums[i],nums[start]
        dfs(0)
        return res