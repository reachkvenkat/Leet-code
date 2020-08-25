class Solution:
    def checkIfExist(self, arr):
        mem = {}
        for num in arr:
            if num * 2 in mem or num/2 in mem:
                return True
            else:
                mem[num] = 1
        return False