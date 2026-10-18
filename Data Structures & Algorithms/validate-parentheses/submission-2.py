class Solution:
    def isValid(self, s: str) -> bool:
        maps = {"{":"}", "[":"]", "(":")"}
        inputs = list(s)
        stack = deque()
        for i in inputs:
            if i in "{[(":
                stack.append(i)
            else:
                if (not stack or i != maps[stack.pop()]):
                    return False
        return not stack

        