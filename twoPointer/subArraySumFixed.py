def subarray_sum_fixed(nums: list[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    # 1 2 3 7 4 1
    # 3
    currWindow = sum(nums[:k])
    ans = currWindow
    
    for i in range(k,len(nums)):
        currWindow += nums[i]
        currWindow -= nums[i-k]
        ans = max(currWindow,ans)
    
    return ans


if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = subarray_sum_fixed(nums, k)
    print(res)
