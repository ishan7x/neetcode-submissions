class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = 0
        while (start < end):
            curr_area = min(heights[start], heights[end]) * (end - start)
            if (curr_area > max_area):
                max_area = curr_area
            if (heights[end] <= heights[start]):
                end-=1
            else:
                start += 1
        return max_area
        