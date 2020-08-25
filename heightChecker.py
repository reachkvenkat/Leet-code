class Solution:
    def heightChecker(self, heights):
        sort_height = sorted(heights)
        cnt = 0
        for i in range(0, len(heights)):
            if sort_height[i] != heights[i]:
                cnt += 1

        return cnt