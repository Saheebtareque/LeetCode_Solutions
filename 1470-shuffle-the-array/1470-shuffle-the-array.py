class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        y = nums[:n]
        z = nums[n:]
        res = []
        for i in range (len(y)):
            res.append(y[i])
            res.append(z[i])
        return res
        