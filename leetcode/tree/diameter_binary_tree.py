from typing import List, Dict, Set, Optional, Tuple, Any
from collections import deque, Counter, defaultdict
import heapq
import bisect
import math



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def dfs(root) -> int:
            if root == None:
                return 0
            l1 = dfs(root.left)
            r2 = dfs(root.right)
            self.ans = max(self.ans,l1 + r2)

            return max(l1,r2) + 1
        dfs(root)
        return self.ans

# --- Test with your <leader>r shortcut ---
if __name__ == "__main__":
    solver = Solution()
    print('Result:', solver.method_name(args))
