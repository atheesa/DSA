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

def tree_max_depth(root: Node) -> int:

    return dfs(root,0)

def dfs(root, depth) -> int:
    if root == None:
        return depth + 1
    return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    res = tree_max_depth(root)
    print(res)


# --- Test with your <leader>r shortcut ---
if __name__ == "__main__":
    solver = Solution()
    print('Result:', solver.method_name(args))
