class Solution:
    def rearrange(self, array, ind):
        i = len(array) - 2
        array[i + 1] = 0
        while i > ind:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            i -= 1

        return array, ind+1

    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0

        while i < len(arr):
            if arr[i] == 0:
                arr, i = self.rearrange(arr, i)
            i += 1
