class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return 2*(self.length + self.width)

class Square(Shape):
    def __init__(self, s):
        self.s1 = s

    def calculate_perimeter(self):
        return 4*(self.s1)


s1 = Square(4)
r1 = Rectangle(2, 4)
s1.what_am_i()
r1.what_am_i()