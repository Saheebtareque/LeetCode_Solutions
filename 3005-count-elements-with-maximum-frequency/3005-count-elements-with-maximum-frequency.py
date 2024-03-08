class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        res = []
        count = 0
        counts = Counter(nums)
        for value in counts.values():
            res.append(value)
        res.sort()
        z = res[-1]
        for p in res:
            if p == z:
                count += z
        return count
        