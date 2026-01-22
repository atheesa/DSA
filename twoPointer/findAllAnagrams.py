def find_all_anagrams(original: str, check: str) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    # Example 2
    # Input: original = "abab", check = "ab"

    # Output: [0, 1, 2]
    # ans = []
    # checkHashMap = {}
    # canditateHashMap = {}
    
    # cbaebabacd
    # abc
    #### ------------- SOLUTION 1 ----------------------------------------------------- 
    # for ch in check:
        # if ch in checkHashMap:
            # checkHashMap[ch] += 1
        # else:
            # checkHashMap[ch] += 1
     
    # l,r = 0,0
    
    # while(l < len(original) and r<len(original)):
        # if (original[l] in checkHashMap):
            # count = 0
            # while(r< len(original) and count < len(check)):
                # if (original[r] in canditateHashMap):
                    # canditateHashMap[original[r]] += 1
                # else:
                    # canditateHashMap[original[r]] == 1
                # count += 1
                # r += 1
            # if canditateHashMap == checkHashMap:
                # ans.append(l)
        
        # l += 1
        # r = l         
    #### ----------------------- SOLUTION 2 -------------------------------------------------------
    
    # Example 2
    # Input: original = "abab", check = "ab"

    # Output: [0, 1, 2]
    ans = []
    candiateWindow = [0]*26
    checkWindow = [0]*26
    
    for i in range(len(check)):
        checkWindow[ord(check[i]) - ord('a')] += 1
        candiateWindow[ord(original[i]) - ord('a')] += 1
    
    if(checkWindow ==  candiateWindow):
        ans.append(0) 
    
    for i in range(len(check),len(original)):
        candiateWindow[ord(original[i])- ord('a')] += 1
        candiateWindow[ord(original[i - len(check)]) - ord('a')] -= 1
        if candiateWindow == checkWindow:
            ans.append(i-len(check) - 1)

     
    return ans

if __name__ == "__main__":
    original = input()
    check = input()
    res = find_all_anagrams(original, check)
    print(" ".join(map(str, res)))
