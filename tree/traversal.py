class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rolr_search(root):
    if root is None:
        return
    print(root.val)
    rolr_search(root.left)
    rolr_search(root.right)


def search_lp(root):
    stk = [root]
    while stk:
        n = stk.pop()
        print(n.val)
        stk.append(n.right) if n.right else ...
        stk.append(n.left) if n.left else ...


def bft_lp(root):
    que = [root]
    while que:
        n = que.pop(0)
        print(n.val)
        que.append(n.left) if n.left else ...
        que.append(n.right) if n.right else ...


def build_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    return root


if __name__ == '__main__':
    r = build_tree()
    rolr_search(r)
    print('*'*10)
    search_lp(r)
    print('*' * 10)
    bft_lp(r)
