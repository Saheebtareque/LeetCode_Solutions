class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            elif stack:
                z = ord(stack[-1])
                w = ord(i)
                p = z-w
                if abs(p) == 32:
                    stack.pop()
                else:
                    stack.append(i)
        return ''.join(stack)
        