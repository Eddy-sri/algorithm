"""
    [5, 7, 7, 8, 8, 8, 10] , 8 ==> [3, 5]
    [5, 7, 7, 8, 8, 8, 10] , 11 ==> [None, None]

"""


def search_range(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1
        else:
            break

    for i in range(len(lst)-1, -1, -1):
        if lst[i] == target:
            return[mid , i]

    return [None , None]

    

    




