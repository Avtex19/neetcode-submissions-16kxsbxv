class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #O(n^2)
        max_area = 0
        n = len(heights)

        for i in range(n):
            current_height = heights[i]
            left = i
            while left>= 0 and heights[left] >= current_height:
                left -= 1
            right = i
            while right < n and heights[right] >= current_height:
                right += 1

            width = right-left-1
            area = current_height * width
            max_area = max(max_area,area)

        return max_area 