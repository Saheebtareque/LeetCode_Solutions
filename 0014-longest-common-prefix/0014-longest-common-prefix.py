class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        v=sorted(strs)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

        # p = len(strs)
        # minimum = 100
        # for nums in strs:
        #     x = len(nums)
        #     minimum = min(minimum,x)
        # substr = ''
        # for i in range (minimum):
        #     for j in range (p):
        #         temp = strs[j][i]
        #         if j == (p-1) or temp != strs[j+1][i] :
        #             return substr
        #     substr = substr + temp
        # return substr 

        