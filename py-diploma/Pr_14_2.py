class RectArea:
    def area(self,length,breadth):
        rect=(length*breadth)
        print("Area of Rectangle is:",rect)
class SqrArea(RectArea):
    def area(self,side):
        self.side=side
        sq=self.side*self.side
        print("Area of Square is:",sq)
obj=RectArea()
obj.area(10,44)
obj1=SqrArea()
obj1.area(8)