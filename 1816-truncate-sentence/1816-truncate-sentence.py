class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x = s.split()
        z = x[:k]
        p = ' '.join(z)
        return p

        