# 11. Container With Most Water

# 56ms 97.42%
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = 0
        while (left < right):
            low = min(height[left], height[right])
            area = max(area, (right - left) * low)

            if height[left] < height[right]:
                while (height[left] <= low and left <= right):
                    left += 1
            else:
                while (height[right] <= low and right >= left):
                    right -= 1

        return area
            