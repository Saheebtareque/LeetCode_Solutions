import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        length = int(sqrt(n)+1)
        for i in range (1,length):
            if n % i ==0:
                res.append(i)
                res.append(n//i)
        p = set(res)
        z = list(p)
        z.sort()
        if k > len(z):
            return -1
        else:
            return z[k-1]


        