class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        res = [0 for _ in range(1, N+2)]
        
        for t in trust:
            res[t[0]] -= 1
            res[t[1]] += 1
        
        for i in range(1, len(res)):
            if res[i] == N-1:
                return i
        
        return -1
                