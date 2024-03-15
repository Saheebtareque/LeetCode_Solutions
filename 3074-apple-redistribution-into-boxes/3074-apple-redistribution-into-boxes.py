class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        count = 0
        capacity.sort(reverse=True)
        for cap in capacity:
            total = total - cap
            count += 1
            if total <=0:
                return count
        