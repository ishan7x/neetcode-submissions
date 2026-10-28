class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        # print(intervals)
        l, r = 0, 1
        rem = []
        while r < len(intervals):
            if intervals[l][1] < intervals[r][0]:
                l = r
            elif intervals[l][1] >= intervals[r][1]:
                rem.append(intervals[r])
            else:
                intervals[l][1] = intervals[r][1]
                rem.append(intervals[r])
            r+=1
        for removals in rem:
            intervals.remove(removals)
        return intervals


        