/*
 * @lc app=leetcode.cn id=9 lang=csharp
 *
 * [9] 回文数
 */

// @lc code=start
public class Solution
{
    public bool IsPalindrome(int x)
    {
        if (x >= 0)
        {
            long tmp = 0;
            int inputX = x;

            while (inputX != 0)
            {
                tmp = tmp * 10 + inputX % 10;
                inputX = inputX / 10;

            }

            if (tmp > int.MaxValue || tmp < int.MinValue)
            {
                return false;
            }
            else
            {
                return (int)tmp == x;
            }
        }
        else
        {
            return false;
        }


    }
}
// @lc code=end

