class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print("Addition:",d.Summation(30,20))
print("Multiplication:",d.Multiplication(12,20))
print("Division:",d.Divide(20,20))
