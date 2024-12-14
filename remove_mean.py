"""
    [4, 5, 2, 8, -2, 5, 1, 9] ==> -2

"""


def remove_min(lst):
    result = []

    min = lst.pop(0)
    lst.append(min)

    for i in range(len(lst)):
        val = lst.pop(0)
        if val < min:
            min  = val
        result.append(val)
        lst.append(val)

    for i in range(len(result)):
        val = result.pop()
        if val != min:
            result.append(val)

    return f"{lst} -->{result} ==> {min}"
        
