def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    l,r = 0,len(arr) - 1
    
    localSum = 0
    # [2, 3, 4, 5, 8, 11, 18]
    
    while(l < r):
        localSum = arr[l] + arr[r]
        if(localSum) == target:
            return [l,r]
        elif(localSum > target):
            r -= 1
        else:
            l += 1 
        
    
    
    return []




if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum_sorted(arr, target)
    print(" ".join(map(str, res)))
