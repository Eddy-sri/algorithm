"""
    rotate
        rotate("hello", 2) return "llohe"
        rotate("hello", 5) return "hello"
        rotate("hello", 6) return "elloh"
        rotate("hello", 7) return "llohe"

"""

def rotate(str, shift):
    added_str = str + str

    if shift > len(str):
        shift = shift % len(str)

    return added_str[shift : shift + len(str)]
    

