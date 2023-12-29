class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subsets = []
        def dfs(i):
            if i == len(nums):
                result.append(subsets.copy())
                return
            subsets.append(nums[i])
            dfs(i+1)
            
            subsets.pop()
            dfs(i+1)
        dfs(0)
        return result

        # time complexity : o(n*2^n)
        
        # For the ppl like me who struggled with grasping the dfs recursive call, below is a simple example:

# Let's say we have the list nums = [1, 2, 3] and we call the dfs function with i = 0.

# The first call: dfs(0):
# The condition i >= len(nums) is false, so we move forward.
# nums[0] is appended to subset which is now [1].
# A new call is made to dfs(1).

# The second call: dfs(1):
# The condition i >= len(nums) is false, so we move forward.
# nums[1] is appended to subset which is now [1, 2].
# A new call is made to dfs(2).

# The third call: dfs(2):
# The condition i >= len(nums) is false, so we move forward.
# nums[2] is appended to subset which is now [1, 2, 3].
# A new call is made to dfs(3).

# The fourth call: dfs(3):
# The condition i >= len(nums) is true, so the current subset [1, 2, 3] is appended to the res list.
# The function returns.

# The third call returns:
# nums[2] is removed from subset which is now [1, 2].
# A new call is made to dfs(3).

# The fifth call: dfs(3):
# The condition i >= len(nums) is true, so the current subset [1, 2] is appended to the res list.
# The function returns.

# The second call returns:
# nums[1] is removed from subset which is now [1].
# A new call is made to dfs(2).

# The sixth call: dfs(2):
# The condition i >= len(nums) is false, so we move forward.
# nums[2] is appended to subset which is now [1, 3].
# A new call is made to dfs(3).

# The seventh call: dfs(3):
# The condition i >= len(nums) is true, so the current subset [1, 3] is appended to the res list.
# The function returns.

# The sixth call returns:
# nums[2] is removed from subset which is now [1].
# A new call is made to dfs(3).

# The eighth call: dfs(3):
# The condition i >= len(nums) is true, so the current subset [1] is appended to the res list.

# Hope this helps! 
# And thanks Neetcode for sharing the original solution!
        
        