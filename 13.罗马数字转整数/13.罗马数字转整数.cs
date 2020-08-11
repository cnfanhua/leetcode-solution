/*
 * @lc app=leetcode.cn id=13 lang=csharp
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
public class Solution
{
    public int RomanToInt(string s)
    {
        s = s.Replace("IV", "Q").Replace("IX", "W").Replace("XL", "E").Replace("XC", "R").Replace("CD", "T").Replace("CM", "Y");

        int result = 0;
        for (int i = 0, j = s.Length; i < j; i++)
        {
            switch (s[i])
            {
                case 'I':
                    result += 1;
                    break;
                case 'V':
                    result += 5;
                    break;
                case 'X':
                    result += 10;
                    break;
                case 'L':
                    result += 50;
                    break;
                case 'C':
                    result += 100;
                    break;
                case 'D':
                    result += 500;
                    break;
                case 'M':
                    result += 1000;
                    break;
                case 'Q':
                    result += 4;
                    break;
                case 'W':
                    result += 9;
                    break;
                case 'E':
                    result += 40;
                    break;
                case 'R':
                    result += 90;
                    break;
                case 'T':
                    result += 400;
                    break;
                case 'Y':
                    result += 900;
                    break;
            }
        }

        if (result >= 1 && result <= 3999)
        {
            return result;
        }
        return 0;

    }
}
// @lc code=end

