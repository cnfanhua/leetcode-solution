/*
 * @lc app=leetcode.cn id=121 lang=csharp
 *
 * [121] 买卖股票的最佳时机
 */

// @lc code=start
public class Solution
{
    public int MaxProfit(int[] prices)
    {
        if (prices.Length == 0)
        {
            return 0;
        }

        int p = 0;  // 利润
        /*
        int pricesLen = prices.Length;

        for (int i = 0; i < pricesLen; i++)
        {
            for (int m = i + 1; m < pricesLen; m++)
            {
                int tmpP = prices[m] - prices[i];

                if (tmpP > p)
                {
                    p = tmpP;
                }
            }
        }
        */
        int b = prices[0];  // 购买价格
        for (int i = 1; i < prices.Length; i++)
        {
            if (prices[i] <= b)
            {
                b = prices[i];
            }
            else if (prices[i] - b > p)
            {
                p = prices[i] - b;
            }
        }

        return p;
    }
}
// @lc code=end

