"""
https://leetcode-cn.com/problems/find-pivot-index/
724.寻找数组的中心索引
找出数组中左侧和等于右侧和的索引,找不到返回-1
"""
from typing import List


class Solution:
    test_in_eg = ([1, 7, 3, 6, 5, 6], [1, 2, 3], [2, 1, -1], [0, 0, 0, 0, 1])
    test_out_eg = (3, -1, 0, 4)

    def test(self):
        for i in range(len(self.test_in_eg)):
            if self.test_out_eg[i] != self.pivotIndex(self.test_in_eg[i]):
                print(f'error{self.test_in_eg[i]}')
                return
        print('Access')
        return

    def pivotIndex(self, nums: List[int]) -> int:
        sum_list = []
        bef_sum = 0
        for n in nums:
            sum_list.append(bef_sum + n)
            bef_sum += n
        for i in range(len(sum_list)):
            if i == 0:
                left = 0
            else:
                left = sum_list[i - 1]
            right = sum_list[-1] - sum_list[i]
            if left == right:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    s.test()
