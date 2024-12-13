
def limit (arr, min = None, max = None):
    """
    >>> limit([1, 2, 3, 4, 5, 6, 7],4)
    [4, 5, 6, 7]
    >>> limit([1, 2, 3, 4, 5, 6, 7],None,4)
    [1, 2, 3, 4]
    >>> limit([1, 2, 3, 4, 5, 6, 7],2,5)
    [2, 3, 4, 5]
    """
    min_check = lambda val : True if min == None else (val >= min) 
    max_check = lambda val : True if max == None else (val <= max)

    return [val for val in arr if min_check(val) and max_check(val)]

