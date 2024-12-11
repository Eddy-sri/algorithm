"""
[1, 3, 5, 6] -> 3 ==> 1
[1, 3, 5, 6] -> 4 ==> 2
[1, 3, 5, 6] -> 7 ==> 4
[1, 3, 5, 6] -> 0 ==> 0

"""

def search(arr,num):
    first = 0
    last = len(arr) - 1
    mid = last // 2

    while first <= last:
        if num > arr[mid]:
            mid += 1
            first = mid
        else:
            mid -= 1
            last = mid
    return first
