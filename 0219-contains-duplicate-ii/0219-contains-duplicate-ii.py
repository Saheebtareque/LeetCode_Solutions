class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        resultIndex = {}
        for i,n in enumerate(nums):
            if n in resultIndex and i - resultIndex[n] <= k:
                return True
            else:
                resultIndex[n] = i
        return False


        