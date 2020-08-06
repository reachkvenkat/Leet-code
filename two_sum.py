'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''


class Solution:
    def twoSum(self, nums, target):
        ch = {}
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in ch:
                return [i,ch[tar]]
            ch[nums[i]] = i
        return None

def TestFunction(nums, target, desired):
    soln = Solution()

    if soln.twoSum(nums,target) == desired:
        print("Test case passed")
    else:
        print("Test case failed")

TestFunction([2, 7, 11, 15], 9, [1,0])
