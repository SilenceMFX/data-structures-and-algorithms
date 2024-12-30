from typing import Optional


class TreeNode:
    """ 二叉树节点类"""

    def __init__(self, val: int):
        self.val: int = val  # 节点值
        self.left: Optional[TreeNode] = None  # 左子节点引用
        self.right: Optional[TreeNode] = None  # 右子节点引用


pre_list = []


def pre_order(root: TreeNode) -> Optional[TreeNode]:
    if root is None:
        return
    pre_list.append(root.val)
    pre_order(root.left)
    pre_order(root.right)


in_list = []


def in_order(root: TreeNode) -> Optional[TreeNode]:
    if root is None:
        return
    in_order(root.left)
    in_list.append(root.val)
    in_order(root.right)


post_list = []


def post_order(root: TreeNode) -> Optional[TreeNode]:
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    post_list.append(root.val)


if __name__ == '__main__':
    n1 = TreeNode(val=1)
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)
    n6 = TreeNode(val=6)
    n7 = TreeNode(val=7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    pre_order(n1)
    in_order(n1)
    post_order(n1)
    print(pre_list)
    print(in_list)
    print(post_list)
