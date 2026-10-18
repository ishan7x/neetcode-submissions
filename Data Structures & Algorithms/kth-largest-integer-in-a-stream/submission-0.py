import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap, -num)
        # print(self.heap)

        

    def add(self, val: int) -> int:
        # adds the val to the list and then returns the kth largest element
        # add val to the max heap, then pop it k times add elements back into the heap
        heapq.heappush(self.heap, -val)
        addBack = []
        for i in range(self.k):
            ans = -self.heap[0]
            heapq.heappop(self.heap)
            addBack.append(ans)
        # print(addBack, ans)
        for num in addBack:
            heapq.heappush(self.heap, -num)
        return ans

        
