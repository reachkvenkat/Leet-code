class Solution:
    def square(self, li):
        res = 0
        for num in li:
            res += (num*num)
        return res
    
    def splitnum(self, number):
        res = []
        while number > 0:
            res.append(number%10)
            number = number // 10
        
        return res
        
    def isHappy(self, n):
        count = 0
        while count < 10:
            if n == 1:
                return True
            n = self.square(self.splitnum(n))
            count += 1
        
        return False