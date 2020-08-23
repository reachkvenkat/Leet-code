class Solution:
    def sortedSquares(self, A):
        pos = 0

        for i in range(0, len(A)):
            if A[i] >= 0:
                pos = i
                break
        if pos > 0:
            neg = pos - 1
        else:
            neg = -1

        res = []
        while pos < len(A) and neg > -1:
            if abs(A[pos]) < abs(A[neg]):
                res.append(A[pos] * A[pos])
                pos += 1
            else:
                res.append(A[neg] * A[neg])
                neg -= 1

        while pos < len(A):
            res.append(A[pos] * A[pos])
            pos += 1

        while neg > -1:
            res.append(A[neg] * A[neg])
            neg -= 1

        return res