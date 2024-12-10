"""
arr ---> [1, 2, 3, 4, 5, 6, 7]
 min = 4 ---> [4, 5, 6, 7]
 max = 4 ---> [1, 2, 3, 4]

"""

def limit (arr, min = None, max = None):
    min_check = lambda val : True if min == None else (val >= min) 
    max_check = lambda val : True if max == None else (val <= max)

    return [val for val in arr if min_check(val) and max_check(val)]

