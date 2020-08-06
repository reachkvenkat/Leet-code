'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4
'''


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<0:
            return False
        binvalue = bin(num)
        return binvalue[::-1].find('1')%2==0 and binvalue.count('1')==1