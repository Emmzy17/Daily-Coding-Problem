def maxProduct(arr):
    res = max(arr)
    currMin, currMax = 1,1

    if len(arr) == 1:
        return res
    if len(arr) == 0:
        return arr
    for n in arr:
        if n == 0:
            currMin, currMax = 1,1
        tmp = currMax * n
        currMax = max(currMax * n, n*currMin, n)
        currMin = min(tmp, n*currMin, n)
        res = max(res, currMax)
    return res

print(maxProduct([2,3,-5,-1,0,2]))
print(maxProduct([5,6,2,9,2]))
print(maxProduct([-4,-9,-5,-7,-3,-2])) 