class Solution:
    def mySqrt(self, x):
        if x <= 1:
            return x
        
        lower = 0
        if x <= 5:
            upper = x
        else:
            upper = x//2
            
        middle = (upper + lower) // 2
            
        while True:
            if middle * middle == x:
                return middle
            elif middle * middle > x:
                upper = middle
            else:
                lower = middle
            
            if (upper + lower) // 2 == middle:
                 return middle
            
            middle = (lower + upper) // 2