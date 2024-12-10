"""
 arr ---> [1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6]
 Frequent_val = 5

"""

def most_repeated(arr):
    values = {}
    result = []
    frequent_val = 0

    for val in arr:
        if val in values.keys():
            values[val] += 1
        else:
            values[val] = 1
    
    frequent_val = max(values.values())
    
    for val in values.keys():
        if values[val] == frequent_val:
            result.append(val)
    return result
        
