class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        m = m + n
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                t = len(nums1) - 1
                while t > i:
                    nums1[t] = nums1[t-1]
                    t -= 1
                nums1[i] = nums2[j]
                i += 1
                j += 1
        i = len(nums1) - 1
        for t in range(n-1, j-1,-1):
            nums1[i] = nums2[t]
            i -= 1