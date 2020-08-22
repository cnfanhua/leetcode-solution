/*
 * @lc app=leetcode.cn id=7 lang=csharp
 *
 * [7] 整数反转
 */

// @lc code=start
public class Solution
{
    public int Reverse(int x)
    {
        long tmp = 0;

        int inputX = x;

        while (inputX != 0)
        {
            tmp = tmp * 10 + inputX % 10;
            inputX = inputX / 10;
        }

        if (tmp < int.MinValue || tmp > int.MaxValue)
        {
            return 0;
        }

        return (int)tmp;
    }
}
// @lc code=end

