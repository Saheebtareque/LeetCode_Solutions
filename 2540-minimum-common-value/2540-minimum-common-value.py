class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        minimum = float('inf')
        p = set(nums1)
        q = set(nums2)
        res = p.intersection(q)
        result = list(res)
        if len(result) == 0:
            return -1
        for num in result:
            minimum = min(minimum,num)
        return minimum

        