from ctypes import pointer
from operator import index


def two_sum(arr, target):
    dict_store = {}
    for n in range(len(arr)):
        for j in range(n+1, len(arr)):
            if arr[n] + arr[j] == target:
                return (arr[n], arr[j])
         
arr = [10,15,3]
print(two_sum(arr, 17))