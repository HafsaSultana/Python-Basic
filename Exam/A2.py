#A2:
class Shape:
    color='red'
    def _int_(self,color):
        self.color=color
        print("Interd Spape")

    def _str_(self):
        return "Spape from str function."

    def _repr_(self):
        return "Spape from repr function."

class Circle(Spape):
    radius=1.0
    def _int_(self,color,radius):
        self.color=color
        self.radius=radius
        print("Interd Circle")

    def _str_(self):
        return "Circle from str function."

    def _repr_(self):
        return "Circle from repr function."

    def get_area(self):
        return (3.1416 *(self.radius*self.radius)



class Rectangle(Spape):

    length=1.0
    width=1.0
    def _int_(self,color,length,width):
        self.color=color
        self.lengtht=length
        self.width=width
        print("Interd Rectangle")

    def _str_(self):
        return "Rectangle from str function."

    def _repr_(self):
        return "Rectangle from repr function."

    def get_area(self):
        return (self.length*self.width)

class Square(Rectangle):

    def _int_(self,color,length):
        self.color=color
        self.lengtht=length
        print("Interd Square")

    def _str_(self):
        return "Square from str function."

    def _repr_(self):
        return "Square from repr function."
