class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l,r = 0,len(numbers)-1
        while l<r:
            z = numbers[l] + numbers[r]
            if z< target:
                l +=1
            elif z> target:
                r -= 1
            else:
                res.append(l+1)
                res.append(r+1)
                return res