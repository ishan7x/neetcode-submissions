import math, heapq
class Solution:
    # I have to return the K closes points to the origin. I can create a min heap of distances and the points associated with those distances. Then I just need to pop it and reverse engineer the points by keeping track of a DS to the points. I will use a map so that if some points are at the same distance then they can be keep tracked of, and the return of values will be according to what tehe order I need

    def distance(self, point: List[int]):
        return math.sqrt((point[0]-0)**2 + (point[1]-0)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for point in points:
            distance = self.distance(point)
            heapq.heappush(heap, (distance, point))
        # print(heap)
        while (k > 0):
            kth = heapq.heappop(heap)
            dist, coord = kth
            ans.append(coord)
            k -= 1
        return ans



        