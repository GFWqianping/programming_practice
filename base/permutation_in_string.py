"""
https://leetcode-cn.com/problems/permutation-in-string/
567.字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。
"""
from typing import List


class Solution:
    test_in_eg = (('ab', 'eidbaooo'), ('ab', 'eidboaoo'), ("adc", "dcda"))
    test_out_eg = (True, False, True)

    def test(self):
        for i in range(len(self.test_in_eg)):
            if self.test_out_eg[i] != self.checkInclusion(*self.test_in_eg[i]):
                print(f'error{self.test_in_eg[i]}')
                return
        print('Access')
        return

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for x in s1:
            s1_dict[x] = s1_dict.get(x) + 1 if s1_dict.get(x) else 1

        for i in range(len(s2)):
            if i + len(s1) > len(s2):
                break
            s2_dict = {}
            for x1 in s2[i:i+len(s1)]:
                s2_dict[x1] = s2_dict.get(x1) + 1 if s2_dict.get(x1) else 1
            if s1_dict == s2_dict:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    s.test()
