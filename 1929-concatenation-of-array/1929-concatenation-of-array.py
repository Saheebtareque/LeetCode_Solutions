class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = nums[:]
        for num in x:
            nums.append(num)
        return nums
        