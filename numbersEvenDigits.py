class Solution:
    def countDigits(self, num):
        count = 0
        while num > 0:
            num = num // 10
            count += 1
        return count

    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if self.countDigits(num) % 2 == 0:
                count += 1
        return count