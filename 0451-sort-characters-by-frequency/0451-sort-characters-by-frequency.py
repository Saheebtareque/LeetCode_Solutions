class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        sorted_by_frequency = sorted(d.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(sorted_by_frequency)
        substr = ''
        for letter, count in converted_dict.items():
            while (count > 0):
                substr = substr + str(letter)
                count -= 1 
        return substr 



        