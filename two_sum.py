"""

tow sum
[2, 7, 11, 15], 9 ==> index [1, 2]

"""

def two_sum(lst, target):
    
    cur1 = 0
    cur2 = len(lst) - 1

    while cur1 < cur2:
        num = lst[cur1] + lst[cur2]

        if num == target:
            return f'index ==> {cur1 + 1, cur2 + 1 }'
        elif num  < target:
            cur1 += 1
        elif num > target:
            cur2 -= 1
    return('can not make the target with this list')

