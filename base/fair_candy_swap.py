"""
https://leetcode-cn.com/problems/fair-candy-swap/
888.公平的糖果棒交换
两个数组各取一个数，交换使两数组的和相等（题目保证这两个数一定存在）
返回这两个数
"""
from typing import List


class Solution:
    test_in_eg = (([1, 1], [2, 2]), ([1, 2], [2, 3]), ([2], [1, 3]), ([1, 2, 5], [2, 4]))
    test_out_eg = ([1, 2], [1, 2], [2, 3], [5, 4])

    def test(self):
        for i in range(len(self.test_in_eg)):
            if self.test_out_eg[i] != self.fairCandySwap(*self.test_in_eg[i]):
                print(f'error{self.test_in_eg[i]}')
                return
        print('Access')
        return

    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = sum(A)
        sum_b = sum(B)
        target = (sum_a + sum_b) // 2
        for a in A:
            if (a - sum_a + target) in B:
                return [a, a - sum_a + target]
        return []


if __name__ == '__main__':
    s = Solution()
    s.test()
