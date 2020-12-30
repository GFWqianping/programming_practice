"""
https://leetcode-cn.com/problems/squares-of-a-sorted-array/
"""


def solution(A):
    """
    length = len(A)
    for i in range(0, length):
        A[i] = A[i] * A[i]
    A.sort()
    return A

    # 执行用时：236 ms, 在所有 Python3 提交中击败了99.62%的用户
    # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了89.33%的用户
    """
    """
    #######
    res = [n*n for n in A]
    res.sort()
    return res
    # 简单实现
    # 执行用时：236ms, 在所有Python3提交中击败了99.62 %的用户
    # 内存消耗：15.5MB, 在所有Python3提交中击败了5.22 %的用户
    """
    length = len(A)
    stack = []
    res = []
    for i in range(0, length):
        if A[i] < 0:
            A[i] = A[i] * A[i]
            stack.append(A[i])
        else:
            A[i] = A[i] * A[i]
            while stack and stack[-1] <= A[i]:
                res.append(stack.pop())
            res.append(A[i])
    if len(res) != len(A):
        stack.reverse()
        res += stack
    return res





