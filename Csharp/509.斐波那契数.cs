/*
 * @lc app=leetcode.cn id=509 lang=csharp
 *
 * [509] 斐波那契数
 */

// @lc code=start
public class Solution
{
    public int Fib(int N)
    {
        if (N < 1)
        {
            return 0;
        }

        if (N < 2)
        {
            return 1;
        }

        return Fib(N - 1) + Fib(N - 2);
    }
}
// @lc code=end

