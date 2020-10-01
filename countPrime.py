import math

class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        
        a = [1] * n
        a[0] = 0
        a[1] = 0
        ub = int(math.sqrt(n)) + 1
        
        for i in range(2, ub):
            if a[i]:
                a[i+i:n:i] = [0] * len(a[i+i:n:i])
        return sum(a)
                    