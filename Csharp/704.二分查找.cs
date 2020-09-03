/*
 * @lc app=leetcode.cn id=704 lang=csharp
 *
 * [704] 二分查找
 */

// @lc code=start
public class Solution
{
    public int Search(int[] nums, int target)
    {
        if (nums.Length == 0)
        {
            return -1;
        }

        int s = 0;
        int e = nums.Length - 1;
        int m;

        while (s <= e)
        {
            m = (s + e) / 2;
            if (nums[m] == target)
            {
                return m;
            }
            else if (target > nums[m])
            {
                s = m + 1;
            }
            else
            {
                e = m - 1;
            }

        }

        return -1;

    }
}
// @lc code=end

