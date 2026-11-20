class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def set_width(self, units):
        self.width = units
        return

    def set_height(self, units):
        self.height = units
        return
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height)*2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
            
        charwidth = '*' * self.width + '\n'
        charheight = charwidth * self.height
        return charheight

    def get_amount_inside(self, shape):
        shape_width = self.width // shape.width
        shape_height = self.height // shape.height
        total_amount = shape_width * shape_height
        return total_amount

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_width(self, units):
        self.width = units
        self.height = units

    def set_height(self, units):
        self.height = units
        self.width = units

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'
