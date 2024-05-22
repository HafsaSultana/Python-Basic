#A1:
class Circle:
    radius=1.0
    def _int_(self,radius):
        self.radius=radius
        print("Interd Circle")

    def _str_(self):
        return "Circle from str function."

    def _repr_(self):
        return "Circle from repr function."

    def get_area(self):
        return 3.1416 *(self.radius*self.radius)#A1:


class Cylinder(Circle):

    height=1.0
    def _int_(self,radius,height):
        self.radius=radius
        self.height=height
        print("Interd Cylinder")

    def _str_(self):
        return "Cylinder from str function."

    def _repr_(self):
        return "Cylinder from repr function."

    def get_area(self):
            #A=2πrh+2πr2
        return (2*3.1416 *self.radius*self.height)+(2*3.1416 *self.radius*self.radius )

    def get_volume(self):
        return (3.1416 *(self.radius*self.radius)*self.height)


A=Circle(5.0)
B=Cylinder(5.0,1.0)

A._str_()
B._repr_()
A.get_area_()
B.get_area_()            
