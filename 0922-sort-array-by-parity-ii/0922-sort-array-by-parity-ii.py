class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        res = []
        length = len(nums)//2
        for z in nums:
            if z%2 == 0:
                even.append(z)
            else:
                odd.append(z)
        for i in range (length):
            res.append(even[i])
            res.append(odd[i])
        return res

        