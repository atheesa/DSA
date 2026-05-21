from typing import List, Dict, Set, Optional, Tuple, Any
from collections import deque, Counter, defaultdict
import heapq
import bisect
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root
    def dfs(self,root):
        if root == None:
            return
        t1 = root.left
        t2 = root.right
        root.left = t2
        root.right = t1
        self.dfs(root.left)
        self.dfs(root.right)
        return
    


 
# --- Test with your <leader>r shortcut ---
if __name__ == "__main__":
    solver = Solution()
    print('Result:', solver.method_name(args))
