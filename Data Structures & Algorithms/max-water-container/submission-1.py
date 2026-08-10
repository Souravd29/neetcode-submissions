class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        maximum_water = 0


        left, right = 0 , n-1

        while left < right:

            distance = (right - left)
            height = min(heights[left],heights[right])
            water = distance * height
            maximum_water = max(maximum_water,water)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1

        return maximum_water