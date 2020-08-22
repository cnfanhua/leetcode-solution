/*
 * @lc app=leetcode.cn id=58 lang=csharp
 *
 * [58] 最后一个单词的长度
 */

// @lc code=start
public class Solution
{
    public int LengthOfLastWord(string s)
    {
        var arr = s.Split(new[] { " " }, StringSplitOptions.RemoveEmptyEntries);
        return arr.Length > 0 ? arr[arr.Length - 1].Length : 0;
    }
}
// @lc code=end

