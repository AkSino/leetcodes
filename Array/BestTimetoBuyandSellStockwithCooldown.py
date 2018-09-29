class Solution(object):
    def maxProfit(prices):
        L = len(prices)
        if (L < 2):
            return 0;

    int
    has1_doNothing = -prices[0];
    int
    has1_Sell = 0;
    int
    has0_doNothing = 0;
    int
    has0_Buy = -prices[0];
    for (int i=1; i < L; i++) {
        has1_doNothing = has1_doNothing > has0_Buy ? has1_doNothing: has0_Buy;
    has0_Buy = -prices[i] + has0_doNothing;
    has0_doNothing = has0_doNothing > has1_Sell ? has0_doNothing: has1_Sell;
    has1_Sell = prices[i] + has1_doNothing;
    }
    return has1_Sell > has0_doNothing ? has1_Sell: has0_doNothing;

}

var=Solution()
print(var.maxProfit([6,1,3,2,4,7]))


