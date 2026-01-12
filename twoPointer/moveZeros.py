# Input:

# [1, 0, 2, 0, 0, 7]
# Output:

# [1, 2, 7, 0, 0, 0]

def move_zeros(nums: list[int]) -> None:
    l,r = 0,0
    while(r < len(nums)):
        if nums[l] == 0:
            while(r<len(nums)):
                if nums[r] != 0:
                    
        

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    move_zeros(nums)
    print(" ".join(map(str, nums)))
