class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        present = defaultdict(int)
        for i in range (len(magazine)):
            present[magazine[i]] += 1
        for j in ransomNote:
            if j in present and present[j] > 0:
                present[j] -= 1
            else:
                return False
        return True
        