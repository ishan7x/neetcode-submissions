from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        queue = deque()
        for v in freq.values():
            heap.append(-v)
        heapq.heapify(heap)
        # print(heap, freq)
        time = 0
        while heap or queue:
            time+=1
            # print(heap)
            if (heap):
                currfreq = 1 + heapq.heappop(heap)
                if (currfreq):
                    queue.append([currfreq, time+n])
            if (queue):
                if (queue[0][1] == time):
                    heapq.heappush(heap, queue.popleft()[0])
            # print(queue)
        return time


