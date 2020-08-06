'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''


class Solution:
    def findDuplicates(self, nums):
        ans = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] *= -1

        return ans


def TestFunction(num_list, des_list):
    soln = Solution()

    if soln.findDuplicates(num_list) == des_list:
        print("Test case passed")
    else:
        print(soln.findDuplicates(num_list))
        print("Test case failed")

TestFunction([4,3,2,7,8,2,3,1], [2,3])
TestFunction([4,3,2,7,6,2,3,9,9], [2,3,9])


