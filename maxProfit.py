class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        max_diff = 0
        pt_1 = 0
        pt_2 = 1

        while pt_1 < pt_2 and pt_2 < len(prices):
            temp = prices[pt_2] - prices[pt_1]
            max_diff = max(max_diff, temp)

            if prices[pt_1] >= prices[pt_2]:
                pt_1 = pt_2

            pt_2 += 1

        return max_diff