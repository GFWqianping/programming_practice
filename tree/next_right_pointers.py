"""
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    if not root:
        return root
    queue = [root]
    account = 0
    nums = 2

    while queue:
        node = queue[0]
        account += 1
        nums = nums * 2 if nums < account else nums
        if account != nums - 1 and len(queue) > 1:
            node.next = queue[1]
        if node.left and node.right:
            queue.append(node.left)
            queue.append(node.right)
        queue.pop(0)
    return root
