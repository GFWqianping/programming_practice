"""
https://leetcode-cn.com/problems/positions-of-large-groups/
830.较大分组的位置
给定字符串s，返回字符串里长度大于等于3的连续字母的位置,按顺序输出
"""
from typing import List


class Solution:
    test_in_eg = ("abbxxxxzzy", "abc", "abcdddeeeeaabbbcd", "abaa")
    test_out_eg = ([[3, 6]], [], [[3, 5], [6, 9], [12, 14]], [])

    def test(self):
        for i in range(len(self.test_in_eg)):
            if self.test_out_eg[i] != self.largeGroupPositions(self.test_in_eg[i]):
                print(f'error{self.test_in_eg[i]}')
                return
        print('a')
        return

    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        start = 0
        length = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                length += 1
            else:
                if length >= 3:
                    res.append([start, i-1])
                length = 1
                start = i
            if i == len(s) - 1:
                if length >= 3:
                    res.append([start, i])
        return res


if __name__ == '__main__':
    s = Solution()
    s.test()
