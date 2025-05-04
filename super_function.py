# Using and explaining Super function

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius} cm^2")
        super().describe()

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width} cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, height, width):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width
    def describe(self):
        print(f"It is a triangle of area {self.width * self.height * 0.5}")
        super().describe()

circle = Circle(color="red",is_filled = True,radius= 5)
square = Square(color="blue",is_filled= False,width= 4)
triangle = Triangle(color="green",is_filled= True, height=5,width= 3)

circle.describe()






