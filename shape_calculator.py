class Rectangle:
    
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.area = 0
        
    def set_width(self, new_w):
        self.width = int(new_w)
        self.side = int(new_w)
        
    def set_height(self, new_h):
        self.height = int(new_h)
        self.side = int(new_h)
        
    def get_area(self):
        self.area = self.width * self.height
        return self.area
        
    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter
    
    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal
    
    def get_picture(self):
        x = ''
        if self.width > 50 or self.height > 50:
            x = 'Too big for picture.'
            return x
        for i in range(self.height):
            for n in range(self.width):
                x += f'*'
            x += f'\n'
        
        return x
    
    def get_amount_inside(self, poly):
        new_h = self.width // poly.width
        new_w = self.height // poly.height

        return new_w * new_h
        
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    
    def __init__(self, side):
        #super().__init__(width,height)
        self.side = side
        self.width = int(side)
        self.height = int(side)
    
    def set_side(self, new_s):
        self.side = new_s
        self.width = int(new_s)
        self.height = int(new_s)
    
    def __str__(self):
        return f'Square(side={self.side})'
