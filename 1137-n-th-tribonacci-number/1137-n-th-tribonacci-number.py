class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n ==2:
            return 1
        previous3 = 0 
        previous1, previous2 = 1,1
        for i in range (3,n+1):
            output = previous1+previous2+previous3
            previous3 = previous2
            previous2 = previous1
            previous1 = output
        return output

        