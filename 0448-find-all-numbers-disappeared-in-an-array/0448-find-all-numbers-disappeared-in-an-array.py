class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        unique = set(nums)
        res = []
        for i in range (1,size+1):
            if i not in unique:
                res.append(i)
        return res
        