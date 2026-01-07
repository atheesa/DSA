def remove_duplicates(arr: list[int]) -> int:
    l,r=0,0
    # 0  
    while(r < len(arr)):
        if(arr[l] != arr[r]):
            l +=1
            arr[l] = arr[r]
        
        r += 1
    return l + 1

# [0,0,1,1,1,2,2]


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))
