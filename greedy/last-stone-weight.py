"""
https://leetcode-cn.com/problems/last-stone-weight/
1046. 最后一块石头的重量

一堆石头重量正整数，每次选最大的两个粉碎
粉碎结果是差值，求最后剩下的石头重量
1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
from typing import List


# def binary_insert(li: List[int], num: int):
#     le = 0
#     ri = len(li) - 1
#     mid = (ri - le) // 2
#     while le < ri - 1:
#         mid = (ri-le) // 2 + le
#         if li[mid] > num:
#             le = mid
#         else:
#             ri = mid
#
#     index = mid + 1 if li[mid] > num else mid
#     li.insert(index, num)


class Solution:
    test_in_eg = [[2, 7, 4, 1, 8, 1]]
    test_out_eg = [1]

    def test(self):
        for i in range(len(self.test_in_eg)):
            if self.test_out_eg[i] != self.lastStoneWeight(*self.test_in_eg[i]):
                print(f'error{self.test_in_eg[i]}')
                return
        print('a')
        return

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            max_stone = stones.pop(0)
            sub_max_stone = stones.pop(0)
            d = max_stone - sub_max_stone
            if d > 0:
                stones.append(d)
                stones.sort(reverse=True)
        return stones[0] if stones else 0


if __name__ == '__main__':
    # s = Solution()
    # s.test()
