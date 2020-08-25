class Solution:
    def sortArrayByParity(self, A):
        odd = len(A) - 1
        even = 0

        while odd > even:
            if A[odd]%2 < A[even]%2:
                A[odd], A[even] = A[even], A[odd]
                odd -= 1
                even += 1

            if A[odd] %2 == 1:
                odd -= 1

            if A[even] %2 == 0:
                even += 1

        return A