class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def dfs (start):
            if start == n:
                ans.append(nums[:]) 
                return
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start] 
                dfs (start + 1)  
                nums[start], nums[i] = nums[i], nums[start]  
        
        dfs(0)
        return ans
        