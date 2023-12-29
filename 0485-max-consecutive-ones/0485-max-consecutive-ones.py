class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = [0]
        for i in range (len(nums)):
            if nums[i] == 1:
                count += 1
                # if i == len(nums)-1:
                #     return count
            else:
                res.append(count)
                count = 0
        if max(res) > count:
            return max(res)
        else:
            return count

        