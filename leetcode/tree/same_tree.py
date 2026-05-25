from typing import List, Dict, Tuple, Optional, Set
from collections import Counter, deque, defaultdict
import heapq
import math
import bisect

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def same_tree(p: Node, q: Node) -> bool:
    
    return dfs(p,q)


def dfs(root1, root2) -> bool:
    if root1 == None and root2 == None:
        return True
    elif root1 == None or root2 == None:
        return False
    elif root1.val != root2.val:
        return False
    return dfs(root1.right,root2.right) and dfs(root1.left,root2.left)


def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

# if __name__ == "__main__":
#     p = build_tree(iter(input().split()), int)
#     q = build_tree(iter(input().split()), int)
#     res = same_tree(p, q)
#     print("true" if res else "false")
#
#
# # --- Test with your <leader>r shortcut ---
# if __name__ == "__main__":
#     print('Result:)
