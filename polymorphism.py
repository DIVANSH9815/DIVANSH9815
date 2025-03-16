from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
       return 3.14 * self.radius ** 2 
    
class triangle(shape):
    def __init__(self,base):
        self.base = base
        
    def area(self):
        return  self.base ** 2

class square(shape):
    def __init__(self,height,base):
        self.height = height 
        self.base = base
        
    def area(self):
        return 0.5 * self.height * self.base 
    
class pizza (circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping = topping
        
shapes = [circle(4),triangle(7),square(6,8),pizza("pepperoni",67)]


for shape in shapes:
    print(shape.area())
