class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        profit =0
        for r in range(1,len(prices)):
            if(prices[l]>prices[r]):
                l=r
            
            profit = max(prices[r]-prices[l],profit)
        
        return profit

        