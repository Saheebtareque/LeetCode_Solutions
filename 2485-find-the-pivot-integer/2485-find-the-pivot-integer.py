class Solution:
    def pivotInteger(self, n: int) -> int:
        res = -1
        if n== 1:
            return 1
        totalsum = (n*(n+1))//2
        for i in range(2,n+1):
            p = (i*(i+1))//2
            z = i-1
            q = totalsum - (z*(z+1)//2)
            if p == q:
                return i
        return res
        