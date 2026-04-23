class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height = the height of the lower bar
        # width = the distance between 2 bars
        # maximize the area
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            curr_area = min(heights[i], heights[j]) * (j-i)
            if max_area < curr_area:
                max_area = curr_area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area