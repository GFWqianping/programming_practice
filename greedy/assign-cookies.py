"""
https://leetcode-cn.com/problems/assign-cookies/
455. 分发饼干

"""
from typing import List


class Solution:
    test_in_eg = [([1, 2, 3], [1, 1]), ([1, 2], [1, 2, 3]), ([10, 9, 8, 7], [5, 6, 7, 8])]
    test_out_eg = [1, 2, 2]

    def test(self):
        for i in range(len(self.test_in_eg)):
            if self.test_out_eg[i] != self.findContentChildren(*self.test_in_eg[i]):
                print(f'error{self.test_in_eg[i]}')
                return
        print('a')
        return

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        meet = 0
        for kid in g:
            while s:
                cookie = s.pop(0)
                if cookie >= kid:
                    meet += 1
                    break
        return meet


if __name__ == '__main__':
    s = Solution()
    s.test()
