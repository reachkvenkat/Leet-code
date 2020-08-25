class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 1:
            return 1
        i = 0
        j = 1
        count = 0

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
                count += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1

        return len(nums) - count