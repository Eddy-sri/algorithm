"""
    [4, 7, 2, 9, 3, 6, 7] ==> [2, 3, 4, 6, 7, 7, 9]
    
"""

def bead_sort(seq):
    if any(not isinstance(i, int) or i <= 0 for i in seq):
        raise TypeError("The input must be a sequence of natural numbers")
    
    for _ in range(len(seq)):
        for i, (first, secend) in enumerate(zip(seq, seq[1:])):
            if first > secend:
                seq[i], seq[i+1] = seq[i+1], seq[i]

    return seq


