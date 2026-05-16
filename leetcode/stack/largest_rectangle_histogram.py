from typing import List, Dict, Tuple, Optional, Set
from collections import Counter, deque, defaultdict
import heapq
import math
import bisect

class Solution:
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        pre_compute = []

        
        for r in range(len(heights)):
            ll = r  
            lr = r
            while(ll >= 0 and heights[ll] >= heights[r]):
                ll -= 1

            while(lr < len(heights) and heights[lr] >= heights[r]):
                lr += 1
            pre_compute[r] = lr - lr + 1
        
        ans = max([heights[i] * pre_compute[i] for i in range(len(heights))])
        return ans



# --- Test with your <leader>r shortcut ---
if __name__ == "__main__":
    solver = Solution()
    print('Result:', solver.largestRectangleArea([6,7]))
    print('Result:', solver.largestRectangleArea([1,3,7]))
