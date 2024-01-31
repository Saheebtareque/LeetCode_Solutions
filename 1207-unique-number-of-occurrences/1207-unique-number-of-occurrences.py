class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        frequency = list(counts.values())
        for i in frequency:
            if frequency.count(i) >1:
                return False
        return True

        