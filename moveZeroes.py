class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 1

        while fast < len(nums) and slow < len(nums):
            if nums[slow] == 0:
                if nums[fast] != 0:
                    nums[slow], nums[fast] = nums[fast], 0
                    slow += 1
                    fast += 1
                else:
                    fast += 1
            else:
                slow += 1
                fast += 1