# https://leetcode-cn.com/problems/ones-and-zeroes/
from typing import List


def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    account_tuple_list = []
    for bin_str in strs:
        z = bin_str.count('0')
        o = bin_str.count('1')
        account_tuple_list.append((z, o))



def min_list_sum(sub_strs: List[tuple]):

