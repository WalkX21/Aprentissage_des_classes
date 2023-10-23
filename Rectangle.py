class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_info(self):
        print(
            "Given a rectangle wit length of " ,self.length, "and width of ",str(self.width)
        )

    def perimeter(self):
        self.perimeter = self.length*2 + self.width*2
        return self.perimeter
    
    def aire(self):
        self.aire = self.length*self.width
        return self.aire

a = int(input('Enter length : '))
b = int(input('Enter wifth : '))
rectangle = Rectangle(a, b)
rectangle.print_info()
print("it's perimeter : " , rectangle.perimeter())
print("it's area : " , rectangle.aire())
# commentaire
