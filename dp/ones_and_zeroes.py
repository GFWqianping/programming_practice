"""
https://leetcode-cn.com/problems/ones-and-zeroes/

测试用例：
findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"],9,80)
findMaxForm(["0","1101","01","00111","1","10010","0","0","00","1","11","0011"],63,36)
findMaxForm(["10","0001","111001","1","0"],3,4) 3
"""
from typing import List
import time


def findMaxForm(strs: List[str], m: int, n: int) -> int:
    start = time.time()
    account_tuple_list = []
    for bin_str in strs:
        z = bin_str.count('0')
        o = bin_str.count('1')
        account_tuple_list.append((z, o))
    re = min_list_sum(account_tuple_list, m, n)
    end = time.time()
    print('用时:', end-start)
    return re


def min_list_sum(tuple_list: List[tuple], m: int, n: int):
    queue = [tuple_list]
    while len(queue):
        zero_sum = 0
        one_sum = 0
        root = queue.pop(0)
        for z, o in root:
            zero_sum += z
            one_sum += o
        if m >= zero_sum and n >= one_sum:
            return len(root)
        if len(root) < 2:
            return 0
        for z, o in root:
            if m >= (zero_sum - z) and n >= (one_sum - o):
                return len(root) - 1
        for index in range(len(root)):
            queue.append(root[0:index] + root[index+1: len(root)])


"""
此算法时间复杂度过高，会报超时
最多运算8层，时间小于2秒

findMaxForm(["10","0001","111001","1","10","1","0101"],1,0)   7层                                                                                                                                                                   
用时: 0.03465890884399414

findMaxForm(["10","0001","111001","1","10","1","111","0101"],1,0)  8层                                                                                                                                                            
用时: 1.8741350173950195

findMaxForm(["10","0001","111001","1","10","1","111","0101","1001"],1,0) 9层                                                                                                                                                       
用时: 148.92271184921265

"""
