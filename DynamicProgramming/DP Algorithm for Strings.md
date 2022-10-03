# LCP（Longest Common Prefix）

用$lcp[i][j]$表示字符串$s$从下标$i$开始的后缀和从下标$j$ 开始的后缀之间的最长公共前缀，那么
$$
s[i:j] = s[j:2*j-i] \Leftrightarrow j-i \leq lcp(i,j).
$$
可用动态规划求LCP：
$$
lcp(i,j)= 
\left\{ 
\begin{align}
&lcp(i+1,j+1) +1 ,&s[i] = s[j]\\
&0, &s[i] \neq s[j]
\end{align}
\right.
$$



# LCS

## Longest Common Substring

用$lcs[i][j]$ 来表示字符串 $s1$ 前 $i$ 个字符和 $s2$ 前$j$ 个字符的公共子串（连续的）长度。

可用动态规划求LCS：
$$
lcs[i][j] = \left \{ 
\begin{align}
&lcs[i-1][j-1] + 1 , &s[i] = s[j] \\
&1, &s[i] \neq s[j]
\end{align}
\right.
$$
取$\max{(lcs)}$ 即得最长公共子串的长度。

## Longest Common Subsequence

子序列与子串的不同在于它并不要求连续，状态转移方程如下：
$$
lcs[i][j] = \left \{ 
\begin{align}
&lcs[i-1][j-1] + 1 , &s[i] = s[j] \\
&\max (lcs[i-1][j], lcs[i][j-1]), &s[i] \neq s[j]
\end{align}
\right.
$$


# LIS (Longest Increasing Subsequence)

不要求子序列连续：
$$
dp[i] = \max(dp[j]) + 1, \quad 0 \leq j < i \quad AND  \quad nums[j] < nums[i]
$$
要求连续，即LCIS (Longest Continuous Increasing Subsequence):
$$
dp[i] = \left \{ 
\begin{align}
&dp[i-1] + 1 , &nums[i] > nums[i-1] \\
&1, &otherwise
\end{align}
\right.
$$


# LPS(Longest Palindrome Subsequence\Substring)

## Longest Palindrome subsequence

$dp[i][j]$ 表示$s[i:j+1]$ 中的最大回文长度，当 $i = j$ 时，$dp[i][j] = 1$ ,下设 $i < j$ :
$$
dp[i] = \left \{ 
\begin{align}
&dp[i+1][j+1] + 2 , &s[i] = s[j] \\
&\max(dp[i][j-1],dp[i-1][j]), &otherwise
\end{align}
\right.
$$

## Longest Palindrome substring

用$p(i,j)$ 表示字符串$s$ 的第$i$ 到$j$ 个字母组成的串，其边界条件：
$$
\left\{
\begin{align}
& p(i,i) = true \\
&p(i,i+1) = (s_i == s_{i+1})
\end{align}
\right.
$$
状态转移方程：
$$
p(i,j)=p(i-1,j-1) \land (s_i == s_j)
$$


# ED(Edit Distance)

最小编辑距离，又称 Levenshtein 距离，它是指两个字符串之间通过增、删、替换(改)三种变换能够使字符串相同的最小编辑次数，用来衡量两个字符串的字符距离（每一次增、删、替换，都算作距离为1）。

> Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
> You have the following 3 operations permitted on a word:
> 1.Insert a character
> 2.Delete a character
> 3.Replace a character
> Example:
> Input: word1 = "horse", word2 = "ros"
> Output: 3
> Explanation: 
> horse -> rorse (replace 'h' with 'r')
> rorse -> rose (remove 'r')
> rose -> ros (remove 'e')

You can solute this problem from [LeetCode]([编辑距离 - 编辑距离 - 力扣（LeetCode）](https://leetcode.cn/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode-solution/)).

用 $dp[i][j]$ 表示$A$ 的前$i$ 个字母和$B$ 的前$j$ 个字母之前的编辑距离。

状态转移方程：
$$
dp[i][j] = \left \{ 
\begin{align}
&1+\min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]-1) , &A_i == b_j \\
&1+\min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]), &A_i \neq B_j
\end{align}
\right.
$$
边界条件：
$$
\left\{
\begin{align}
& dp[i][0] = i \\
& dp[0][j] = j
\end{align}
\right.
$$


