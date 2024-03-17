pie=22/7
r=int(input("Enter Radius of cylinder: "))
h=int(input("Enter Height of cylinder: "))

SA=2*pie*r*(h+r)
Vol=pie*r*r*h

print("The Surface Volume of Cylinder is :{:.3f}".format(Vol))
print("The Surface Area of Cylinder is :{:.3f}".format(SA))