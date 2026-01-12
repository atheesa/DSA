def container_with_most_water(arr: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    l,r = 0,len(arr)-1
    area = 0
    while(l<r):
        width = r - l
        height = min(arr[l],arr[r])
        area = max(area,width * height)

        if(arr[l] > arr[r]):
            r -= 1
        else:
            l += 1
    
    return area

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = container_with_most_water(arr)
    print(res)
