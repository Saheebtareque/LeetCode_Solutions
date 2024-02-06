# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         l,r = 0,len(height)-1
#         while l<r:
#             if r-l == 1:
#                 z = min(height[l],height[r])
#                 return z
#             elif height[l+1] - height[l] >= 1:
#                 l = l+1
#             elif height[r-1] - height[r] >2:
#                 r = r-1
#             else:
#                 z = min(height[l],height[r])
#                 index = r - l
#                 area = z * index
#                 return area
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

        