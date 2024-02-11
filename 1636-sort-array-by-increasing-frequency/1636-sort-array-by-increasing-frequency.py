class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        # res = []
        # count = Counter(nums)
        # buckets = defaultdict(list)
        # for n,freq in count.items():
        #     buckets[freq].append(n)
        # for i in range (1,len(nums)):
        #     for z in buckets[i]:
        #         q = i
        #         while q >= 1:
        #             res.append(z)
        #             q -= 1
        # return res
        n = len(nums)
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        sorted_arr = sorted(nums, key=lambda x: (freq[x], -x))
        return sorted_arr
        