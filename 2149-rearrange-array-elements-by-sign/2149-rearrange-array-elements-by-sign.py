class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        length = len(nums)//2
        resPositive = []
        resNegative = []
        result = []
        for num in nums:
            if num < 0:
                resNegative.append(num)
            else:
                resPositive.append(num)
        for i in range (length):
            result.append(resPositive[i])
            result.append(resNegative[i])
        return result
        