class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        stack = []
        for i in s:
            if i=='(' or i==')':
                if i=='(':
                    count +=1
                    stack.append(i)
                elif i==')' and count >0:
                    stack.append(i)
                    count -=1
            else:
                stack.append(i)
        stack.reverse()
        while count>0:
            stack.remove('(')
            count -= 1
        stack.reverse()
        return ''.join(stack)