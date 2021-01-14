"""
https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/
1018.可被5整除的二进制前缀
输入一个0，1组成的数组
输出由从0：i的数组成的2进制数能不能被5整除的bool组成的结果answer
"""
from typing import List


class Solution:
    test_in_eg = ([0, 1, 1], [1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1])
    test_out_eg = ([True, False, False], [False, False, False], [True, False, False, False, True, False],
                   [False, False, False, False, False])

    def test(self):
        for i in range(len(self.test_in_eg)):
            if self.test_out_eg[i] != self.prefixesDivBy5(self.test_in_eg[i]):
                print(f'error{self.test_in_eg[i]}')
                return
        print('Access')
        return

    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        dec_num = 0
        answer = []
        for i in A:
            dec_num = dec_num * 2 + i
            answer.append(dec_num % 5 == 0)
        return answer


if __name__ == '__main__':
    s = Solution()
    s.test()
