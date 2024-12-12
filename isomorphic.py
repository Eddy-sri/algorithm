"""
isomorphism, in modern algebra, a one-to-one correspondence (mapping)
 between two sets that preserves binary relationships between elements of the sets.
 For example, the set of natural numbers can be mapped
 onto the set of even natural numbers by multiplying each natural number by 2.

 foo , bar ==> false
 foo , bee ==> true
"""

def isomorphic(str_1, str_2):
    if len(str_1) != len(str_2):
        return False
    
    dict_val = {}
    set_val = set()

    for i in range(len(str_1)):
        if str_1[i] not in dict_val:
            if str_2[i] in set_val:
                return False
            dict_val[str_1[i]] = str_2[i]
            set_val.add(str_2[i])
        elif dict_val[str_1[i]] != str_2[i]:
            return False
        
    return True

