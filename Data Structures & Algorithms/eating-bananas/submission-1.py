from math import *

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)
        start = 1
        while (start <= maxPiles):
            mid = (start + maxPiles) // 2
            print("current count: ", mid)
            hours = self.calculateHours(mid, piles)      
            print("current hours: ", hours)      
            if (mid == 1 or (hours <= h and self.calculateHours(mid-1, piles) > h)):
                print("answer count: ", mid)
                return mid
            elif (hours > h):
                start = mid + 1
            else:
                maxPiles = mid - 1
        
    def calculateHours(self, mid, piles):
        hours = 0
        for p in piles:
            hours += math.ceil(p / mid)
        # print(hours)
        return hours

            