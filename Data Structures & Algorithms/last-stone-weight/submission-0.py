import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        # print(heap)

        while (len(heap) > 1):
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if (x == y):
                continue
            else:
                if (x > y):
                    heapq.heappush(heap, -x+y)
                else:
                    heapq.heappush(heap, x-y)
        return -heap[0] if (len(heap) > 0) else 0
        