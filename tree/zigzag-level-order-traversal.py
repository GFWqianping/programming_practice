"""
https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
103. 二叉树的锯齿形层序遍历
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def solution(root: TreeNode):
    queue = [root]
    re_queue = []
    re = []
    if not root:
        return []
    while queue or re_queue:
        layer = []
        for node in queue:
            layer.append(node.val)
            node.left and re_queue.append(node.left)
            node.right and re_queue.append(node.right)

        layer and re.append(layer)
        queue.clear()
        layer = []

        for node in re_queue:
            node.left and queue.append(node.left)
            node.right and queue.append(node.right)
        re_queue.reverse()
        for node in re_queue:
            layer.append(node.val)
        layer and re.append(layer)
        re_queue.clear()
    return re
