from typing import List, Dict, Tuple, Optional, Set
from collections import Counter, deque, defaultdict
import heapq
import math
import bisect

class Solution:
             
    def largestRectangleArea(self, heights: List[int]) -> int:
    
        stack = deque()
        ans = 0  
        for i,h in enumerate(heights):
            mi = i
            while (stack and stack[-1][1] >h):
                li,lh = stack.pop() 
                mi = min(li,mi)
                ans = max(ans,(i - li)*lh)
            stack.append((mi,h))

        print(stack)
        while stack:
            li,lh = stack.popleft()
            ans = max(ans,(((len(heights) - 1)- li + 1 )* lh))
            # else:
            #     ans = max(ans,((len(heights) -1) - li + 1  * lh))
        
       # [6,7] 
        return ans 
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #
    #     cache = [0] * len(heights)
    #     pre_compute = [0] * len(heights)
    #
    #
    #     for r in range(len(heights)):
    #         ll = r  
    #         lr = r
    #         while(ll > 0 and heights[ll - 1] >= heights[r]):
    #             ll -= 1
    #
    #         while(lr < len(heights) - 1 and heights[lr + 1] >= heights[r]):
    #             lr += 1
    #         pre_compute[r] = lr - ll + 1
    #
    #     ans = max([heights[i] * pre_compute[i] for i in range(len(heights))])
    #     return ans
    #


# --- Test with your <leader>r shortcut  ---
if __name__ == "__main__":
    solver = Solution()
    print('Result:', solver.largestRectangleArea([6,7]))
    print('Result:', solver.largestRectangleArea([1,3,7]))
    print('Result:', solver.largestRectangleArea( [7,1,7,2,2,4]))
    print('Result:', solver.largestRectangleArea([2,4]))
    print('Result:', solver.largestRectangleArea([2,1,5,6,2,3]))
    print('Result:', solver.largestRectangleArea([2,1,2]))
    print('Result:', solver.largestRectangleArea([5,5,1,7,1,1,5,2,7,6]))
    print('Result:', solver.largestRectangleArea([2,7,6]))
 

    
