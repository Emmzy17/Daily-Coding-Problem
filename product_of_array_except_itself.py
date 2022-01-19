def product_of_array_except_itself(arr):
    res = [1] * len(arr)
    prefix = 1
    for i in range(len(arr)):
        res[i] *= prefix
        prefix*=arr[i]

    postfix =1
    for i in range(len(arr)-1, -1, -1):
        res [i] *=postfix
        postfix *=arr[i]

    return res

l1 = [2,3,5]
print(product_of_array_except_itself(l1))