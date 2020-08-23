class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxCount = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            if i == 0:
                if count > maxCount:
                    maxCount = count
                count = 0
        if count > maxCount:
            return count
        return maxCount