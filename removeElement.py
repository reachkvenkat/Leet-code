class Solution:
    def removeElement(self, nums, val):

        count = 0
        end = len(nums) - 1
        front = 0

        while front <= end:
            if nums[front] == val:
                nums[front] = nums[end]
                nums[end] = val
                end -= 1
                count += 1
                front -= 1
            front += 1

        return len(nums) - count