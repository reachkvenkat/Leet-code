class Solution:
    def replaceElements(self, arr):
        n = len(arr) - 1
        mx = arr[n]

        for i in range(n-1, -1, -1):
            arr[i], mx = mx, max(arr[i], mx)
        arr[n] = -1

        return arr