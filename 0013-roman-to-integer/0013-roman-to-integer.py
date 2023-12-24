class Solution:
    def romanToInt(self, s: str) -> int:
        mapScale = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        summation = 0
        nums = list(s)
        for i in range (len(nums)):
            z = mapScale[nums[i]]
            if (i + 1)< len(nums) and z < mapScale[nums[i+1]]:
                summation = summation - z
            else:
                summation = summation + z
        return summation