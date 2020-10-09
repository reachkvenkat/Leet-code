class Solution:
    def majorityElement(self, nums):
        cnt = {}
        length = len(nums)
        for i in range(length):
            if nums[i] in cnt:
                cnt[nums[i]] += 1
            else:
                cnt[nums[i]] = 1
        for key in cnt:
            if cnt[key] > length//2:
                return key
        