"""
[1, 3, 5, 7, 9],[2, 4, 6, 8,10, 12, 14]
1
2
3
4
5
6
7
8
9
10
12
14

"""

class Zigzag:
    def __init__(self, lst1, lst2):
        self.lst = [lst1, lst2]

    def next(self):
        zig = self.lst.pop(0)
        zag = zig.pop(0)
        if zig:
            self.lst.append(zig)
        
        return zag
    
    def has_next(self):
        if self.lst:
            return True
        return False
    
z = Zigzag([1, 3, 5, 7, 9],[2, 4, 6, 8,10, 12, 14])

while z.has_next():
    print(z.next())
        