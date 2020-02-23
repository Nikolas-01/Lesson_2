class Rectangle:
    def __init__ (self):
        self.width = None
        self.length = None
    def diagonal(self):
        return ((self.length**2) + (self.width**2))**0.5

rectangle = Rectangle()
rectangle.length = float(input('введите длину:'))
rectangle.width = float(input('введите ширину:'))
diagonal = rectangle.diagonal()
print ("Диагональ:")
print(diagonal)