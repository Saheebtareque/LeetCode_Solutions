class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        iPositions = []
        product =1
        #list comprehension
        for count, value in enumerate(nums):
            if value == 0:
                iPositions.append(count)
        if len(iPositions) > 1:
            d = [0 for x in nums]
            return d
        elif len(iPositions) == 1:
            res2 = [0 for x in nums]
            z = iPositions.pop()
            for i in range(len(nums)):
                if i != z:
                    product = product * nums[i]
            for i in range(len(nums)):
                if i == z:
                    res2[i] = product
            return res2
        else:
            for num in nums:
                product = product * num
            for i in range (len(nums)):
                res.append(product//nums[i])
            return res



