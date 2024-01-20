class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range (len(tokens)):
            if tokens[i] == '+':
                q = stack.pop()
                w = stack.pop()
                result = int(w) + int(q)
                stack.append(result)
            elif tokens[i] == '-':
                q = stack.pop()
                w = stack.pop()
                result = int(w) - int(q)
                stack.append(result)
            elif tokens[i] == '*':
                q = stack.pop()
                w = stack.pop()
                result = int(w) * int(q)
                stack.append(result)
            elif tokens[i] == '/':
                q = stack.pop()
                w = stack.pop()
                result = int(w) / int(q)
                stack.append(int(result))
            else:
                stack.append(tokens[i])
        return int(stack[0])