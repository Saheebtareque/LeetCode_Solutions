class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []
        ans = []
        n =len(nums)
        def dfs(i):
            if i >= n and subset[:] not in ans:
                ans.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            while i+1 < n and nums[i] == nums[i+1]:
                i +=1
            dfs(i+1)
        dfs(0)
        return ans


        