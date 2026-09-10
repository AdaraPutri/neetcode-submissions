# maximize, biggest length x width (difference in index x height)
# can not change order of integers in the array
# two pointer approach
# brute force: not ideal


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1   
        largest = 0     

        while left < right:
            # check current area
            area = (right - left) * min(heights[left], heights[right])
            # update largest
            largest = max(area, largest)

            # if either heights are smaller
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            elif heights[left] == heights[right]:
                if heights[left + 1] > heights[right - 1]:
                    left += 1
                else:
                    right -= 1
        
        return largest