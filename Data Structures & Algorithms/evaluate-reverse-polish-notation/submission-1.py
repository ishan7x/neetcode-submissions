class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"
        stack = deque()
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    result = a + b
                elif i == '-':
                    result = a - b
                elif i == '*':
                    result = a * b
                else:
                    result = int(a / b)
                stack.append(result)
        return stack.pop()