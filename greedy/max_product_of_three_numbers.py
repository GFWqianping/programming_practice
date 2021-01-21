"""
https://leetcode-cn.com/problems/maximum-product-of-three-numbers/
628.三个数的最大乘积
输入: 数组nums    3<=len(num)<=10^4  -1000<=nums[i]<=1000
输出: 在数组中找出由三个数组成的最大乘积，并输出这个乘积
"""
from typing import List


def re_insert(re_l: List[int], num: int):
    if num < re_l[0]:
        re_l.insert(0, num)
    elif num < re_l[1]:
        re_l.insert(1, num)
    else:
        re_l.append(num)


class Solution:
    test_in_eg = ([1, 2, 3], [1, 2, 3, 4], [-100, -98, -1, 2, 3, 4], [-1, -2, -3], [-1, -2, -3, -4])
    test_out_eg = (6, 24, 39200, -6, -6)

    def test(self):
        for i in range(len(self.test_in_eg)):
            if self.test_out_eg[i] != self.maximumProduct(self.test_in_eg[i]):
                print(f'error{self.test_in_eg[i]}')
                return
        print('Access')
        return

    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        re_list = []
        re_list.sort()
        two_min_negative_nums = []
        negative_count = 0
        for n in nums:
            if n < 0:
                negative_count += 1
                if len(two_min_negative_nums) < 2:
                    two_min_negative_nums.append(n)
                    two_min_negative_nums.sort()
                elif n < two_min_negative_nums[0]:
                    two_min_negative_nums[1], two_min_negative_nums[0] = two_min_negative_nums[0], n
                elif n < two_min_negative_nums[1]:
                    two_min_negative_nums[1] = n
            if len(re_list) < 3:
                re_list.append(n)
                re_list.sort()
            elif n > re_list[0]:
                re_list.pop(0)
                re_insert(re_list, n)

        if len(two_min_negative_nums) == 2 and len(nums) != negative_count \
                and two_min_negative_nums[0] * two_min_negative_nums[1] > re_list[0] * re_list[1]:
            re = two_min_negative_nums[0] * two_min_negative_nums[1] * re_list[2]
        else:
            re = re_list[0] * re_list[1] * re_list[2]
        return re


if __name__ == '__main__':
    s = Solution()
    s.test()
