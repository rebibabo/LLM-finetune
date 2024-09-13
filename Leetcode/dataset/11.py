class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > max_val:
                max_val = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_val