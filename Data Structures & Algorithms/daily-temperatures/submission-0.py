class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        result = [0] * len(temperatures)
        temps = list(enumerate(temperatures))
        for i,j in temps:
            while(stack and j > stack[-1][0]):
                stackTemp, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append((j, i))
        return result

        