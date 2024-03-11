class Solution:
    def customSortString(self, order: str, s: str) -> str:
        z = list(s)
        result = ''
        for i in range (len(order)):
            if order[i] in z :
                p = order[i]
                while (z.count(order[i])>0):
                    result = result + p
                    z.remove(order[i])
        res2 = ''.join(z)
        result = result + res2
        return result

        